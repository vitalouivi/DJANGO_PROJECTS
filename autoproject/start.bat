mkdir %1 
cd %1
pip install virtualenv
virtualenv env
call env\Scripts\activate

pip install django
django-admin startproject %1 .
pip freeze > requirements.txt

cls

echo python manage.py runserver > run.bat
echo python manage.py makemigrations > mkmigr.bat
echo python manage.py migrate > migr.bat
