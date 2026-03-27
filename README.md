# 📚 My Library — Django CRUD App

A personal book library web app with user authentication. Built with Django.

## Features
- Register / Login / Logout
- Add, Edit, Delete books (your own only)
- Genre tags & read/unread status
- Deployable on Render

---

## Local Setup

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run migrations
```bash
python manage.py migrate
```

### 5. Create a superuser (optional, for admin panel)
```bash
python manage.py createsuperuser
```

### 6. Start the server
```bash
python manage.py runserver
```

Visit: http://127.0.0.1:8000

---

## Deploy to Render

### 1. Push to GitHub
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

### 2. Create a Web Service on Render
- Go to https://render.com and sign up
- Click **New > Web Service**
- Connect your GitHub repo

### 3. Configure the service
| Setting | Value |
|---|---|
| Environment | Python 3 |
| Build Command | `./build.sh` |
| Start Command | `gunicorn library_project.wsgi --log-file -` |

### 4. Add Environment Variables
In Render dashboard → Environment:
| Key | Value |
|---|---|
| `SECRET_KEY` | (generate a random long string) |
| `DEBUG` | `False` |
| `PYTHON_VERSION` | `3.11.0` |

### 5. Deploy!
Click **Create Web Service** — Render will build and deploy automatically.

---

## Project Structure
```
library_project/
├── library_project/       # Django project config
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── books/                 # Main app
│   ├── models.py          # Book model
│   ├── views.py           # CRUD views
│   ├── forms.py           # Book & Register forms
│   ├── urls.py            # Book URLs
│   ├── urls_auth.py       # Register URL
│   └── templates/
│       ├── books/         # Book templates
│       └── registration/  # Auth templates
├── requirements.txt
├── Procfile
├── build.sh
└── manage.py
```
