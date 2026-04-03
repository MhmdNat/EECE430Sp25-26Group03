# voleyPlayerList

EECE430 Django CRUD project for managing volleyball players.

## Setup

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Run Locally

```powershell
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

Open: http://localhost:8000/

## Docker Image (GitHub Packages)

This repository is the source code. The Docker image is published as a GitHub Package.

- Image: `ghcr.io/mhmdnat/eece430sp25-26group03:latest`
- Package page: https://github.com/users/mhmdnat/packages/container/eece430sp25-26group03

Pull and run from GitHub:

```powershell
docker pull ghcr.io/mhmdnat/eece430sp25-26group03:latest
docker run -d -p 8000:8000 --name voleyplayerlist ghcr.io/mhmdnat/eece430sp25-26group03:latest
```
