## A simple dJango project

### Local Installation

Requirements

- Python 3.5

1. Create a Python 3.5 virtualenv

```sh
# install virtualenv if you don't have
pip3 install virtualenv

# create a virtualenv
virtualenv my-env

# Activate the virtualenv
source my-env/bin/activate
```

2. Clone the Project from Github

```sh
git clone https://github.com/ShafiurShamim/django-project.git

# Enter the Project directory
cd django-project
```

3. Install dependencies

```sh
pip install -r requirements.txt
```

4. We'll use Default sqlite3 database

```sh
# Create tables
python manage.py migrate
```

5. Create a superuser

```sh
python manage.py createsuperuser
```

6. For compiling scss and javascript, we'll use webpack. Here we need [Node.js](https://nodejs.org/en/), this project uses `node v8.10`.

```sh
# Install npm dependencies and run the development
npm install && npm run dev
```

7. Run the test suit

```sh
python manage.py test
```

8. Run the server

```sh
python manage.py runserver
```
