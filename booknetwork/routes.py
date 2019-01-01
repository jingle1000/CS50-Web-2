from flask import Flask, render_template, url_for, flash, jsonify, request, g, session, redirect, abort
from flask_paginate import Pagination, get_page_args
from werkzeug.security import generate_password_hash, check_password_hash
from booknetwork import app, Base, engine, db
from booknetwork.forms import RegistrationForm, LoginForm, SearchForm
from booknetwork.models import User, Review, Book
import requests
import datetime

#create database schema
Base.metadata.create_all(engine)

search_data = []

@app.route('/', methods=['GET', 'POST'])
def home():
    form = SearchForm()
    if request.method == "POST":
        text = form.searchText.data
        result = db.execute(
            "SELECT * FROM book WHERE (LOWER(isbn) LIKE LOWER(:text)) OR (LOWER(title) LIKE LOWER(:text)) OR (author LIKE LOWER(:text)) LIMIT 10",
            { "text": '%' + text + '%'} 
        ).fetchall()
        del search_data[:]
        for book in result:
            book_fields = {}
            book_fields['isbn'] = book[1]
            book_fields['title'] = book[2]
            book_fields['author'] = book[3]
            book_fields['year_published'] = book[4]
            search_data.append(book_fields)
        return redirect(url_for('search_results'))
    return render_template('index.html', form=form, dashboard=True)

@app.route('/searchresults')
def search_results():
    print('running search')
    print(search_data)
    return render_template('searchresults.html', results=search_data)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        print(hashed_password) ###remove for debugging
        db.execute(
                "INSERT INTO user (username, email, password) VALUES (:username, :email, :password)",
                { "username": form.username.data, "email":  form.email.data, "password": hashed_password }
            )
        db.commit()
        message = 'Account created successfully, please login!'
        return render_template('signup.html', form=form, message=message)
    return render_template('signup.html', form=form)

@app.route('/logout')
def logout():
    return redirect(url_for('home'))

