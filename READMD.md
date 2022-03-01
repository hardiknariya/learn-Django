====================== For create custom user model ========================

1. create new app
2. in app models.py import AbstractUser, PermissionsMixin, and BaseUserManager
3. create custom user model
4. create custom user model manager
5. add app in setting "INSTALLED_APP" 
6. add new Field AUTH_USER_MODEL = "your_app_name.your_custom_user_model_name"
7. check  all places to  import user model as get_user_model
8. delete all migrations and database
9. run makemigratios and migrate
10. enjoy your codding :)

---------------------------------------------------------------------------------
