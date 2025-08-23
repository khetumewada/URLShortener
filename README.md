# 🔗 URL Shortener

A simple and efficient **URL Shortener** built with **Django**. It allows users to convert long URLs into short, shareable links and track usage.

---

## 🚀 Features

* Shorten long URLs into unique short links
* Redirect from short link to original URL
* Track number of clicks on each shortened URL
* User authentication (sign up, login, logout)
* Social login with Google
* Responsive UI with mobile support
* Deployed on **Render** with **PostgreSQL** database

---

## 🛠️ Tech Stack

* **Backend:** Django, Django REST Framework
* **Database:** PostgreSQL
* **Frontend:** HTML, TailwindCSS
* **Authentication:** Django Auth, Google OAuth (via AllAuth)
* **Deployment:** Render

---

## ⚙️ Installation (Windows)

1. **Clone the repository**

   ```powershell
   git clone https://github.com/khetumewada/URLShortener.git
   cd URLShortener
   ```

2. **Create and activate a virtual environment**

   ```powershell
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. **Install dependencies**

   ```powershell
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the project root:

   ```env
   SECRET_KEY=your_secret_key
   DEBUG=True
   DATABASE_URL=postgres://username:password@hostname:port/dbname
   ALLOWED_HOSTS=127.0.0.1,localhost
   ```

5. **Apply migrations & collect static files**

   ```powershell
   python manage.py migrate
   python manage.py collectstatic
   ```

6. **Run the development server**

   ```powershell
   python manage.py runserver
   ```

👉 Open `http://127.0.0.1:8000` in your browser.

---

## 🌍 Deployment

The project is deployed on **Render**.

👉 Live Project: [URL Shortener](https://urlshortener-28e3.onrender.com)

---

## 📜 License

This project is licensed under the **MIT License**.
