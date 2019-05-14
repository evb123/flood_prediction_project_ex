# Documentation for visualisation app
Author: Evelyn Byer / Megan Duffy
Date started: 05/04/2019
Date finished: 12/04/19

## Virtual environment
A virtual environment (Python 3.5) must be created in order to run the app.   
The environment must be created using the file 'mod_spec.txt' using the following command in the anaconda prompt:  
~~~
conda create --name rightsideDash --file mod_spec.txt.
~~~

## Code files
The dash app is stored in the folder 'honey'.
The folder honey must be downloaded and the working directory must point to it.
The app is started by running the file 'Main.py' and navigating on the browser to the url '127.0.0.1:port' where 'port' is the port number. 

## Data storage
Data is stored in JSON files and SQLite databases. In order to ensure that data has not been corrupted, check the hashes of the file against the following.

#### Commands to get hashes:
~~~
certutil.exe -hashfile .\rightside2.db MD5
certutil.exe -hashfile .\IloveSQLite.db MD5
~~~

#### Hashes:
MD5 hash of .\IloveSQLite.db: 5a62046079d437b4135ae7f68eae37f5

MD5 hash of .\rightside2.db: f9f673c1fbe4ae5991352b545c463b4f
