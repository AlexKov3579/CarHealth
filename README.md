# CarHealth

This repo requires to be installed in [Python virtual environment](https://docs.python.org/3/library/venv.html)
Briefly, you have to create parent folder, where environment will be placed and open it with PowerShell.
```
python -m venv c:\path\to\myenv
```
Open folder with environment in powershell and execute script Activate.ps1
```
myenv/Scripts/Activate.ps1
```

In order to work, it also requires Django framework.
After you created and activated virtual environment, you can install Django with command
```
pip3 install django==3.1
```
After you install Django, clone this repo to the same folder with your virtual environment, example: 

ParentFolder

-  CarHealth
  
-  VirtEnv

After that, you can run the server with 
```
python manage.py runserver
```
from your parent folder, while virtual environment is active

After server started, it will show it's address. In order to access login page, go to http:/localhost:8000/login/login.html
