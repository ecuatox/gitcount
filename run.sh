repo_name=$(awk -F': ' '/repo_name/ {print $2}' local_settings.txt)
repo_url=$(awk -F': ' '/repo_url/ {print $2}' local_settings.txt)

mkdir count
cd count
git clone $repo_url
cd $repo_name

for commit in $(git rev-list master)
do
	git checkout $commit
	message=$(git log --format=%B -n 1 $commit)
	count=$(git ls-files | xargs wc -l)

	echo $commit >> ../../git_report.txt
	echo $message >> ../../git_report.txt
	echo $count >> ../../git_report.txt
	#echo >> ../../git_report.txt
done

cd ../../
sudo rm -r count
python3 run.py
sudo rm git_report.txt
