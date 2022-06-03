# Medical Database 
This project was developed as a final work for “Database” course during my second year in uni. It serves as an example of a simple database and analytics website system for a
medical facility. 

Running
-------
Creating database template

    python manage.py migrate
    
Seeding database with faker data

    python manage.py filldb [--filldb={small, large, medium}] 

Running the website

    python manage.py runserver

Address
-------
  http://127.0.0.1:8000/

