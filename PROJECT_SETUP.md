# KitchenInventory Django Project

This is a Django project for managing kitchen inventory with user registration.

## Project Structure

- **KitchenInventory/**: Main project directory containing settings and configuration
- **inventory/**: Django app for managing kitchen inventory
- **registration/**: Django app for user registration
- **manage.py**: Django management script

## Database Configuration

The project is configured to use MySQL database with the following settings:
- Database name: `kitchen_inventory`
- Host: `localhost`
- Port: `3306`
- User: `root`
- Password: (empty - should be configured for production)

## Setup Instructions

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Create MySQL database:
   ```sql
   CREATE DATABASE kitchen_inventory;
   ```

3. Run migrations:
   ```bash
   python manage.py migrate
   ```

4. Create superuser (optional):
   ```bash
   python manage.py createsuperuser
   ```

5. Run development server:
   ```bash
   python manage.py runserver
   ```

## Dependencies

- Django 4.2.x
- mysqlclient 2.2.0+

## Apps

### inventory
Django app for managing kitchen inventory items.

### registration
Django app for handling user registration and authentication.
