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

A model for User's Profiles, is created on User registration. <br>

### Atributes:

`user`: `User.id` related instance.<br>

`description`: Description of profile, is a `string` value.<br>

`owner_tags`: Instances of `Tags` related to User Profile.<br>

`birth_date`: birth date of User, when you create
a new instance of Profile insert data
as follows: (%Y/%m/%d).<br>

`id`: UUID related to Profile instance.

## Tags

A Tags model, holds descriptive data about User,

### Atributes:

`tag_name`: Name of a Tags instance, is a string value.<br>
`id`: UUID related to Tags instance.

## BlockedUsers

A BlockedUsers model, keeps record of blocked users for a main User, this models is referenced
when a User registrates. <br>

### Atributes:

`owner`: User Profile of main User. <br>
`blocked_list`: A list of Profile instances who the main User dont wants to see. <br>

## LikeUsers

A model for store liked users records, this model is references to a Profile when a User
registrates.

### Atributes:

`owner`: User Profile of main User. <br>
`like_list`: A list of Profile instances who the main User like. <br>

## Chat

A Chat model for record conversations within two users. <br>
This model is created when two users makes a match. <br>

### Atributes:

`user_one`: Some User.
`user_two`: Another User.
`messages`: A list with Message instances.
`id`: a UUID.

## Message

A model to record messages witihn two users, goes inside Chat table. <br>

### Atributes:

`sender`: Who sends the message.
`reciever`: Who recieves the message.
`created_at`: Time for creation.

# Documentation.

# Profile managment:

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
# Block Users Functionality.

### `api/profile/blocked_list/<uuid:profile_id>/` <br>
### METHOD: `GET`. <br>

Get data from User BlockedUsers table.

### Returns: <br>
A dict of blocked users with key's value's {<user.name>: <user.id>}
from BlockedUsers table.
***

### `api/profile/blocked_list/update/<uuid:profile_id>/` <br>
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

***
# Messages Functionality

### `api/chat/<uuid:chat_id>/` <br>
### METHODS: `PUT`, `DELETE`.

`GET`: <br>
Get a Chat instance by his 'chat_id'. <br>

Returns: <br>
A Chat instance on success, a error message if fails. <br>

`DELETE`: <br>
Deletes a Chat instance by his 'chat_id'. <br>

Returns: <br>
A success nessage on successm, a error message if fails. <br>

***
### `api/chat/messages/<uuid:chat_id>/`
### METHOD: `PUT`.

Put a new message in a Chat instance. <br>

A 'chat_id' and a payload with these fiels is required: <br>
'sender': A profile UUID who sends the message. <br>
'reciever': A profile UUID who recieve the message. <br>
'msg_content': A string with the content of message. <br>

Returns: <br>
A updated Chat instance on success,
a ugly error message if fails. <br>

***
### `api/chat/inbox/<uuid:profile_id>/`
### METHOD: `GET`

Get al Chat instance related to a Profile. <br>

A valid 'profile_id' on url is required. <br>

Return: <br>
All chat instances of User, as 'user_one'
or 'user_two'. <br>
***
# Match Making

### `api/profile/like_list/update/<uuid:profile_id>/`
### METHOD: `PUT`.

Add users profiles or make a match. <br>

A payload with keys 'like_id' with a valid
profiles id is required. <br>

Returns: <br>
If like_list from liked Profile have record of the
main User a Chat instance is created, else only saves
the liked Profile on the like_list of main User. <br>

if profile_id or like_id are not valid returns a error
message. <br>

***
### `api/profile/like_list/<uuid:profile_id>`
### METHOD: `GET`

Get LikeUsers list from Profile <br>

Returns:
On success returns Profile like_list, else
return a ugly error message. <br>

***
### `api/profile/random_feed/<uuid:profile_id>/`
### METHOD: 'GET'

Get feed <br>

Get a random Profile list for populate the feed. <br>

Returns:
On success all Profile excluding the Profiles inside of
LikeUsers and BlockedUsers, else a error message. <br>
***
### `api/profile/feed/<uuid:profile_id>/`
### METHOD: 'GET'

Get a Profile list for populate the feed. <br>

Returns: <br>
On success all Profile by exception of block and likes,
thath match almost once with the 'owner_tags' of the main user.
Else a error message. <br>

