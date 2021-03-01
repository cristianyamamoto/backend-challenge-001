# Jungle Devs - Backend Challenge #001

## Description
**Challenge goal**: The idea of the challenge is to implement a very simplified version of [Reddit](https://www.reddit.com), 
meaning you will have *Users*, *Topics*, *Posts* and *Comments*. with this you're expected to test your knowledge on 
the basic concepts involved in a Django backend application, and to also learn even more.
Always!

**Target level**: This is an entry level course, no prior knowledge of programming is needed.
 
**Final accomplishment**: By the end of this challenge, you’ll be able to understand the basics of Django and how to create your own RESTful API with basic CRUD functionalities.

## Acceptance criteria
- Separate your project into 4 Django apps, one for each entity:
  - User
  - Topic
  - Post
  - Comment
- Have all the required fields for each entity as described on this README
- Use the URL structure described on this README with Nested URL Routers

## Prerequisites

- [Python 3.7](https://www.python.org)
- [Docker](https://www.docker.com)
- [Docker Compose](https://docs.docker.com/compose/)
- [Virtualenv](https://github.com/pypa/virtualenv/)
- [Git](https://git-scm.com/)

## Instructions to Run

- Create the virtual environment and activate it

        virtualenv -p python3 venv
        source venv/bin/activate
- Install the requirements `pip install -r requirements.txt`
- Start the dockers `docker-compose up` with the database and the localstack
- Run the server with `python manage.py runserver 8000`

You need a `.env`file with your environment variables, here's an example file:
```
LOAD_ENVS_FROM_FILE='True'
ENVIRONMENT='development'
SECRET_KEY='#*=backend-challenge=*#'
DEFAULT_FROM_EMAIL='Challenge <challenge@jungledevs.com>'
DATABASE_URL='postgres://postgres:postgres@localhost:5432/boilerplate'
SENTRY_DSN='sentry_key'
AWS_STORAGE_BUCKET_NAME='django-be'
```

## Additional Information
Here are some useful stuff to keep in mind while completing this challenge:

* Try to keep your code [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself), so the creation of 
[abstract helper](https://realpython.com/modeling-polymorphism-django-python/#abstract-base-model) [models](https://docs.djangoproject.com/en/3.0/topics/db/models/#abstract-base-classes) is more than welcome 
to avoid repetition of fields in your models
* Remember that only the author of a topic, post or comment should be able to modify or delete it!
If you have any doubts, check the 
[Authentication and Permissions part](https://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/) 
on the Django REST tutorial
* For better structuring and visualization, you may use 
[Nested Serializers](https://www.django-rest-framework.org/api-guide/relations/#nested-relationships) to customize your 
responses beyond the primary keys

### Entities

As mentioned in the description, this challenge will have four entities (each one should be a separate app). 
Here are brief descriptions of what they are and what are the expected properties of each (keep in mind that you can 
improve them as you wish!):

* *User*: can be used plain from what is offered by Django;
* *Topic*: the equivalent of a sub-reddit. The suggest fields are:
    * Name
    * Title
    * Author
    * Description
    * URLName - the name we want to use to reach it through the browser (check [SlugField](https://docs.djangoproject.com/en/2.1/ref/models/fields/#slugfield))
    * Created_at
    * Updated_at
* *Post*: the equivalent of a *Reddit thread*, a *post* belongs to a *specific topic* and is *created by an user*. The 
suggested fields are:
    * Title
    * Content
    * Created_at
    * Updated_at
    * Topic
* *Comment*: the equivalent of a comment, a comment belongs to a *specific post* (which belongs to a *specific topic*) 
and is *created by an user*. The suggested fields are:
    * Title
    * Content
    * Created_at
    * Updated_at
    * Post
    
### URLs    

We want to have a behavior similar to *Reddit (not necessarily equal)*, so ideally we'd like a structure like this:

* */topics/* - lists all available topics
* */topics/{urlname}/* - details (as well as some posts) from a specific topic (identified by *urlname*)
* */topics/{urlname}/posts/* - lists all posts from a specific topic
* */topics/{urlname}/posts/{post_id}/* - lists details and some comments from a post
* */topics/{urlname}/posts/{post_id}/comments/* - lists all comments from a post
* */topics/{urlname}/posts/{post_id}/comments/{comment_id}/* - lists details from a comment


If you have any doubts on how to implement these structures, check the
[Nested Routers documentation](https://github.com/alanjds/drf-nested-routers) and the 
[lookup field section on the Routers documentation](https://www.django-rest-framework.org/api-guide/routers/#simplerouter).

## Postman Tests

In order to test the application functionalities we can use Postman.

### POST method

To test a POST method that creates topics, posts and comments, it was created an authorization token for permission purposes.
On the body tab, we write a raw JSON text to pass the desired information for each entity. Below follow some examples.

Creating a Topic Example (endpoint: `/topics/`):
```
{
 "title": "Topico 1",
 "name": "Topico 1",
 "description": "Descrição do Topico 1",
 "url_name": "topico1"
}
```

Creating a Post Example (endpoint: `/topics/topico1/posts/`):
```
{
 "title": "Post 1 do topico 1",
 "content": "Conteúdo do post 1 do Topico 1"
}
```

Creating a Comment Example (endpoint: `/topics/topico1/posts/1/comments/`):
```
{
 "title": "Comment 1 do Post 1 do topico 1",
 "content": "Conteúdo do comment 1 do post 1 do Topico 1"
}
```

### GET method

After creating topics, posts and comments, we can use the GET method to retrieve the information of each one.

* Here follow some examples of endpoints that respect the URLs behavior said previously:
    * /topics - Retrieves all Topics
    * /topics/topico1 - Retrieves details of a Topic
    * /topics/topico1/posts - Retrieves Posts of a Topic
    * /topics/topico1/posts/1 - Retrieves details of a Post
    * /topics/topico1/posts/1/comments - Retrieves Comments of a Post
    * /topics/topico1/posts/1/comments/1 - Retrieves details of a Comment
	
### PATCH and DELETE method

Also, we can test if only the author of a topic, post or comment can modify or delete it.
For example, if we use the endpoint `/topics/topico1/posts/1/comments/1/`, we can modify or delete the comment if the authorization token belongs to the author.

