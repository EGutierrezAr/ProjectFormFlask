python -m pip install flask
python -m pip install flask_sqlalchemy
python -m pip install flask_migrate
python -m pip install psycopg2
python -m pip install flask_wtf

pip3 install -r requirements.txt

.\venv\Scripts\activate // De ser necesario para cambiar de venv

flask db init// Crear nuestra caperta de migrate

flask db migrate //

flask db upgrade //para que se guarden los cambios en la DB

Si llegamos hacer una modificacion:

-flask db stamp head//Para verificar que todo este actualizado al momento
-flask db migrate
-flask db upgrade

//RUN
(env) PS C:\Software\Udemy\PythonFlask\flask-datta-able> $env:FLASK_APP="app.py"
(env) PS C:\Software\Udemy\PythonFlask\flask-datta-able> $env:FLASK_ENV="development"
(env) PS C:\Software\Udemy\PythonFlask\flask-datta-able> flask run