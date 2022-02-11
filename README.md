# django-calculator

A web app where you can login and calculate basic mathematics in your personal enviroment with history of your previous work.

Link To the Live App (https://django-calculator-app.herokuapp.com/)

🧰 Techs Used

<img src="https://cdn.worldvectorlogo.com/logos/django.svg" alt="Django" width="50" height="50"/>  <img src="https://cdn.worldvectorlogo.com/logos/html5-2.svg" alt="CSS Logo" width="50" height="50"/>  <img src="https://cdn.worldvectorlogo.com/logos/sqlite.svg" alt="SQlite" width="100" height="50"/>   <img src="https://cdn.worldvectorlogo.com/logos/python-5.svg" alt="Python" width="60" height="50"/> <img src="https://cdn.worldvectorlogo.com/logos/javascript-1.svg" alt="js" width="50" height="50"/> <img src="https://cdn.worldvectorlogo.com/logos/jquery-1.svg" alt="js" width="200" height="50"/> <img src="https://cdn.worldvectorlogo.com/logos/gunicorn.svg" alt="js" width="100" height="50"/> 

For Devlopment:

1) Fork the repo to your account
2) Clone it in your system
3) Then install all the requirements using command `pip freeze > requirements.txt`
4) Then run the commands:-
   * `python manage.py makemigrations`
   * `pyhton manage.py migrate`
   Note - These commands are used to create all the necessary schemas in your database and to migrate all the changes in models.
5) To run the app in your local environment run the command :- `python manage.py runserver`
6) Now you can see your local environment running at `localhost:8000`

For Deployement:

1) I have used `Heroku`
2) I served my app using `gunicorn` .

To see the web app in action you can use these credentials :

Username - dell567
Password - Dell@567

Admin Username - aayush
Admin Password -aayush

You can also create your own admin username and password by creating a new superuser and to do so just run this command 
`python manage.py createsuperuser`
