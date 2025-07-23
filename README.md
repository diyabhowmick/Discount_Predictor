# 🛍️ Discount Prediction Web Application
This is a Django-based web application that predicts discounts for products based on input parameters using a trained model. The application provides a simple web interface where users can enter product details and receive discount predictions.

## 📁 Project Structure
Discount Prediction/

└── 22112007_predict/
    ├── manage.py
    ├── db.sqlite3                  # SQLite database
    ├── templates/                  # HTML templates
    │   ├── predict_discount.html   # Input form
    │   └── prediction_result.html  # Output result page
    ├── predict/                    # Django app configuration
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py

    
## 🚀 Features
1. Web form to input product-related data
2. Displays predicted discount based on ML model
3. Built with Django (Python Web Framework)
4. Stores data using SQLite

## 🛠️ Setup Instructions

### 1. Clone the project or extract the zip
unzip 'Discount Prediction.zip'
cd '22112007_predict'

### 2. Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

### 3. Install dependencies
pip install -r requirements.txt

### 4. If requirements.txt is not present, you can manually install Django:
pip install django

### 5. Run database migrations
python manage.py migrate

### 6. Run the server
python manage.py runserver

### 7. Open the app in your browser
http://127.0.0.1:8000/


## 📄 Templates Overview
predict_discount.html: Accepts product features as input.
prediction_result.html: Displays the predicted discount.

## ⚙️ Requirements
1. Python 3.7+
2. Django 4.x+
3. SQLite (default with Django)

## 📌 Notes
The ML model code or .pkl file does not appear in the extracted files, so the prediction logic may need to be added or restored if missing.
The database file db.sqlite3 is pre-included and might contain previous predictions or logs.

