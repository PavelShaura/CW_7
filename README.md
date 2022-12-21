# TODOLIST PROJECT

Powered by Django Rest framework, Postgres, docker-compose and OAuth with social-auth.
 
## The functionality of the program:

> ### ***The graphical user interface for working with goals is a board, where each goal is a card on this board.***
> **Addresses:**

> http://coder.pp.ru/auth
> 
> admin: http://coder.pp.ru/admin/
> 
<img width="929" alt="auth" src="https://user-images.githubusercontent.com/104260807/208913976-63d81b76-548d-4987-89ec-7281bbbc0e8b.png">


## **Telegram bot:**

 You can link a Telegram account to an application account and get or create all the user's goals.
 
 > Bot telegram https://t.me/app_todo_bot
 
## **Board:**

The board is divided into 3 columns by status.

**1. To fulfill — goals that the user simply adds up, but does not proceed to them (some kind of "backlog").**

**2. In work — the goals that the user is currently trying to achieve.**

**3. Completed — goals that have been achieved.**

So that the achieved goals do not score the whole board,
it is possible to assign them a special status "In the archive". 
Then they will not be displayed on the board, but you can return to them using the Archive page.

On each card you can see:

The name of the goal.
Priority:
low,
medium,
high,
critical.
Deadline date — if the deadline date is greater than the current date, the card should be displayed as overdue.
Category — combining goals according to a convenient criterion, for example, the categories "Personal", "Work", "Health", "Finance".

**Sorting, filtering and search functions:**


By default, the cards in each column are sorted by priority (in order of importance) and deadline date.
It should be possible to sort cards by deadline date without taking into account priority.
Filtering:

Cards can be filtered by category/categories.
Cards can be filtered by priority/priorities.
Cards can be filtered by the deadline date.
Search:

You can search by entering the text in the name of the card.

## **Working with a goal**
<img width="941" alt="todo" src="https://user-images.githubusercontent.com/104260807/208902732-b8f8ebb8-9815-45fe-ab7d-72c6cd5b752c.png">

Clicking on the card opens the detailed view of the goal screen. On it , the user can:

See detailed information about the goal.
Title.
Description.
Category.
Status.
Priority.
The deadline date.
Date of creation.
The date of the last update.

Edit the goal:

Title.
Description.
Category.
Status.
Priority.
The deadline date.

When editing a goal, the update date should change.

Archive the target.
Give her the status "In the archive", and then she will leave the board.

Work with comments:

Comments are needed to add notes, links, files, photos, and anything on the topic to the goal.

<img width="916" alt="comments" src="https://user-images.githubusercontent.com/104260807/208911844-9c700208-34fb-401d-b025-ec58c519fba2.png">

Create comments.
Edit comments.
Delete comments.
View the list of comments:
Sort by creation date in descending order (the most recent ones are at the top).
Display:
The text of the comment.
The date the comment was created.
The date the comment was updated (if it does not match the creation date).

## **Interface for categories**

There is a separate interface for working with categories:

1. Creating a category.

2. Editing a category.

3. View the list of categories.

4. Deleting a category.




## How to launch project in development environment:

**1. Create virtual environment**

**2. Install dependencies from requirements.txt**

> pip install -r todolist/requirements.dev.txt
> 
**3. Set environment variables in .env file**

> create .env file in todolist folder
> 
**you can copy the default variables from todolist/.env.example**

**4. Launch database from deploy folder**

> cd deploy
> 
>docker compose --env-file ../todolist/.env -f docker-compose.db.yaml up -d
> 
**5. Make migrations from todolist folder**

> cd todolist
> 
>./manage.py makemigraitons
> 
>./manage.py migrate
> 
**6. Launch project**
> 
> ./manage.py runserver
> 
## Accessing admin site

**1. Create admin-user**

> ./manage.py createsuperuser
> 
set values and required fields

**2. Access admin site at http://127.0.0.1:8000/admin/**

## How to launch project in development with Docker-compose

**1. Create .docker_env file in deploy folder:**

***you can copy the default variables from todolist/.env.example
make sure to set DB_HOST to db which is a container name***

**2. Use docker-compose.dev.yaml from within deploy folder**

> cd deploy
> 
>docker compose --env-file .docker_env -f docker-compose.dev.yaml up -d
>

**3. The following would be done:**

***postgresql container would start
migrations would apply
api container would start
front container would start***

## Deploy

**1. Deploy is automated with github actions.**

**2. Project files used:**

***actions: .github/workflows/actions.yaml
compose file: deploy/docker-compose.ci.yaml
env variables: deploy/.ci_env
variables in compose and env files are replaced with github secrets***

**3. Docker hub images:**

> ***front: sermalenk/skypro-front:lesson-38***

> ***back: pshaura/todolist_project:***

**4. To add admin during first launch:**

***connect to server and access project folder***

> docker exec -it <api container_id> /bin/bash
> 
> ./manage.py createsuperuser
> 

