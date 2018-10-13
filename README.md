#Create Django R\E web app 
create python virutal environment.
kde-bot@kde-bot-MS-7751:~/dev/btre_app$ python3 -m venv ./venv

activate virtual environment
kde-bot@kde-bot-MS-7751:~/dev/btre_app$ source ./venv/bin/activate

Now from within the virtual environment...
>Upgrade Pip as needed
(venv) kde-bot@kde-bot-MS-7751:~/dev/btre_app$ pip install --upgrade pip
>Install Django
(venv) kde-bot@kde-bot-MS-7751:~/dev/btre_app$ pip install django
>Create project 
(venv) kde-bot@kde-bot-MS-7751:~/dev/btre_app$ django-admin startproject btre .
>Upgrade pylint
(venv) kde-bot@kde-bot-MS-7751:~/dev/btre_app$ /home/kde-bot/dev/btre_app/venv/bin/python -m pip install -U pylint