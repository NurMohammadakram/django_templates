# Student Management System

A Django-based web application for managing student information with CRUD (Create, Read, Update, Delete) operations.

## Project Overview

This project is a student information management system built with Django. It allows users to add, view, edit, and delete student records through a user-friendly web interface.

## Project Structure

```
myProject/
├── db.sqlite3                 # SQLite database
├── manage.py                  # Django management script
├── myProject/                 # Main project directory
│   ├── __init__.py
│   ├── asgi.py               # ASGI configuration
│   ├── settings.py           # Django settings
│   ├── urls.py               # Main URL configuration
│   └── wsgi.py               # WSGI configuration
└── student_info/              # Student app
    ├── migrations/           # Database migrations
    ├── static/
    │   └── student_info/
    │       └── css/
    │           └── style.css # Styling
    ├── templates/            # HTML templates
    │   ├── base.html         # Base template
    │   ├── index.html        # Home page
    │   ├── includes/         # Template includes
    │   │   ├── footer.html
    │   │   └── header.html
    │   └── student/
    │       ├── add_student.html    # Add student form
    │       ├── edit_student.html   # Edit student form
    │       └── show_student.html   # Student details
    ├── admin.py              # Admin configuration
    ├── apps.py               # App configuration
    ├── models.py             # Database models
    ├── tests.py              # Unit tests
    ├── urls.py               # App URL configuration
    └── views.py              # View functions/classes
└── media/                     # User-uploaded files
    └── student_info/
```

## Technology Stack

- **Backend**: Django
- **Database**: SQLite
- **Frontend**: HTML, CSS
- **Python**: 3.x

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Setup Instructions

1. **Clone or navigate to the project directory**:
   ```bash
   cd myProject
   ```

2. **Create and activate a virtual environment** (optional but recommended):
   ```bash
   python -m venv .venv
   
   # On Windows:
   .venv\Scripts\activate
   
   # On macOS/Linux:
   source .venv/bin/activate
   ```

3. **Install required dependencies**:

- Install from the included `requirements.txt` (recommended):
   ```bash
   pip install -r requirements.txt
   ```

- Or install only Pillow (used for image handling):
   ```bash
   pip install pillow
   ```

4. **Run migrations** (if needed):
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser** (for admin access):
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the application**:
   - Main application: `http://localhost:8000`
   - Admin panel: `http://localhost:8000/admin`

## Features

- ✅ **Add Students**: Create new student records with relevant information
- ✅ **View Students**: Display list of all students and individual student details
- ✅ **Edit Students**: Update existing student information
- ✅ **Delete Students**: Remove student records from the system
- ✅ **Responsive Design**: Clean and user-friendly interface
- ✅ **Admin Panel**: Django admin interface for database management

## Usage

### Adding a Student

1. Navigate to the application home page
2. Click on "Add Student" button
3. Fill in the student information form
4. Click "Submit" to save the student record

### Viewing Students

1. View the list of all students on the home page
2. Click on a student to view detailed information

### Editing a Student

1. Click on the student record you want to edit
2. Click the "Edit" button
3. Modify the information
4. Click "Save" to update the record

### Deleting a Student

1. Navigate to the student's detail page
2. Click the "Delete" button
3. Confirm the deletion

## Key Files

| File | Description |
|------|-------------|
| `models.py` | Defines the Student data model |
| `views.py` | Contains view logic for CRUD operations |
| `urls.py` | Maps URLs to views |
| `admin.py` | Registers models in Django admin |
| `templates/base.html` | Base template for all pages |
| `static/student_info/css/style.css` | Application styling |

## Admin Interface

Access the Django admin panel at `/admin` to:
- Manage student records directly
- View database statistics
- Perform bulk operations

## Database

The project uses SQLite (`db.sqlite3`), which is lightweight and suitable for development. For production, consider migrating to PostgreSQL or MySQL.

## Common Commands

```bash
# Create new migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver

# Access Django shell
python manage.py shell

# Collect static files (production)
python manage.py collectstatic
```

## Future Enhancements

- Add authentication/user accounts
- Implement search and filter functionality
- Add student enrollment tracking
- Export student data to CSV/PDF
- Add grade management system
- Implement email notifications

## Troubleshooting

**Issue**: Port 8000 is already in use
```bash
python manage.py runserver 8080
```

**Issue**: Database migration errors
```bash
python manage.py migrate --fake-initial
```

**Issue**: Missing dependencies
```bash
pip install -r requirements.txt
```

---

For more information on Django, visit: [Django Documentation](https://docs.djangoproject.com/)