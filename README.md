# Local environment
Install python version 3.5.x

For mac Install Homebrew - http://brew.sh/
```
brew install python3
```
For Ubuntu/Debian
```
sudo apt-get install python3.5
```
Go to https://www.python.org/downloads/ for windows

Setup virtual environemnt
```
pip3 install --upgrade virtualenv
virtualenv -p python3 venv
```

# Dependencies and configurations
Clone code
```
git clone https://github.com/Ryan0006/vic-migrant-health.git
```
Install python package
```
source <path to venv>/venv/bin/activate
pip3 install -r requirements.txt
```
Set following environment variable
```
ALLOWED_HOSTS=<your allowed hosts>
SECRET_KEY=<your secret key>
EMAIL_HOST=<your email host>
EMAIL_HOST_USER=<your host user>
EMAIL_HOST_PASSWORD=<your host password>
EMAIL_PORT=<25/587>
GOOGLE_MAPS_API_KEY=<your Google Maps API key>
```

# Deploy application
For Windows, do extra as using Gitbash to run following commands.
For all,
Create superuser (optional)
```
python3 manage.py createsuperuser
```
Deploy to local server
```
python3 manage.py runserver
```
Deploy to production server

Refer to Django documentation checklist for details -  https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/
