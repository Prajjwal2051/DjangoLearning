# NIE College Trainer Management System

A Django-based web application for managing trainers at NIE College with comprehensive search and filtering capabilities.

## Features

- **Trainer Management**: Complete CRUD operations for trainer profiles
- **Advanced Search**: Search trainers by name, email, department, and specialization
- **Detailed Profiles**: View comprehensive trainer information including experience, bio, and contact details
- **Admin Panel**: Full-featured Django admin interface for managing trainers
- **Responsive Design**: Modern, mobile-friendly UI with beautiful styling
- **Comprehensive Tests**: Full test coverage for models, views, and admin functionality

## Project Structure

```
DjangoLearning/
├── nie_college/              # Main project configuration
│   ├── settings.py          # Project settings
│   ├── urls.py              # Main URL configuration
│   └── wsgi.py              # WSGI configuration
├── trainers/                # Trainers app
│   ├── models.py            # Trainer model definition
│   ├── views.py             # View functions for listing and detail pages
│   ├── admin.py             # Admin panel configuration
│   ├── urls.py              # App URL patterns
│   ├── tests.py             # Comprehensive test suite
│   ├── templates/           # HTML templates
│   │   └── trainers/
│   │       ├── base.html           # Base template
│   │       ├── trainer_list.html   # Trainer listing with search
│   │       └── trainer_detail.html # Trainer detail view
│   └── management/
│       └── commands/
│           └── populate_trainers.py  # Sample data generator
├── manage.py                # Django management script
└── README.md                # This file
```

## Installation & Setup

1. **Activate Virtual Environment**:
   ```bash
   source venv/bin/activate.fish
   ```

2. **Install Dependencies** (already installed):
   ```bash
   pip install django
   ```

3. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

4. **Populate Sample Data**:
   ```bash
   python manage.py populate_trainers
   ```

5. **Create Superuser** (for admin access):
   ```bash
   python manage.py createsuperuser
   ```

6. **Run Development Server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the Application**:
   - Trainer Search: http://127.0.0.1:8000/trainers/
   - Admin Panel: http://127.0.0.1:8000/admin/

## Usage

### Searching for Trainers

1. Navigate to `/trainers/` to see all active trainers
2. Use the search box to find trainers by name or email
3. Filter by department (CS, ME, EC, CV, EE, IS)
4. Filter by specialization (AI, ML, Web Development, Database, Networking, Other)
5. Click "View Details" on any trainer card to see complete information

### Admin Panel Features

- Add, edit, and delete trainers
- Advanced filtering and search
- Bulk operations
- Field organization with collapsible sections

## Models

### Trainer Model

- **Personal Information**: First name, last name, email, phone
- **Professional Details**: Department, specialization, years of experience
- **Additional Info**: Bio, join date, active status
- **Timestamps**: Auto-tracked creation and update times

**Departments**: Computer Science, Mechanical Engineering, Electronics & Communication, Civil Engineering, Electrical Engineering, Information Science

**Specializations**: AI, Machine Learning, Web Development, Database Management, Networking, Other

## Running Tests

Execute the comprehensive test suite:

```bash
python manage.py test trainers
```

The test suite includes:
- **Model Tests**: Creation, string representation, ordering
- **View Tests**: List view, detail view, search, filtering
- **Admin Tests**: Registration verification

All 14 tests pass successfully! ✅

## API Endpoints

- `GET /trainers/` - List all trainers with optional search/filter parameters
  - Query params: `q` (search), `department`, `specialization`
- `GET /trainers/<id>/` - View specific trainer details

## Technologies Used

- **Django 5.2.8**: Web framework
- **SQLite**: Database (default)
- **HTML/CSS**: Frontend templates with embedded styling
- **Python 3**: Programming language

## Sample Data

The application includes 10 sample trainers across different departments and specializations. Use the `populate_trainers` management command to reset or recreate sample data.

## Development

To continue development:

1. Modify models in `trainers/models.py`
2. Create and run migrations: `python manage.py makemigrations && python manage.py migrate`
3. Update views in `trainers/views.py`
4. Customize templates in `trainers/templates/trainers/`
5. Add tests in `trainers/tests.py`
6. Run tests frequently: `python manage.py test`

## Future Enhancements

- Add REST API using Django REST Framework
- Implement trainer ratings and reviews
- Add course assignments to trainers
- Create student-trainer matching system
- Add authentication and user roles
- Export trainer data to CSV/PDF
- Add profile pictures for trainers
- Implement email notifications

## License

This is a learning project for NIE College trainer management.

---

**Created with Django 5.2.8** | **Last Updated: November 2025**

College Django sikha rhaa tha.....
