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

### Setup the Database

#### Create user database model

1. Create class `UserProfile(AbstractBaseUser, PermissionsMixin)` in `profiles_api/models.py` ([cmd 10](#commands))

- `email`: `EmailField`
- `name`: `CharField`
- `is_active`: `BooleanField`
- `is_staff`: `BooleanField`
- Instantiate `UserProfileManager` object
- Instantiate `USERNAME_FIELD` for `email` and `REQUIRED_FIELDS` as a list including `name`
- Create functions `get_full_name`, `get_short_name` and `__str__`

#### Create user model manager

1. Create class `UserProfileManager(BaseUserManager)` in `models.py`
2. Create function `create_user` ([cmd 11](#commands))

- Input `email`, `name` and `password` with default `None`
- Raise error if `email` is not provided
- Normalize the email
- Instantiate model `user` using the provided inputs `email` and `name`
- Set password for the `user`
- Save the user into `self._db`
- Return the created `user`

3. Create function `create_superuser` ([cmd 11](#commands))

- Input `email`, `name` and `password`
- Run `create_user` and instantiate the return object as `user`
- Set `is_superuser` and `is_staff` to `True`
- Save the user into `self._db`
- Return the created `user`

4. Set `AUTH_USER_MODEL` to `profiles_api.UserProfile` in `profiles_project/settings.py`

#### Create migrations and sync DB

1. Make migrations for `profiles_api` ([cmd 12](#commands))
2. Migrate the migrations ([cmd 13](#commands))

### Setup Django admin

1. Register the `models.UserProfile` in `profiles_api/admin.py` ([cmd 14](#commands))
2. Create superuser ([cmd 15](#commands))

### Introduction to API Views

#### Hello World API View

1. Create class `HelloApiView(APIView)` ([cmd 16](#commands))

- Create function `get` with `request` input
- Create a list `an_apiview` of text messages
- Return `Response` intaking a dict with keys `message` and `an_apiview`

2. Create `urls.py` in `profiles_api`
3. Include `profiles_api.urls` as `api/` in `profiles_project/urls.py`
4. Add `HelloApiView` as `hello-view/` in `profiles_api/urls.py`
5. Check the response by navigating to `/api/hello-view/`

#### Serializer

1. Create `serializers.py` in `profiles_api`
2. Create class `HelloSerialzer(serializers.Serializer)`

- `name`: `CharField` with `max_length=10`

3. Instantiate `serializer_class` as `HelloSerializer` in `HelloApiView`

#### POST Request

1. Create function `post` in `HelloApiView` ([cmd 17](#commands))

- Instantiate `serializer` using `serializer_class` intaking `data=request.data`
- If `serializer` is valid
  - Get `name` from the validated data
  - Create message "Hello <name>"
  - Return `Response` intaking a dict with key `message`
- If `serializer` is not valid
  - Return `Response` intaking `serializer.errors` with `status=status.HTTP_400_BAD_REQUEST`

#### PUT, PATCH and DELETE Requests

1. Create functions `put`, `patch` and `delete` which only return `RESPONSE({'method': '<method>'})`
2. Check to see the options are now available on the page

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
10.

```python
class UserProfile(AbstractBaseUser, PermissionsMixin):
  email = models.EmailField(max_length=255, unique=True)
  name = models.CharField(max_length=255)
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)

  objects = UserProfileManager()

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['name']

  def get_full_name(self):
      """Retrieve full name of user"""
      return self.name

  def get_short_name(self):
      """Retrieve shot name of user"""
      return self.name

  def __str__(self):
      """Return string representation of our user"""
      return self.email
```

11.

```python
class UserProfileManager(BaseUserManager):
  """Manager for user profiles"""

  def create_user(self, email, name, password=None):
    """Create a new user profile"""
    if not email:
      raise ValueError('Users must have an email address')
    email = self.normalize_email(email)
    user = self.model(email=email, name=name)
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_superuser(self, email, name, password):
    """Create and save a new superuser with given details"""
    user = self.create_user(email, name, password)
    user.is_superuser = True
    user.is_staff = True
    user.save(using=self._db)
    return user
```

12. `python manage.py makemigrations profiles_api`
13. `python manage.py migrate`
14. `admin.site.register(models.UserProfile)`
15. `python manage.py createsuperuser`
16.

```python
class HelloApiView(APIView):
  def get(self, request, format=None):
    an_apiview= [
      "message 1",
      "message 2",
      "message 3",
      "message 4",
    ]

    return Response({
      'message': 'Hello world',
      'an_apiview': an_apiview,
    })
```

17.

```python
def post(self, request):
  serializer = self.serializer_class(data=request.data)

  if serializer.is_valid():
    name = serializer.validated_data.get('name')
    message = f'Hello {name}'
    return Response({'message': message})
  else:
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```
