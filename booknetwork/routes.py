from flask import Flask, render_template, url_for, flash, jsonify, request, g, session, redirect, abort
from flask_paginate import Pagination, get_page_args
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

@app.route('/logout')
def logout():
    return redirect(url_for('home'))

