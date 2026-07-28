# BlogShare
 
A multi-user blogging platform built with Django. Users can create accounts, write and publish posts, comment on other user's posts.
 
## Features
 
- User accounts (sign up, log in, log out)
- Create blog posts
- Per-user post authorship (each post is tied to its author)
- Browse and read posts from other users
- Comment on other users' posts
- View a user's post history and comment history
- Debug toolbar enabled for local development
## Tech Stack
 
- **Backend:** Django 5.1.7 (Python)
- **Config:** [python-decouple](https://pypi.org/project/python-decouple/) for environment-based settings
- **Dev tools:** [django-debug-toolbar](https://django-debug-toolbar.readthedocs.io/)
- **Frontend:** HTML templates + static CSS, with npm for front-end dependencies/tooling