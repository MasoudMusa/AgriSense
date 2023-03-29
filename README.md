
# Agri Sense

A tech-based solution that provides farmers with insights and data to make informed decisions about their crops.


## Documentation

[Documentation](https://linktodocumentation)

dw
## API Reference

### Get all user deatils(superuser)
```http
GET /api/users/ HTTP/1.1
Content-Type: application/json
Authorization: Token <token>>
```

### Change details of current authenticated user
```http
PUT /api/user/update/ HTTP/1.1
Content-Type: application/json
Authorization: Token <token>>

{
    "email": "user@email.com",
    "first_name": "First Name",
    "last_name": "Last Name"
}
```

### Register user qith email,pasuser@email.comme
```http
POST /api/auth/register/ HTTP/1.1
content-type: application/json

{
    "email": "user@email.com",
    "password": "biddweuiuaUI",
    "first_name": "First Name",
    "last_name": "Last Name"
}
```
### Login user with email,pasuser@email.comrd
```http
POST /api/auth/login/ HTTP/1.1
content-type: application/json

{
    "email": "user@email.com",
    "password": "biddweuiuaUI"
}
```
### Change password for authenticated user
```http
POST /api/auth/user/change-password/ HTTP/1.1
content-type: application/json
Authorization: Token <token>f

{    
    "old_password": "biddweuiuaUI",
    "new_password": "biddweuiuaUI123"
}
```
### Get user details by ID(superuser)
```http
GET /api/user/3/ HTTP/1.1
content-type: application/json
Authorization: Token <token>d
```

### Log out authenticated user
```http
POST /api/auth/logout/ HTTP/1.1
content-type: application/json

{"token"<token>}
```
### Get current user details
```http
GET /api/user/ HTTP/1.1
Content-Type: application/json
Authorization: Token <token>	
```
### Get all user deatils(superuser)
```http
GET /api/users/ HTTP/1.1
Content-Type: application/json
Authorization: Token <token>	
```
### Change details of current authenticated user
```http
PUT /api/user/update/ HTTP/1.1
Content-Type: application/json
Authorization: Token <token>f

{
    "email": "user@email.com",
    "first_name": "First Name",
    "last_name": "Last Name"
}
```
# Hi, I'm Mwenda! 👋


## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://katherineoelsner.com/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mwenda-mwabehah-856542261/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/)

