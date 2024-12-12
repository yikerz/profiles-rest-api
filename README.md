### Setting up your project

1. Initialize with git
2. Create file `.gitignore`
3. Create file `LICENSE` (optional)

### SSH linkage to GitHub

1. Generate ssh key ([cmd 1](#commands))
2. Add new ssh key on GitHub setting
3. Create new repo for this project

### Creating a development server

1. Initialize `ubuntu/bionic64` with Vagrant ([cmd 2](#commands))
2. Modify `Vagrantfile`
3. Create new VM ([cmd 3](#commands))
4. SSH to the Vagrant VM ([cmd 4](#commands))

### Create a Django app

1. SSH to vagrant server
2. Create a new python virtual env at `~/env` ([cmd 5](#commands))
3. Activate the virtual env ([cmd 6](#commands))
4. Create file `requirements.txt` in `/vagrant` (the sync folder)

- `django==2.2`
- `djangorestframework==3.9.2`

5. In the VM server, install the dependencies using `pip`
6. Start new project in the root folder using `django-admin` ([cmd 7](#commands))
7. Start new app called `profiles_api` ([cmd 8](#commands))
8. Add the following apps to the `INSTALLED_APPS` in `profiles_project/settings.py`

- `rest_framework`
- `rest_framework.authtoken`
- `profiles_api`

9. Run the server on `0.0.0.0:8000` ([cmd 9](#commands))

### Commands

1. `ssh-keygen -t rsa -b 4096 -C "yikerz0425@gmail.com"`
2. `vagrant init ubuntu/bionic64`
3. `vagrant up`
4. `vagrant ssh`
5. `python -m venv ~/env`
6. `source ~/env/bin/activate`
7. `django-admin.py startproject profiles_project .`
8. `python manage.py startapp profiles_api`
9. `python manage.py runserver 0.0.0.0:8000`
