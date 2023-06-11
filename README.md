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

# Models

## Profiles

### Atributes:

`user`: `User.id` related instance.<br>

`description`: Description of profile, is a `string` value.<br>

`owner_tags`: Instances of `Tags` related to User Profile.<br>

`birth_age`: birth age of User, when you create
a new instance of Profile insert data
as follows: (%Y/%m/%d).<br>

`id`: UUID related to Profile instance.

## Tags

### Atributes:

`tag_name`: Name of a Tags instance, is a string value.<br>
`id`: UUID related to Tags instance.

# Documentation.

## Profile managment:

### Routs:

### `/api/signup/`<br>
### METHOD: `POST`.<br>

Create an authenticated User instance  with Profile Instance.<br>

A payload on request body with fields 'username', 'password' and 'birth_date' is required.<br>

### Return:<br>
If Users's username does not exist return a new Profile instance data with
Authentication Token, else a error message.<br>
***

### `/api/login/`<br>
### METHOD: `POST`.<br>

Get User Authentication.

### Returns:<br>
User's Profile Authentication Token,  username and id on success.
Else a error message if fails.<br>
***

### `/profile/<uuid:profile_id>/`<br>
### METHODS: `GET`, `PUT`.

`PUT`:<br>
Update Profile tags and description, send a payload on body
request with fields:<br>

`remove_tags: <Tag's UUID's'>` delete tags. <br>

`add_tags: <Tag's UUID's>` add tags. <br>

`description: <str>`. change description. <br>

### Returns: <br>
On success a updated Profile instance data, else an error message. <br>

`GET`:<br>

Get a Profile instance on detail.<br>

### Returns: <br>
User's Profile data on success, else a error message.<br>
***

### `/api/profile/delete/<uuid:profile_id>/` <br>
### METHOD: `DELETE`. <br>

Delete a Profile instance. <br>

### Returns: <br>
On success return a http 204 status or a error message if fails. <br>
***

### `/api/tags/` <br>
### METHOD: `GET`. <br>

List al Tags instaces.

### Returns: <br>
All Tags instaces.<br>






