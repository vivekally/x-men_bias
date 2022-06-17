## X-Men Bias identification service

### Running application
1. Install python 
2. Install virtual env

### 1.0 Install python
```
Install python according your os below example for linux

$ sudo apt-get update
$ sudo apt-get install python3.6

check by below command
$ python3 --version
```


### 2.0 To install virtual env and activate in Linux
```
$ python3 -m venv myvenv
$ source myvenv/bin/activate
```
### 2.1 Install all the dependency
```
$ python -m pip install --upgrade pip
$ pip install psycopg2-binary
$ pip install -r requirements.txt
```

### 2.3 Command to run application
```
$ python ./manage.py runserver
 ````