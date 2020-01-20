#! /bin/sh


# Restart ngnix
sudo service nginx restart

# Restart postgresql
sudo service postgresql start

# Restart postgresql
sudo service postgresql start



sudo -u postgres psql -c "SELECT version();"


#CREATE DB

sudo -u postgres psql -c "CREATE USER root WITH ENCRYPTED PASSWORD 'root';"
#sudo -u postgres psql -c "CREATE USER postgres WITH ENCRYPTED PASSWORD 'postgres';"
sudo -u postgres psql -c "ALTER USER postgres with password 'postgres'"
sudo -u postgres psql -c "CREATE DATABASE pathogendb;"
sudo -u postgres psql -c "ALTER ROLE postgres SET client_encoding TO 'utf8';"
sudo -u postgres psql -c "ALTER ROLE postgres SET default_transaction_isolation TO 'read committed';"
sudo -u postgres psql -c "ALTER ROLE postgres SET timezone TO 'UTC';"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE pathogendb TO postgres;"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE pathogendb TO root;"


# Initiate and migrate db
echo "Create table by Flask"
flask create_tables
sudo -u postgres psql -c "\connect pathogendb;"

echo "InitDB"
python wsgi.py db init
echo "MigrateDB"
python wsgi.py db migrate
sudo -u postgres psql -c "\connect pathogendb;"

echo "Upgrade db"
python wsgi.py db upgrade


# Load demo data
echo "Load some data as demo"
sudo -u postgres psql -c "\connect pathogendb;"
sudo -u postgres psql -d pathogendb -c "\COPY pathogens FROM '/najlabioinfo/pathogenMemoPackage/demodata/pathogenlistH.csv' WITH (FORMAT csv);"
#sudo -u postgres psql -d pathogendb -c  "SELECT * FROM pathogens;"


#Run Flask app (dev)
flask run --host=0.0.0.0 --port=5000

#Run Flask app (prod)
#uwsgi --socket 0.0.0.0:8080 --protocol=http -w wsgi:app
