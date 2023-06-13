# blinder API final
REST API for Blinder project.

Instructions for development and testing purposes.

On the virtualization that you are using install
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

`birth_date`: birth date of User, when you create
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

Create an authenticated User instance with Profile Instance.<br>
Also creates a BlockedUsers table for User. <br>

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

List all Tags instaces.

### Returns: <br>
All Tags instaces.<br>

***

### `profile/blocked_list/<uuid:profile_id>/` <br>
### METHOD: `GET`. <br>

Get data from User BlockedUsers table.

### Returns: <br>
A dict of blocked users with key's value's {<user.name>: <user.id>}
from BlockedUsers table.
***

### `profile/blocked_list/update/<uuid:profile_id>/` <br>
### METHODS: `PUT`, `DELETE`.

METHODS: `PUT`, `DELETE`

A payload called `id_list` with a list of valid UUID's
is required. <br>

Returns: <br>
A dict of blocked users on success,
a error message if 'profile_id' or 'id_list' have
invalid data. <br>

`PUT`: <br>
Add Users to BlockedUsers main User table. <br>

`DELETE`: <br>
Remove Users of BlockedUsers main User Table. <br>

