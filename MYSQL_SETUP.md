# 🗄️ MySQL Setup Guide for NIE College Trainer Management System

This guide will help you migrate from SQLite to MySQL.

## Prerequisites

✅ MySQL 8.4.6 is already installed
✅ PyMySQL package is already installed
✅ Data backup created: `data_backup.json`

## Step 1: Create MySQL Database and User

Run the SQL setup script with ONE of these commands:

### Option A: If MySQL root has no password (common on local dev)
```bash
sudo mysql < setup_mysql.sql
```

### Option B: If MySQL root requires password
```bash
mysql -u root -p < setup_mysql.sql
```

### Option C: Manual setup (if script fails)
```bash
sudo mysql
# Or: mysql -u root -p

# Then run these commands:
CREATE DATABASE IF NOT EXISTS nie_college_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER IF NOT EXISTS 'nie_user'@'localhost' IDENTIFIED BY 'nie_password_123';
GRANT ALL PRIVILEGES ON nie_college_db.* TO 'nie_user'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

## Step 2: Fix MySQL Authentication Plugin Error

If you get "Plugin 'mysql_native_password' is not loaded" error, you need to change the authentication method:

```bash
sudo mysql
# Or: mysql -u root -p

# Run this command:
ALTER USER 'nie_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'nie_password_123';
FLUSH PRIVILEGES;
EXIT;
```

## Step 3: Enable MySQL Configuration in Django

The settings are already prepared. Just uncomment the MySQL section in `nie_college/settings.py`:

```bash
# Edit the file and swap commented sections, or run this automated script:
python3 << 'EOF'
import re

with open('nie_college/settings.py', 'r') as f:
    content = f.read()

# Comment SQLite
content = content.replace(
    "# SQLite Configuration (backup/development)\nDATABASES = {\n    'default': {\n        'ENGINE': 'django.db.backends.sqlite3',",
    "# SQLite Configuration (backup/development)\n# DATABASES = {\n#     'default': {\n#         'ENGINE': 'django.db.backends.sqlite3',"
)
content = content.replace(
    "        'NAME': BASE_DIR / 'db.sqlite3',\n    }\n}",
    "#         'NAME': BASE_DIR / 'db.sqlite3',\n#     }\n# }"
)

# Uncomment MySQL
content = content.replace(
    "# MySQL Configuration (uncomment to use)\n# DATABASES = {",
    "# MySQL Configuration\nDATABASES = {"
)
content = content.replace("#     'default': {", "    'default': {")
content = content.replace("#         'ENGINE'", "        'ENGINE'")
content = content.replace("#         'NAME'", "        'NAME'")
content = content.replace("#         'USER'", "        'USER'")
content = content.replace("#         'PASSWORD'", "        'PASSWORD'")
content = content.replace("#         'HOST'", "        'HOST'")
content = content.replace("#         'PORT'", "        'PORT'")
content = content.replace("#         'OPTIONS'", "        'OPTIONS'")
content = content.replace("#             'charset'", "            'charset'")
content = content.replace("#             'init_command'", "            'init_command'")
content = content.replace("#         },", "        },")
content = content.replace("#     }\n# }", "    }\n}")

with open('nie_college/settings.py', 'w') as f:
    f.write(content)

print("✅ Settings updated to use MySQL!")
EOF
```

## Step 4: Run Migrations

Create the database tables in MySQL:

```bash
/home/prajjwal25/Desktop/Coding/DjangoPython/.venv/bin/python manage.py migrate
```

## Step 5: Import Data from SQLite

Load the backed up data into MySQL:

```bash
/home/prajjwal25/Desktop/Coding/DjangoPython/.venv/bin/python manage.py loaddata data_backup.json
```

## Step 6: Test the Application

```bash
/home/prajjwal25/Desktop/Coding/DjangoPython/.venv/bin/python manage.py runserver
```

Visit: http://127.0.0.1:8000/trainers/

## 🔍 Verify MySQL Connection

Check that data is in MySQL:

```bash
mysql -u nie_user -p'nie_password_123' nie_college_db -e "SELECT * FROM trainers_trainer;"
```

## 🔐 Security Notes

**IMPORTANT:** The default password `nie_password_123` is for development only!

For production:
1. Change the password:
   ```sql
   ALTER USER 'nie_user'@'localhost' IDENTIFIED BY 'your_strong_password';
   ```
2. Store credentials in environment variables or a `.env` file
3. Never commit passwords to git!

## 📊 Database Information

- **Database Name:** nie_college_db
- **Username:** nie_user
- **Password:** nie_password_123 (change this!)
- **Host:** localhost
- **Port:** 3306
- **Charset:** utf8mb4

## 🛠️ Useful MySQL Commands

### Check database size
```bash
mysql -u nie_user -p'nie_password_123' nie_college_db -e "
SELECT 
    table_name AS 'Table',
    ROUND(((data_length + index_length) / 1024 / 1024), 2) AS 'Size (MB)'
FROM information_schema.TABLES 
WHERE table_schema = 'nie_college_db'
ORDER BY (data_length + index_length) DESC;
"
```

### View all trainers
```bash
mysql -u nie_user -p'nie_password_123' nie_college_db -e "
SELECT id, name, email, department, specialization 
FROM trainers_trainer 
LIMIT 10;
"
```

### Drop database (if you need to start over)
```bash
mysql -u nie_user -p'nie_password_123' -e "DROP DATABASE nie_college_db;"
```

## ⚠️ Troubleshooting

### Error: "Access denied for user"
- Check username and password
- Make sure you ran the setup SQL script
- Try the ALTER USER command from Step 2

### Error: "Unknown database"
- Run the CREATE DATABASE command from Step 1

### Error: "Can't connect to MySQL server"
- Check if MySQL service is running: `sudo systemctl status mysqld`
- Start MySQL: `sudo systemctl start mysqld`

### Error: "Plugin 'mysql_native_password' is not loaded"
- Run the ALTER USER command from Step 2
- This is common with MySQL 8.x

## 🔄 Switch Back to SQLite

If you need to switch back to SQLite:

1. Edit `nie_college/settings.py`
2. Comment the MySQL DATABASES section
3. Uncomment the SQLite DATABASES section
4. Restart the server

---

**Ready to migrate? Follow the steps above!** 🚀
