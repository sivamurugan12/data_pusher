# Data Pusher - Django REST API

![Data Pusher](https://raw.githubusercontent.com/sivamurugan12/data_pusher/main/assets/data_pusher_banner.png)

## 📌 Overview
Data Pusher is a Django-based REST API designed to securely receive, process, and send data to multiple destinations via webhooks. This system allows users to create accounts, configure webhook destinations, and track API events while ensuring authentication, logging, and background task execution.

---

## 🚀 Features
![Features](https://raw.githubusercontent.com/sivamurugan12/data_pusher/main/assets/features.png)
- **User Authentication** - Secure JWT-based authentication.
- **Account Management** - Create and manage accounts.
- **Webhook Destinations** - Send data via webhooks.
- **Logging & Monitoring** - Track API events and requests.
- **Role-Based Access Control (RBAC)** - Admin and User roles.
- **Rate Limiting** - Limits 5 requests per second per account.
- **Asynchronous Processing** - Uses Celery & Redis for background tasks.
- **Advanced Querying & Filtering** - Search logs, accounts, and destinations.
- **Performance Optimization** - Django caching for faster responses.
- **API Documentation** - Swagger for interactive API reference.

---

## 📂 Project Structure
![Project Structure](https://raw.githubusercontent.com/sivamurugan12/data_pusher/main/assets/project_structure.png)
```
/data_pusher
│── accounts/             # Account management module
│── destinations/         # Webhook destination handling
│── logs/                 # API event logging system
│── users/                # User authentication & management
│── roles/                # Role-based access control
│── account_members/      # Links users to accounts
│── manage.py             # Django project manager
│── requirements.txt      # Dependencies list
│── db.sqlite3            # Database (SQLite/PostgreSQL)
```

---

## 🔧 Installation & Setup
### Prerequisites
Ensure you have **Python 3.8+**, **pip**, and **Redis** installed.

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/sivamurugan12/data_pusher.git
cd data_pusher
```
### 2️⃣ Create a Virtual Environment & Install Dependencies
```sh
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate    # Windows
pip install -r requirements.txt
```
### 3️⃣ Apply Database Migrations
```sh
python manage.py migrate
```
### 4️⃣ Create an Admin User
```sh
python manage.py createsuperuser
```
### 5️⃣ Start the Server
```sh
python manage.py runserver
```
📌 **API is now available at:** `http://127.0.0.1:8000/`

---

## 🌐 API Endpoints
![API Endpoints](https://raw.githubusercontent.com/sivamurugan12/data_pusher/main/assets/api_endpoints.png)
| **Feature**        | **Method** | **URL**                    | **Auth Required?** |
|--------------------|-----------|----------------------------|--------------------|
| User Signup       | POST      | /api/users/register/       | ❌ No  |
| User Login        | POST      | /api/token/                | ❌ No  |
| Create Account    | POST      | /api/accounts/             | ✅ Yes |
| Add Destination   | POST      | /api/destinations/         | ✅ Yes |
| Log Event         | POST      | /api/logs/                 | ✅ Yes |

🔍 **Swagger API Docs:** `http://127.0.0.1:8000/swagger/`

---

## ⚡ Asynchronous Processing (Celery)
This project uses **Celery** to handle background tasks, ensuring efficient data processing.

### Start Celery Worker
```sh
celery -A data_pusher worker --loglevel=info
```

---

## 🔒 API Rate Limiting
Django’s built-in throttling restricts API requests to **5 per second per account** to prevent overuse.

---

## 🛠 Testing
Run unit tests to verify API functionality:
```sh
pytest
```

---

## 🤝 Contributing
We welcome contributions! Fork the repo, create a feature branch, and submit a pull request.

---

## 📜 License
This project is licensed under the **MIT License**.

---

## 🙌 Acknowledgments
Special thanks to **CustomerLabs** for providing this challenge and fostering innovation! 🚀


