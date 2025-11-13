# 🚀 How to Run the NIE College Trainer Management System

## Quick Start (Easiest Method)

### Option 1: Using the Run Script
```bash
cd /home/prajjwal25/Desktop/Coding/DjangoPython/DjangoLearning
bash run_server.sh
```

### Option 2: Direct Command
```bash
cd /home/prajjwal25/Desktop/Coding/DjangoPython/DjangoLearning
/home/prajjwal25/Desktop/Coding/DjangoPython/.venv/bin/python manage.py runserver
```

## 🌐 Access the Application

Once the server is running, open your web browser and visit:

### Main Application:
- **Trainer Search Page**: http://127.0.0.1:8000/trainers/
  - Search trainers by name or email
  - Filter by department and specialization
  - View detailed trainer profiles

### Admin Panel:
- **Admin Interface**: http://127.0.0.1:8000/admin/
  - Manage trainers (add, edit, delete)
  - Advanced search and filtering
  - **Note**: You need to create a superuser first (see below)

## 👤 Create Admin Account (First Time Only)

To access the admin panel, create a superuser:

```bash
cd /home/prajjwal25/Desktop/Coding/DjangoPython/DjangoLearning
/home/prajjwal25/Desktop/Coding/DjangoPython/.venv/bin/python manage.py createsuperuser
```

Follow the prompts to enter:
- Username
- Email address (optional)
- Password

## 🛠️ Useful Commands

### Run the Server
```bash
/home/prajjwal25/Desktop/Coding/DjangoPython/.venv/bin/python manage.py runserver
```

### Stop the Server
Press `Ctrl + C` in the terminal

### Run Tests
```bash
/home/prajjwal25/Desktop/Coding/DjangoPython/.venv/bin/python manage.py test trainers
```

### Check for Issues
```bash
/home/prajjwal25/Desktop/Coding/DjangoPython/.venv/bin/python manage.py check
```

### Repopulate Sample Data
```bash
/home/prajjwal25/Desktop/Coding/DjangoPython/.venv/bin/python manage.py populate_trainers
```

### Make Migrations (after model changes)
```bash
/home/prajjwal25/Desktop/Coding/DjangoPython/.venv/bin/python manage.py makemigrations
/home/prajjwal25/Desktop/Coding/DjangoPython/.venv/bin/python manage.py migrate
```

## 📊 What You'll See

### Trainer Search Page (http://127.0.0.1:8000/trainers/)
- Modern, responsive interface
- Search form with filters
- Grid of trainer cards
- Click "View Details" to see full trainer profile

### Features Available:
✅ Search by name or email
✅ Filter by 6 departments (CS, ME, EC, CV, EE, IS)
✅ Filter by 6 specializations (AI, ML, Web, Database, Networking, Other)
✅ View 10 sample trainers
✅ Beautiful gradient design with animations

## 🎯 Expected Behavior

When you run the server, you should see:
```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
November 13, 2025 - XX:XX:XX
Django version 5.2.8, using settings 'nie_college.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

## ⚠️ Important Notes

1. **404 Error on Root URL**: If you visit http://127.0.0.1:8000/ directly, you'll get a 404 error. This is normal! The app is at http://127.0.0.1:8000/trainers/

2. **Server Must Be Running**: Keep the terminal window open while using the application

3. **Development Server**: This is for development only. Don't use it in production!

## 🐛 Troubleshooting

### Server Won't Start
```bash
# Check if Django is installed
/home/prajjwal25/Desktop/Coding/DjangoPython/.venv/bin/python -c "import django; print(django.get_version())"

# Check for database issues
/home/prajjwal25/Desktop/Coding/DjangoPython/.venv/bin/python manage.py migrate
```

### Port Already in Use
```bash
# Use a different port
/home/prajjwal25/Desktop/Coding/DjangoPython/.venv/bin/python manage.py runserver 8001
```

### Can't Access Admin
```bash
# Create a superuser
/home/prajjwal25/Desktop/Coding/DjangoPython/.venv/bin/python manage.py createsuperuser
```

## 📝 Sample Data

The application comes with 10 sample trainers:
- Rajesh Kumar (CS, AI, 8 years)
- Priya Sharma (CS, ML, 6 years)
- Amit Patel (CS, Web Development, 5 years)
- Sneha Reddy (EC, Networking, 7 years)
- Vikram Singh (ME, Robotics, 10 years)
- Anita Desai (IS, Database, 9 years)
- Karthik Iyer (EE, Power Systems, 4 years)
- Meera Nair (CS, AI, 3 years)
- Suresh Babu (CV, Structural, 12 years)
- Divya Krishnan (EC, ML, 5 years)

## 🎉 Enjoy!

Your Django application is fully functional and ready to use!

---
**Server is currently running!** 🟢
Visit: http://127.0.0.1:8000/trainers/
