# WhatBytes Project

Welcome to the WhatBytes Project! This Django web application is designed to provide users with a comprehensive dashboard, user profile management, and authentication functionalities. It also includes features like password reset and account management.

## Features

- **Dashboard**: Displays user-specific information and provides links to other functionalities.
- **User Authentication**: Includes login, logout, and password change functionalities.
- **Password Reset**: Allows users to reset their passwords via email.
- **User Profile**: View and manage user profile information.
- **Registration**: New users can register an account.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/KHUSHI-AGARWAL-1/WhatBytes_Assignment.git
   cd myproject
 2. **Create a virtual environment and activate it:**

    ```bash
    python -m venv env
    env\Scripts\activate
3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
4. **Set up environment variables:**

     ```bash
    EMAIL_HOST_USER=your_email@gmail.com
    EMAIL_HOST_PASSWORD=your_email_password
5. **Apply migrations:**

   ```bash
   python manage.py migrate
6. **Create a superuser (optional but recommended):**

   ```bash
   python manage.py createsuperuser
7. **Run the development server:**

   ```bash
   python manage.py runserver

*The application will be available at http://127.0.0.1:8000/.*
