# app/routes.py
from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import User, SearchableContent
from app import db
from sqlalchemy import or_, text
from flask_wtf.csrf import CSRFProtect
import bleach

# Initialize CSRF protection
csrf = CSRFProtect()

# Sample data for search demonstration
SAMPLE_DATA = [
    {
        "title": "Introduction to Web Security",
        "description": "Learn about common web security vulnerabilities and how to protect against them."
    },
    {
        "title": "SQL Injection Prevention",
        "description": "Understanding SQL injection attacks and implementing proper defenses."
    },
    {
        "title": "Cross-Site Scripting (XSS)",
        "description": "Exploring XSS vulnerabilities and implementing content security policies."
    },
    {
        "title": "Authentication Best Practices",
        "description": "Learn about secure user authentication methods and password handling."
    },
    {
        "title": "CSRF Protection",
        "description": "Understanding Cross-Site Request Forgery attacks and implementing tokens."
    }
]

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Use SQLAlchemy's parameterized queries to prevent SQL injection
        user = User.query.filter_by(username=username).first()
        
        if user and user.password == password:  # In production, use proper password hashing
            return f"Welcome {bleach.clean(username)}!"
        else:
            return "Invalid credentials", 401
            
    return render_template('login.html')

@main.route('/search')
def search():
    query = request.args.get('q', '').lower()
    results = []
    
    if query:
        # Use parameterized queries to prevent SQL injection
        sanitized_query = bleach.clean(query)
        results = SearchableContent.query.filter(
            or_(
                SearchableContent.title.ilike(f'%{sanitized_query}%'),
                SearchableContent.description.ilike(f'%{sanitized_query}%')
            )
        ).all()
    
    return render_template('search.html', query=query, results=results)

@main.route('/echo')
def echo():
    message = request.args.get('message', '')
    # Sanitize output to prevent XSS
    sanitized_message = bleach.clean(message)
    return f"<h1>Echo: {sanitized_message}</h1>"