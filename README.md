# FurryBuddies

FurryBuddies is a Django web application that provides a platform for pet owners to create profiles, share photos, and connect over their furry companions. Users can create, edit, and delete posts, and view details of other pets in the community.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)

## Features

- **User Profile Management**: Create, edit, and delete user profiles with personal information and profile pictures.
- **Pet Management**: Add, edit, and remove pet profiles, including details like name, breed, and age.
- **Post Sharing**: Publish posts with pet images and short descriptions. Posts can be edited or deleted by their authors.
- **Dashboard**: View all published posts with pagination.
- **Post Details**: View detailed information about a selected post.
- **Author Profile**: View the author’s details, including the total number of pets and posts.
- **Delete Profiles and Posts**: When a user profile is deleted, all associated posts are removed from the platform.

## Images
![Home Screen](static/images/furry_screenshots/Screenshot%20from%202024-11-17%2012-29-43.png)
![Create Profile](static/images/furry_screenshots/Screenshot%20from%202024-11-17%2012-30-05.png)
![Profile Details](static/images/furry_screenshots/Screenshot%20from%202024-11-17%2012-31-56.png)
![Published Posts](static/images/furry_screenshots/Screenshot%20from%202024-11-17%2012-36-08.png)

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/furrybuddies.git
    cd furrybuddies
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On Mac/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Run migrations**:
    ```bash
    python manage.py migrate
    ```

6. **Create a superuser**:
    ```bash
    python manage.py createsuperuser
    ```

7. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

8. Visit `http://127.0.0.1:8000` in your browser to start using FurryBuddies.

## Usage

1. **Sign up** and create your author profile.
2. Add pets to your profile and upload photos or posts to showcase them.
3. Interact with posts on the dashboard, viewing details or editing/deleting as needed.
4. Manage your profile and see a summary of your pets and posts.

## Technologies Used

- **Backend**: Django, Django ORM
- **Frontend**: HTML, CSS
- **Database**: PostgreSQL
- **Other**: Django Template Language (DTL), Django Forms, Django Class-Based Views (CBVs)

