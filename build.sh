echo "BUILD START"
python3 -m pip install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic --noinput --clear
python3 createsu.py
echo "BUILD END"
