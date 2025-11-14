# NIE College Trainer Management - React Frontend

A modern React frontend for the NIE College Trainer Management System built with Vite, React Router, and Axios.

## Features

- 🎨 **Modern UI**: Beautiful gradient design matching the Django templates
- 🔍 **Advanced Search**: Search trainers by name or email
- 🎯 **Filters**: Filter by department and specialization
- 📱 **Responsive Design**: Mobile-friendly interface
- ⚡ **Fast**: Built with Vite for optimal performance
- 🔄 **Live Updates**: Real-time data from Django REST API

## Prerequisites

Before running the React frontend, make sure:

1. **Django Backend is Running**
   ```bash
   cd /home/prajjwal25/Desktop/Coding/DjangoPython/DjangoLearning
   /home/prajjwal25/Desktop/Coding/DjangoPython/.venv/bin/python manage.py runserver
   ```

2. **Node.js is Installed** (version 16 or higher)

## Running the Application

### 1. Start Django Backend (Terminal 1)
```bash
cd /home/prajjwal25/Desktop/Coding/DjangoPython/DjangoLearning
/home/prajjwal25/Desktop/Coding/DjangoPython/.venv/bin/python manage.py runserver
```

### 2. Start React Frontend (Terminal 2)
```bash
cd /home/prajjwal25/Desktop/Coding/DjangoPython/DjangoLearning/frontend-react
npm run dev
```

### 3. Open in Browser
Visit: http://localhost:5173/

## Project Structure

```
frontend-react/
├── src/
│   ├── components/
│   │   ├── Header.jsx          # App header
│   │   ├── Footer.jsx          # App footer
│   │   ├── TrainerList.jsx     # Trainer listing with search
│   │   └── TrainerDetail.jsx   # Trainer details
│   ├── services/
│   │   └── api.js              # Axios API client
│   ├── App.jsx                 # Main app with routing
│   └── main.jsx                # Entry point
├── package.json
└── vite.config.js
```

## Technologies Used

- **React 19.2.0**: UI library
- **React Router 6.26.0**: Client-side routing
- **Axios 1.6.0**: HTTP client
- **Vite 7.2.2**: Build tool

## Troubleshooting

### "Failed to load trainers" Error
**Solution**: Make sure Django backend is running on port 8000

### CORS Errors
**Solution**: Django has `django-cors-headers` configured

---

**Built with ❤️ for NIE College**
