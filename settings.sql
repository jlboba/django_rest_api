CREATE DATABASE django_contacts;
CREATE USER djangouser WITH PASSWORD 'django';
GRANT ALL PRIVILEGES ON DATABASE django_contacts TO djangouser;
