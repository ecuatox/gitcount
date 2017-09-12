## GitCount
Count every line in a github repository  
Get a full report as a txt file and excel sheet

## Usage
1. Clone the github repository `git clone https://github.com/tenstad/gitcount.git`
2. Enter the repository `cd gitcount`
3. Create a virtualenv `virtualenv -p python3 env`
4. Source the env `source env/bin/activate`
5. Install requirements `pip install -r requirements.txt`
6. Create a `local_settings.txt` file with the following information about your repository
```
repo_name: REPOSITORY_NAME
repo_url: https://github.com/USERNAME/REPOSITORY_NAME.git
branch: master
inverted: false
```
7. Create a `ignore.txt` file with regex expressions describing what to ignore
```
\.gitignore
.*fonts.*
.*__init__.py
.*\.svg
.*\.png
```
8. Make the script executable `chmod +x run.sh`
9. Run the script `./run.sh` or `./run.sh <number>` if you only want the last `<number>` commits
10. Display the report `cat report.txt` or open the excel document

## Example report.txt output
```
...

ae8795f27d10679ffbb565a2bb3123fd8cdca5bd
Fix FileNotFoundError when not using ignore.txt
Total 108
    7 .gitignore
   77 run.py
   24 run.sh

ef374c17481b4908d9db0fb19acfc184679c09d0
Create README.md
Total 150
    7 .gitignore
   42 README.md
   77 run.py
   24 run.sh

...
```
