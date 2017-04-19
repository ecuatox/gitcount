import re
import xlwt
from datetime import datetime

def local_setting(key):
	try:
		with open('local_settings.txt', 'r') as f:
			line = f.readline()
			while line:
				if line.startswith('%s: ' % key):
					return line.split(': ')[1].strip()
				line = f.readline()
		return ''
	except FileNotFoundError:
		return ''

def get_ignore():
	ignore = []

	try:
		f = open('ignore.txt', 'r')
	except FileNotFoundError:
		return ignore

	line = f.readline().strip()
	while line != '':
		ignore.append(line)

		line = f.readline().strip()

	f.close()
	return ignore

def get_data():
	data = []

	ignores = get_ignore()
	inverted = bool(eval(local_setting('inverted').capitalize()))
	if not inverted: ignores.append('total')

	f = open('git_report.txt', 'r')
	commit_id = f.readline().strip()

	while commit_id != '':
		message = f.readline().strip()
		count = f.readline().strip()
		date = f.readline().strip()
		user = f.readline().strip()

		commit = {}
		lines = count.split()
		i = 0
		total = 0
		while i < len(lines) - 1:
			if inverted:
				for ignore in ignores:
					if re.match(ignore, lines[i+1]):
						total += int(lines[i])
						commit[lines[i+1]] = int(lines[i])
						break
				i += 2
			else:
				match = False
				for ignore in ignores:
					if re.match(ignore, lines[i+1]):
						match = True
						break
				if match:
					i += 2
					continue

				total += int(lines[i])
				commit[lines[i+1]] = int(lines[i])
				i += 2

		data.append({
			'id': commit_id,
			'message': message,
			'data': commit,
			'date': date,
			'user': user,
			'total': total,
		})

		commit_id = f.readline().strip()

	f.close()
	return data

def main():

	wb = xlwt.Workbook()
	ws = wb.add_sheet('Sheet 1')

	ws.write(0, 0, 'Date')
	ws.write(0, 1, 'Commit ID')
	ws.write(0, 2, 'User')
	ws.write(0, 3, 'Lines')
	ws.write(0, 4, 'Messages')

	f = open('report.txt', 'w')
	data = get_data()[::-1]
	for a in enumerate(data):
		i, commit = a
		ws.write(i+1, 0, datetime.fromtimestamp(int(commit['date'])).strftime('%Y-%m-%d %H:%M:%S'))
		ws.write(i+1, 1, commit['id'])
		ws.write(i+1, 2, commit['user'])
		ws.write(i+1, 3, commit['total'])
		ws.write(i+1, 4, commit['message'])

		f.write(commit['id'] + '\n')
		f.write(commit['message'] + '\n')
		f.write('Total %r' % commit['total'] + '\n')
		lines = []
		for fname in commit['data']:
			lines.append((fname, str(commit['data'][fname]).rjust(5, ' ') + ' '))
		lines = sorted(lines)
		f.write('\n'.join(['%s%s' % (line[1], line[0]) for line in lines]) + '\n')
		f.write('\n')
	f.close()

	wb.save('report.xls')

main()
