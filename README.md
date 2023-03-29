
# Agri Sense

A tech-based solution that provides farmers with insights and data to make informed decisions about their crops.


## Documentation

[Documentation](https://linktodocumentation)

dw
## API Reference

### Get all user deatils(superuser)
```http
GET http://localhost:8000/api/users/ HTTP/1.1
Content-Type: application/json
Authorization: Token <token>>
6d	
```

### Change details of current authenticated user
```http
PUT http://localhost:8000/api/user/update/ HTTP/1.1
Content-Type: application/json
Authorization: Token <token>>

{
    "email": "user@email.com",
    "first_name": "First Name",
    "last_name": "Last Name"
}
```

### Register user qith email, password, first and last names
```http
POST http://localhost:8000/api/auth/register/ HTTP/1.1
content-type: application/json

{
    "email": "user@email.com",
    "password": "biddweuiuaUI",
    "first_name": "First Name",
    "last_name": "Last Name"
}
```
### Login user with email and password
```http
POST http://localhost:8000/api/auth/login/ HTTP/1.1
content-type: application/json

{
    "email": "user@email.com",
    "password": "biddweuiuaUI"
}
```
### Change password for authenticated user
```http
POST http://localhost:8000/api/auth/user/change-password/ HTTP/1.1
content-type: application/json
Authorization: Token <token>f

{    
    "old_password": "biddweuiuaUI",
    "new_password": "biddweuiuaUI123"
}
```
### Get user details by ID(superuser)
```http
GET http://localhost:8000/api/user/3/ HTTP/1.1
content-type: application/json
Authorization: Token <token>d
```

### Log out authenticated user
```http
POST http://localhost:8000/api/auth/logout/ HTTP/1.1
content-type: application/json

{"token"<token>}
```
### Get current user details
```http
GET http://localhost:8000/api/user/ HTTP/1.1
Content-Type: application/json
Authorization: Token <token>	
```
### Get all user deatils(superuser)
```http
GET http://localhost:8000/api/users/ HTTP/1.1
Content-Type: application/json
Authorization: Token <token>	
```
### Change details of current authenticated user
```http
PUT http://localhost:8000/api/user/update/ HTTP/1.1
Content-Type: application/json
Authorization: Token <token>f

{
    "email": "user@email.com",
    "first_name": "First Name",
    "last_name": "Last Name"
}
```
