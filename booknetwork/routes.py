from flask import Flask, render_template, url_for, flash, jsonify, request, g, session, redirect, abort
from flask_paginate import Pagination, get_page_args
from booknetwork import app, Base, engine, db
from booknetwork.forms import RegistrationForm, LoginForm, SearchForm
from booknetwork.models import User, Review, Book
import requests
import datetime

#create database schema
Base.metadata.create_all(engine)

@app.route('/')
def home():
    form = SearchForm()
    return render_template('index.html', form=form)

