# INHS Dashboard
A Django based API that allows users within INHS to view a dashboard with data from the INHS biological collections (INHS-HERP) and view research articles/papers associated with each specimen. Other users can add reviews regarding the research work related to a specimen.

# Data Source
Illinois Natural History Survey - Amphibian and Reptile Collection. Occurrence dataset (ID: 4a086dbb-2b18-4ee9-a6dc-901da56c636a) <br>
https://biocoll.inhs.illinois.edu/portal/content/dwca/INHS-HERP_DwC-A.zip accessed via the INHS Collections Data Portal, biocoll.inhs.illinois.edu/portal, 2025-01-17) <br>
https://biocoll.inhs.illinois.edu/portal/collections/misc/collprofiles.php?collid=46

## Installation
1. Clone the repository:
```bash
 https://github.com/anjaliasha123/Django-Specimen-Collection-API.git
```

2. Docker compose startup (LOCAL DEV):
```bash
 docker compose -f local.yaml up --build
```
REMEMBER: Replace 'production' with 'local' as settings configuration file in the manage.py, wsgi.py & celery.py files. 

3. Docker compose startup (PRODUCTION):
```bash
 docker compose -f production.yaml up --build
```
REMEMBER: Replace 'local' with 'production' as settings configuration file in the manage.py, wsgi.py & celery.py files.

## Technology
<div align="center">
	<code><img width="50" src="https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/github.png" alt="GitHub" title="GitHub"/></code>
	<code><img width="50" src="https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/python.png" alt="Python" title="Python"/></code>
	<code><img width="50" src="https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/django.png" alt="Django" title="Django"/></code>
	<code><img width="50" src="https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/postgresql.png" alt="PostgreSQL" title="PostgreSQL"/></code>
	<code><img width="50" src="https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/nginx.png" alt="Nginx" title="Nginx"/></code>
	<code><img width="50" src="https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/digital_ocean.png" alt="Digital Ocean" title="Digital Ocean"/></code>
  <code><img width="50" src="https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/react.png" alt="React" title="React"/></code>
	<code><img width="50" src="https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/redux.png" alt="Redux" title="Redux"/></code>
</div>

## Funtionality
- Users can register to access the dashboard
- Registered users must verify email. Email verification request is sent via an email
- Anonymous/authenticated users can view all the data from INHS data
- Only authenticated users can update the data, add/like research articles associated with the specimen collection.
- When a user updates the data, a notification is sent via email to the admin.
- Authenticated users can add reviews or comments regarding the research work.

## Architecture
![image](https://github.com/user-attachments/assets/e5fc7423-1d76-441c-a358-be65eebbfc78)

## App features
- CRUD operations
- API documentation using drf-yasg
- Django Admin UI
- Celery workers to send email notification 
- Redis as message broker

## Frontend - Ongoing Devlopment
https://github.com/anjaliasha123/Specimen-Collection-Dashboard

