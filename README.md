# jwt_sample_project

## Git 
```
In your terminal

git clone https://github.com/Peiyu-212/jwt_sample_project.git

docker-compose up --build -d
docker-compose exec app bash
python manage.py migrate
```


## API
### First step: register account
**POST** /api/users/register
User need to register account to have authority.
```
[POST] [This link](http://localhost:8002/api/users/register)

[body] 
{'username': 'rrrrr', 
 'password': 'tttt',
 'first_name': 'rrrrr',
 'last_name': 'hhhh'}

[message]
{
    "user": {
        "id": 2,
        "password": "pbkdf2_sha256$260000$6K2UVVFhNXdZMk9c4hdFA4$6geZoFK97JAo9BecTEC4hiMb81pTWBp/hueO5BKrWYc=",
        "last_login": null,
        "is_superuser": false,
        "username": "rrrrr",
        "first_name": "rrrr",
        "last_name": "hhhh",
        "email": "",
        "is_staff": false,
        "is_active": true,
        "date_joined": "2023-07-11T09:30:38.437355Z",
        "groups": [],
        "user_permissions": []
    },
    "message": "User created successfully! Please try to login again."
}
```

### Second step: get jwt token
User login with username and password to get jwt token 

**POST** /api/token/

```
[POST]  [This link](http://localhost:8002/api/token/)

[body] 
{'username': 'rrrr', 
 'password': 'tttt'}

[message]
{'access': token, 'refresh': token}
```

### Create article api
**POST** /api/article/new_post/

```
[POST]  [This link](http://localhost:8002/api/article/new_post/)

[body]
{'title': 'test_post3',
 'content': 'this is a test post and need to upload multiple image',
 'uploaded_images': [image list]}
{'Authorization': 'Bearer jwt token'}

[message]
{'title': 'test_post3',
 'content': 'this is a test post and need to upload multiple image',
 'images': [{'image': file_path, 'description': null}]}
```

### Delete article api
**DELETE** /api/article/{id}/

```
[Delete] [This link](http://localhost:8002/api/article/2/)

[body]
{'Authorization': 'Bearer jwt token'}

[message]
{'status': '204 No Content'}
```

### Update article api
**PATCH** /api/article/{id}/

```
[PATCH] [This link](http://localhost:8002/api/article/3/)


[body]
{'title': 'test_post3',
 'content': 'this is a test post and need to upload multiple image',
 'uploaded_images': [image list]}
{'Authorization': 'Bearer jwt token'}

[message]
{'title': 'test_post3',
 'content': 'this is a test post and need to upload multiple image',
 'images': [{'image': file_path, 'description': null}]}
```

### List article api
**GET** /api/article/

```
[GET] [This link](http://localhost:8002/api/article/)

[body]
{'Authorization': 'Bearer jwt token'}

[message]
{
  "count": 2,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 3,
      "title": "test_post_update_now",
      "content": "this is a test post to update content and reload image",
      "last_modified": "2023-07-11T08:14:08.543865Z",
      "images": [
        {
          "id": 2,
          "image": "files/istockphoto-1322277517-612x612.jpg",
          "description": null,
          "article": 3
        }
      ]
    },
    {
      "id": 4,
      "title": "test_post3",
      "content": "this is a test post and need to upload multiple image",
      "last_modified": "2023-07-11T07:46:48.638506Z",
      "images": [
        {
          "id": 1,
          "image": "files/May20.jpg",
          "description": null,
          "article": 4
        }
      ]
    }
  ]
}
```
