my_venv/Scripts/activate
# Add PostgreSQL binaries to the system PATH
#echo 'export PATH=$PATH:/usr/pgsql-13/bin' >> ~/.bashrc
#source ~/.bashrc
pip install -r requirements.txt 
python manage.py collectstatic

