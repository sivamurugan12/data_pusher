Data Pusher - Django REST API
📌 Overview
Data Pusher is a Django-based REST API designed to handle secure and efficient data transmission via webhooks. With this system, users can create accounts, configure webhook destinations, and track events seamlessly. It ensures reliable data handling with authentication, logging, and background task execution.

🚀 Features
Secure Authentication - JWT-based authentication for safe access.
Account Management - Create and manage multiple accounts.
Webhook Destinations - Send data to external platforms via webhooks.
Logging & Monitoring - Keep track of API events and data flow.
Role-Based Access Control (RBAC) - Admin and User roles for controlled access.
API Rate Limiting - Prevent abuse with a limit of 5 requests per second per account.
Asynchronous Processing - Uses Celery & Redis for background processing.
Advanced Querying & Filtering - Retrieve specific logs, accounts, and destinations easily.
Performance Optimization - Implements Django caching for faster API responses.
Swagger Documentation - Interactive API reference for easy integration.
📂 Project Structure
📁 data_pusher/
 ├── 📂 accounts/            # Account management module
 ├── 📂 destinations/        # Webhook destination handling
 ├── 📂 logs/                # API event logging system
 ├── 📂 users/               # User authentication & management
 ├── 📂 roles/               # Role-based access control
 ├── 📂 account_members/     # Links users to accounts
 ├── manage.py              # Django project manager
 ├── requirements.txt       # Dependencies list
 ├── db.sqlite3             # Database (SQLite/PostgreSQL)
🔧 Installation & Setup
Prerequisites
Ensure you have Python 3.8+, pip, and Redis installed.

1️⃣ Clone the Repository
git clone https://github.com/your-repo/data_pusher.git
cd data_pusher
2️⃣ Create a Virtual Environment & Install Dependencies
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
pip install -r requirements.txt
3️⃣ Apply Database Migrations
python manage.py migrate
4️⃣ Create an Admin User
python manage.py createsuperuser
5️⃣ Start the Server
python manage.py runserver
📌 API is now available at: http://127.0.0.1:8000/

🌐 API Endpoints
Feature	Method	URL	Auth Required?
User Signup	POST	/api/users/register/	❌ No
User Login	POST	/api/token/	❌ No
Create Account	POST	/api/accounts/	✅ Yes
Add Destination	POST	/api/destinations/	✅ Yes
Log Event	POST	/api/logs/	✅ Yes
🔍 Swagger API Docs: http://127.0.0.1:8000/swagger/

⚡ Asynchronous Processing (Celery)
This project uses Celery for background task execution, ensuring efficient data processing.

Start Celery Worker:
celery -A data_pusher worker --loglevel=info
🔒 API Rate Limiting
Django's built-in throttling restricts API requests to 5 per second per account to prevent overuse.

🛠 Testing
Run unit tests to verify API functionality:

pytest
🤝 Contributing
We welcome contributions! Fork the repo, create a feature branch, and submit a pull request.

📜 License
This project is licensed under the MIT License.

🙌 Acknowledgments
Special thanks to CustomerLabs for providing this challenge and fostering innovation! 🚀
