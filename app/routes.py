# app/routes.py
from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import User, SearchableContent
from app import db
from sqlalchemy import or_, text

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
        # Intentionally vulnerable SQL injection using raw SQL
        query = text(f"SELECT * FROM user WHERE username='{username}' AND password='{password}'")
        print(f"Executing SQL query: {query}")  # Debug output
        try:
            result = db.session.execute(query)
            user = result.first()
            print(f"Query result: {user}")  # Debug output
            if user:
                return f"Welcome {username}!"
            else:
                return "Invalid credentials", 401
        except Exception as e:
            print(f"Database error: {str(e)}")  # Debug output
            return f"Database error: {str(e)}", 500
    return render_template('login.html')

@main.route('/search')
def search():
    query = request.args.get('q', '').lower()
    results = []
    
    if query:
        # Search through the database using SQL LIKE
        # Intentionally vulnerable to SQL injection
        results = SearchableContent.query.filter(
            or_(
                SearchableContent.title.ilike(f'%{query}%'),
                SearchableContent.description.ilike(f'%{query}%')
            )
        ).all()
    
    return render_template('search.html', query=query, results=results)

@main.route('/echo')
def echo():
    message = request.args.get('message', '')
    # Intentionally vulnerable to XSS
    return f"<h1>Echo: {message}</h1>"