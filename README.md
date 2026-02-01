# Botique

A Django-based boutique/shop web application built with Python.
This project focuses on the backend architecture, providing a robust foundation for an online boutique platform with user accounts, product management, and core website functionality. While the frontend and UI are minimal, the project is designed to showcase strong backend development skills.
[GitHub Repository](https://github.com/sobhan661/Botique)

---

## Features

- **Product boutique website** built with Django  
- **User accounts** with registration & login  
- Modular Django apps (`accounts`, `core`, `website`, etc.)  
- Custom templates for frontend UI  
- Secure authentication powered by Django’s built-in system  
- Easy to extend with products, cart, checkout, and admin tools

---

## Tech Stack

- **Python** (Django framework)  
- **HTML** (Templates)  
- **Bootstrap** (UI)

---

## Requirements

Before running the project, install the necessary Python packages:

```bash
pip install -r requirements.txt
```

---

## Setup & Run

1. **Clone the repository**

```bash
git clone https://github.com/sobhan661/Botique.git
cd Botique
```

2. **Create & activate a Python virtual environment**

```bash
python -m venv venv
source venv/bin/activate
venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Apply migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Create a superuser (optional, for admin access)**

```bash
python manage.py createsuperuser
```

6. **Run the development server**

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser to view the app.

---

## License

This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for more information.

---