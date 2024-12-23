# User Management - Django Authentication

 

https://github.com/user-attachments/assets/73afc887-a325-43bc-8ddd-c7849353f5d8


## Overview
This project implements a robust user authentication system using Django. It includes features such as login, logout, Google OAuth2 authentication, password reset via email, and enhanced security measures. Additionally, the project emphasizes user-friendly UI/UX to ensure a seamless experience.

---

## Features

### 1. **User Authentication**
- Secure user registration with form validation.
- User login and logout functionality.
- Persistent sessions managed securely.

### 2. **Google OAuth2 Integration**
- Allows users to log in using their Google accounts.
- Implemented using Django-Allauth or similar libraries.

### 3. **Password Management**
- Password reset functionality via email.
- Secure token generation for reset links.
- Password strength validation for increased security.

### 4. **UI/UX Design**
- Modern and responsive design for all authentication-related pages:
  - Login
  - Signup
  - Password Reset
  - Password Reset Confirmation
- Error messages displayed intuitively to guide the user.

### 5. **Security Features**
- Passwords stored using Django's secure hashing mechanism.
- CSRF protection enabled.
- Secure token validation for password reset.
- Account lockout after multiple failed login attempts.
- SSL recommended for production environments.

---

## Technologies Used

- **Framework**: Django
- **Frontend**: HTML5, CSS3, Bootstrap
- **Authentication**: Django-Allauth (for Google OAuth2)
- **Email**: SMTP or third-party email service (e.g., SendGrid, Mailgun)

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/sreenath-pydev/user_management
cd user_management
```
### 2. Create a Virtual Environment
    python -m venv venv

    # Activate the virtual environment
    venv\Scripts\activate

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
- Create a `.env` file in the project root.
- Add the following variables:
```env
EMAIL_HOST_USER='YOUR_MAIL@gmail.com'
EMAIL_HOST_PASSWORD='HOST_APP_PASSWORD' # https://knowledge.workspace.google.com/kb/how-to-create-app-passwords-000009237
DEFAULT_FROM_EMAIL='YOUR_MAIL@gmail.com'
GOOGLE_CLIENT_KEY = 'YOUR_KEY'
GOOGLE_CLIENT_SECRET = 'YOUR_SECRET'

```

### 5. Apply Migrations
```bash
python manage.py migrate
```

### 6. Run the Server
```bash
python manage.py runserver
```
Access the application at `http://127.0.0.1:8000/`.

---

## How It Works

### Login and Logout
- Users can log in with their registered email and password.
- Sessions are managed securely to maintain user authentication state.

### Google OAuth2 Authentication
- Users can log in using their Google accounts.
- The system fetches user profile details securely from Google.

### Password Reset
- Users can request a password reset link via email.
- Clicking the link redirects them to a secure page to set a new password.

### UI/UX Enhancements
- All forms are styled using Bootstrap for responsiveness.
- Error messages and success notifications guide users through the process.

### Security
- All sensitive data is hashed and encrypted.
- CSRF tokens are used to prevent cross-site request forgery.
- HTTPS is recommended for all production deployments.

---

## Contributing
We welcome contributions to improve the project! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`feature-name`).
3. Commit changes and push to your branch.
4. Submit a pull request.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

