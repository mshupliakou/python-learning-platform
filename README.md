# 🐍 PyLearn - Python Learning Platform

![Python](https://img.shields.io/badge/Python-3.9-blue?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0-green?style=for-the-badge&logo=flask&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-NeonDB-336791?style=for-the-badge&logo=postgresql&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple?style=for-the-badge&logo=bootstrap&logoColor=white)

**PyLearn** is a comprehensive web-based Learning Management System (LMS) designed to teach Python programming. The platform provides a structured learning path with modules, lessons, and interactive quizzes to test user knowledge.

🚀 **Live Demo:** [https://pylearn-mshupliakou.onrender.com](https://pylearn-mshupliakou.onrender.com)

---

## 📄 Documentation

> ⚠️ **Note:** Comprehensive project documentation (including architecture details, database schema, and requirements analysis) is included in this repository, but it is currently available in **Polish 🇵🇱 only**.

You can find the documentation PDF files in the project files.

---

## ✨ Key Features

### 🎓 For Students
* **Structured Learning:** Access to organized modules and lessons.
* **Interactive Quizzes:** Test your knowledge after each lesson with auto-grading system.
* **Progress Tracking:** Prevents retaking already completed quizzes to ensure integrity.
* **Modern UI:** Dark-themed, mobile-friendly interface built with Bootstrap 5.
* **Syntax Highlighting:** Code examples are beautifully formatted using Prism.js.

### 🛠️ For Administrators
* **Content Management:** Create, edit, and delete modules and lessons via a GUI.
* **Rich Text Editor:** Integrated **TinyMCE** editor for formatting lesson content (images, code blocks, tables).
* **Quiz Builder:** Dynamic interface for creating questions and answers.
* **Role-Based Access Control (RBAC):** Admin dashboard is protected and accessible only to authorized users.

---

## 🏗️ Tech Stack

* **Backend:** Python, Flask (Microframework)
* **Database:** PostgreSQL (Hosted on NeonDB), SQLAlchemy ORM
* **Frontend:** HTML5, CSS3, JavaScript, Bootstrap 5, Jinja2 Templates
* **Authentication:** Flask-Login, Werkzeug Security
* **Deployment:** Render.com, Gunicorn WSGI

---

## ⚙️ Installation & Local Setup

If you want to run this project locally, follow these steps:

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/mshupliakou/python-learning-platform.git](https://github.com/mshupliakou/python-learning-platform.git)
    cd python-learning-platform
    ```

2.  **Create a virtual environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment Variables**
    Create a `.env` file in the root directory and add the following:
    ```env
    SECRET_KEY=your_secret_key_here
    DATABASE_URL=postgresql://user:password@host/database
    ```
    *(Note: You need a running PostgreSQL instance or a connection string to a cloud DB like NeonDB)*

5.  **Run the application**
    ```bash
    python run.py
    ```
    The app will be available at `http://127.0.0.1:5000`.

---

## 📂 Project Structure

```text
├── app/
│   ├── static/          # CSS, JS, Images
│   ├── templates/       # HTML files (Jinja2)
│   ├── __init__.py      # App factory & DB config
│   ├── models.py        # Database models (User, Module, Lesson, Quiz)
│   └── routes.py        # Application logic & View functions
├── requirements.txt     # Python dependencies
└── run.py               # Entry point
```

## 🤝 Contributing
Contributions, issues, and feature requests are welcome!

## 📝 Author
Mikhail Shupliakou
