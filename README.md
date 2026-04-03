# Django Projects

This folder contains two Django projects for EECE430 coursework.

## Setup

1. Create the virtual environment (if not already created):
```powershell
cd ..
python -m venv venv
cd djangoProjects
```

2. Activate the virtual environment:
```powershell
.\venv\Scripts\Activate.ps1
```

3. Install dependencies:
```powershell
pip install -r requirements.txt
```

## Running the Projects

### voleyPlayerList (CRUD Project)
```powershell
cd voleyPlayerList
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```
Open browser: `http://localhost:8000/`

### originalVolleySite (Tutorial Project)
```powershell
cd originalVolleySite
python manage.py migrate
python manage.py runserver 0.0.0.0:8001
```
Open browser: `http://localhost:8001/testapp/`

## Admin Panel

For either project, create a superuser:
```powershell
python manage.py createsuperuser
```
Then visit: `http://localhost:8000/admin` (or port 8001)
