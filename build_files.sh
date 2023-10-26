source my_venv/Scripts/activate
sudo apt update
sudo apt install postgresql postgresql-contrib
sudo systemctl start postgresql.service
# Add PostgreSQL binaries to the system PATH
#echo 'export PATH=$PATH:/usr/pgsql-13/bin' >> ~/.bashrc
#source ~/.bashrc
pip install -r requirements.txt 
python manage.py collectstatic

