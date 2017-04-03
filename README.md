## GitCount
Count every line in a github repository

## Usage
1. Clone the github repository `git clone https://github.com/ecuatox/gitcount.git`
2. Enter the repository `cd gitcount`
3. Create a `local_settings.txt` file with the following information about your repository
```
repo_name: REPOSITORY_NAME
repo_url: https://github.com/USERNAME/REPOSITORY_NAME.git
branch: master
```
4. Create a `ignore.txt` file with regex expressions describing what to ignore
```
total
\.gitignore
.*fonts.*
.*__init__.py
.*\.svg
.*\.png
```
5. Make the script executable `chmod +x run.sh`
6. Run the script `./run.sh`
7. Display the report `cat report.txt`

## Example output
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
