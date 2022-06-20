# Task 76: Django Models 

Create a new GitHub repository with a README.md, and Python .gitignore file.  
Clone it to your machine/computer, which will create a new folder on your computer with your repository’s content.  
Create a new virtual environment in that folder named .env and install Django in it.  
Create a new Django project. Use your Zuriboard Student ID as the name of the project.  
Create a new application using the Django startapp command. The app should be called blog.  

Add the blog app to the main_projects INSTALLED_APPS.  

Create a new model in the **blog** app called **Post**. It should have the following fields:

 Post

--------

Title : A string of maxlength 200, use Django’s models.CharField

Text : Any amount of text, use Django’s TextField

Author : A Foreign Key to the current user model. Make use of Django’s get_user_model function.

Created_date : A date-time column, use Django’s models.DateTimeField. 

Published_date : A date-time column, use Django’s models.DateTimeField. 

--------

Create migrations for your new model using the makemigrations Django command.  
Run all migrations using the migrate Django command.  
Stage and Commit your Django project and push your changes to your GitHub repository.  
Ensure your final code/submission is on the default branch of your GitHub repository.  
