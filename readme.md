# 🎓 Student Management System

A full-stack, responsive Student Management Platform built with **FastAPI** on the backend and pure **HTML/JS/Tailwind CSS** on the frontend. This platform features secure role-based access control, allowing Administrators to manage course offerings and enrollments, while giving Students a seamless portal to discover courses, enroll, and manage their profiles.

## ✨ Features

### 🔐 Authentication & Security

* **JWT-Based Auth:** Secure login and session management.

* **Role-Based Routing:** Automatic frontend redirection to either the Admin Dashboard or Student Portal based on the authenticated user's role.

* **Secure Password Confirmation:** Sensitive profile updates require password validation.

### 👨‍🎓 Student Portal

* **Course Discovery:** Scrollable feed of all available courses and real-time course search functionality.

* **Seamless Enrollment:** Enroll in courses using UPI or Card credentials with instant success receipts and transaction IDs.

* **Profile Management:** View and edit personal details (Name, Email, Mobile, City) via a smooth modal interface.

### 👨‍💻 Admin Dashboard

* **Course Management:** Full CRUD operations (Add, Update, Delete) for the course catalog.

* **Enrollment Tracking:** View a detailed list of all students enrolled in a specific course, including transaction IDs.

## 📸 Screenshots & Demos

### 1. Login Screen
![Login Screen](assets/Screenshot%202026-11-11%20083306.png)

### 2. Sign Up Screen
![Sign Up Screen](assets/Screenshot%202026-11-11%20083559.png)

### 3. Student Portal & Enrollment
![Student Portal](assets/Screenshot%202026-11-11%20083408.png)

### 4. Admin Dashboard
![Admin Dashboard](assets/Screenshot%202026-11-11%20083459.png)

## 📂 Project Structure

Here is an overview of the project's architecture:

```
📦 Student-Management-System
 ┣ 📂 assets            # Images and screenshots for documentation
 ┣ 📂 database          # Database connection and session management
 ┣ 📂 exceptions        # Custom error handling and HTTP exceptions
 ┣ 📂 models            # SQLAlchemy Database Models
 ┃ ┣ 📜 __init__.py
 ┃ ┣ 📜 base.py
 ┃ ┣ 📜 courses.py
 ┃ ┣ 📜 payments.py
 ┃ ┗ 📜 users.py
 ┣ 📂 repos             # Repository layer for database queries
 ┣ 📂 routers           # FastAPI API Endpoints
 ┃ ┣ 📜 __init__.py
 ┃ ┣ 📜 admin_router.py
 ┃ ┣ 📜 auth_router.py
 ┃ ┗ 📜 student_router.py
 ┣ 📂 schemas           # Pydantic models for request/response validation
 ┣ 📂 services          # Core business logic
 ┃ ┣ 📜 __init__.py
 ┃ ┣ 📜 auth_service.py
 ┃ ┣ 📜 course_service.py
 ┃ ┣ 📜 payment_service.py
 ┃ ┗ 📜 student_service.py
 ┣ 📂 frontend          # HTML/JS/Tailwind User Interface
 ┃ ┣ 📜 admin.html
 ┃ ┣ 📜 index.html      # Login Page
 ┃ ┣ 📜 signup.html
 ┃ ┗ 📜 student.html
 ┣ 📂 tests             # Unit and integration tests
 ┃ ┣ 📜 __pycache__
 ┃ ┣ 📜 test_repo.py
 ┃ ┣ 📜 test_repo2.py
 ┃ ┣ 📜 test_routers.py
 ┃ ┗ 📜 test_service.py
 ┣ 📜 .env              # Environment variables (DB credentials, secret keys)
 ┣ 📜 .gitignore        # Ignored files for Git version control
 ┣ 📜 main.py           # Main FastAPI application entry point
 ┗ 📜 requirements.txt  # Python project dependencies

```

## 🚀 Getting Started

### Prerequisites

* Python 3.8+

* A modern web browser

* `pip` (Python package manager)

### 1. Backend Setup (FastAPI)

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/student-management-system.git
   cd student-management-system
   
   ```

2. Install the required dependencies using the requirements file:

   ```bash
   pip install -r requirements.txt
   
   ```

3. Set up your environment variables:

   * Create a `.env` file based on your required configurations (e.g., database URL, JWT secret key).

4. Run the FastAPI server via the main entry point:

   ```bash
   uvicorn main:app --reload
   
   ```

   *The backend will now be running on `http://127.0.0.1:8000`*

### 2. Frontend Setup

Because the frontend uses pure HTML, CSS (via Tailwind CDN), and JavaScript, no Node.js build process is required!

1. Navigate to the `frontend` folder.

2. Open `index.html` directly in your browser, or use a tool like **VS Code Live Server** to serve the files locally.

3. Ensure the `API_BASE_URL` in the frontend JavaScript blocks points to your running FastAPI instance (`http://127.0.0.1:8000`).

## 🛠️ Tech Stack

* **Backend:** Python, FastAPI, SQLAlchemy, Pydantic

* **Frontend:** HTML5, Vanilla JavaScript (Fetch API), Tailwind CSS

* **Authentication:** OAuth2 with Password Bearer (JWT Tokens)