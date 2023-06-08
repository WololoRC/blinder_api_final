# blinder API final
REST API for Blinder project.

Instructions for development and testing purposes.

On the virtualization that are you using install
```django```,```djangorestframework```,```requests```

Then:
```
./manage.py migrate
./manage.py runserver
```

## DOCUMENTATION:

`api/tags/`<br>
METHODS: `GET`<br>
List all Tags

***
`api/signup/`<br>
METHODS: `POST`.<br>

Create a user and retrive a token authentication.<br>

A .json body with fields 'username'
and 'password' is required.
***
`'api/login/'`<br>
METHODS: `POST`.<br>

Get User credentials and return a authenticatio token and users id
if User is authenticated.

A .json body with fields 'username' and 'password'
is 'required'.
***
`api/profile/`<br>
METHODS: `POST`.<br>
An Authorization header with user's token is required.
e.g: 'Authorization: Token <token>'.

`POST`:<br>
Create a Profile for User.

A .json body with fields: 'user_id', 'description' and 'birth_age'
is required.

birth_age must have this format '1997-2-4'.

Returns users Profile
