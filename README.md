# Multi-Factor-Authentication
# 3-Factor Authentication System

## Overview

This project is a 3-Factor Authentication System developed using Django, HTML/CSS, and a custom SMS gateway integration for sending One-Time Passwords (OTPs). It employs Traccar for enhanced security through SMS verification.

## Features

- **User Registration:** Seamless registration process with validation.
- **User Login:** Secure login with username and password.
- **OTP and PIN Verification:** Additional layers of authentication for enhanced security.
- **Email Notifications:** Personalized welcome emails upon successful registration.
- **SMS Functionality via Traccar:** Utilizes Traccar for SMS notifications during OTP verification.

## Technology Stack

- **Django:** Backend framework for robust web development.
- **HTML/CSS:** Frontend design for a user-friendly interface.
- **Traccar:** Integrated for reliable SMS functionality.
- **SQLite:** Lightweight, embedded database for data management.

## How to Use

1. Clone the repository: `git clone https://github.com/your-username/3-factor-authentication.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the Django server: `python manage.py runserver`
4. Access the application at [http://localhost:8000](http://localhost:8000)

## SMS Functionality with Traccar

The project integrates Traccar for sending SMS notifications during OTP verification. Traccar is a versatile GPS tracking system that is harnessed here for enhanced security through SMS.

### Configuration

1. **Traccar Installation:**
   - Install Traccar on a server following [Traccar installation instructions](https://www.traccar.org/installation/).

2. **Configure Traccar in Settings:**
   - In the Django project settings, configure Traccar server details for SMS functionality.

```python
# views.py

TRACCAR_API_URL = 'http://your-traccar-server:8082'
TRACCAR_API_KEY = 'your-traccar-api-key'
```
If you have any doubts as to how to run this file, please raise an issue and I will help you out 😁
