#!/bin/bash
# Automated MySQL Migration Script for NIE College Trainer Management System

set -e  # Exit on error

VENV_PYTHON="/home/prajjwal25/Desktop/Coding/DjangoPython/.venv/bin/python"
PROJECT_DIR="/home/prajjwal25/Desktop/Coding/DjangoPython/DjangoLearning"

echo "🗄️  MySQL Migration Script for NIE College Trainer Management System"
echo "===================================================================="
echo ""

# Step 1: Create MySQL Database
echo "📊 Step 1: Creating MySQL Database and User"
echo "-------------------------------------------"
echo "You will be prompted for your MySQL root password (if set)"
echo ""

mysql -u root -p << 'MYSQL_SCRIPT'
-- Create database
CREATE DATABASE IF NOT EXISTS nie_college_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Create user
CREATE USER IF NOT EXISTS 'nie_user'@'localhost' IDENTIFIED BY 'nie_password_123';

-- Fix authentication for MySQL 8.x
ALTER USER 'nie_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'nie_password_123';

-- Grant privileges
GRANT ALL PRIVILEGES ON nie_college_db.* TO 'nie_user'@'localhost';
FLUSH PRIVILEGES;

-- Verify
SELECT 'Database and user created successfully!' AS Status;
SHOW DATABASES LIKE 'nie_college_db';
MYSQL_SCRIPT

if [ $? -eq 0 ]; then
    echo "✅ MySQL database and user created successfully!"
else
    echo "❌ Failed to create database. Please check your MySQL root credentials."
    exit 1
fi

echo ""
echo "📝 Step 2: Updating Django Settings to Use MySQL"
echo "------------------------------------------------"

cd "$PROJECT_DIR"

# Update settings.py to use MySQL
python3 << 'EOF'
with open('nie_college/settings.py', 'r') as f:
    content = f.read()

# Comment SQLite section
content = content.replace(
    "# SQLite Configuration (backup/development)\nDATABASES = {\n    'default': {\n        'ENGINE': 'django.db.backends.sqlite3',\n        'NAME': BASE_DIR / 'db.sqlite3',\n    }\n}",
    "# SQLite Configuration (backup/development)\n# DATABASES = {\n#     'default': {\n#         'ENGINE': 'django.db.backends.sqlite3',\n#         'NAME': BASE_DIR / 'db.sqlite3',\n#     }\n# }"
)

# Uncomment MySQL section
content = content.replace(
    "# MySQL Configuration (uncomment to use)\n# DATABASES = {\n#     'default': {\n#         'ENGINE': 'django.db.backends.mysql',\n#         'NAME': 'nie_college_db',\n#         'USER': 'nie_user',\n#         'PASSWORD': 'nie_password_123',\n#         'HOST': 'localhost',\n#         'PORT': '3306',\n#         'OPTIONS': {\n#             'charset': 'utf8mb4',\n#             'init_command': \"SET sql_mode='STRICT_TRANS_TABLES'\",\n#         },\n#     }\n# }",
    "# MySQL Configuration\nDATABASES = {\n    'default': {\n        'ENGINE': 'django.db.backends.mysql',\n        'NAME': 'nie_college_db',\n        'USER': 'nie_user',\n        'PASSWORD': 'nie_password_123',\n        'HOST': 'localhost',\n        'PORT': '3306',\n        'OPTIONS': {\n            'charset': 'utf8mb4',\n            'init_command': \"SET sql_mode='STRICT_TRANS_TABLES'\",\n        },\n    }\n}"
)

with open('nie_college/settings.py', 'w') as f:
    f.write(content)

print("✅ Django settings updated to use MySQL")
EOF

echo ""
echo "🔄 Step 3: Running Django Migrations on MySQL"
echo "---------------------------------------------"

$VENV_PYTHON manage.py migrate

if [ $? -eq 0 ]; then
    echo "✅ Migrations completed successfully!"
else
    echo "❌ Migration failed. Check errors above."
    exit 1
fi

echo ""
echo "📥 Step 4: Loading Data from SQLite Backup"
echo "------------------------------------------"

if [ -f "data_backup.json" ]; then
    $VENV_PYTHON manage.py loaddata data_backup.json
    
    if [ $? -eq 0 ]; then
        echo "✅ Data imported successfully!"
    else
        echo "⚠️  Warning: Some data may not have been imported. Check errors above."
    fi
else
    echo "⚠️  No backup file found (data_backup.json). Skipping data import."
    echo "   You can populate sample data with: python manage.py populate_trainers"
fi

echo ""
echo "🎉 MySQL Migration Complete!"
echo "============================"
echo ""
echo "📊 Database Information:"
echo "  - Database: nie_college_db"
echo "  - User: nie_user"
echo "  - Password: nie_password_123"
echo "  - Host: localhost:3306"
echo ""
echo "🚀 To start the server:"
echo "   $VENV_PYTHON manage.py runserver"
echo ""
echo "🌐 Then visit: http://127.0.0.1:8000/trainers/"
echo ""
echo "🔍 Verify data in MySQL:"
echo "   mysql -u nie_user -p'nie_password_123' nie_college_db -e 'SELECT COUNT(*) FROM trainers_trainer;'"
echo ""
