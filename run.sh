repo_name=$(awk -F': ' '/repo_name/ {print $2}' local_settings.txt)
repo_url=$(awk -F': ' '/repo_url/ {print $2}' local_settings.txt)
branch=$(awk -F': ' '/branch/ {print $2}' local_settings.txt)
f=../../git_report.txt

mkdir count
cd count
git clone $repo_url
cd $repo_name
git checkout $branch

if [ "$1" == "" ]
then
	commitlist=$(git rev-list $branch)
else
	commitlist=$(git rev-list $branch -$1)
fi

for commit in $commitlist
do
	git checkout $commit
	message=$(git log --format=%B -n 1 $commit)
	count=$(git ls-files | xargs wc -l)
	date=$(git log --format=%at -n 1 $commit)
	user=$(git log --format=%aN -n 1 $commit)

	echo $commit >> $f
	echo $message >> $f
	echo $count >> $f
	echo $date >> $f
	echo $user >> $f
done

cd ../../
rm -r -f count
python3 run.py
rm git_report.txt
