from pathogen_memo import application,db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

import os
from flask import Flask, jsonify, redirect, render_template, flash, Blueprint, request, session, url_for
from flask_login import login_required, logout_user, current_user, login_user
from flask import current_app as app
from werkzeug.security import generate_password_hash, check_password_hash
from sys import version

from pathogen_memo.forms import login_form, signup_form
from flask_login import LoginManager


login_manager = LoginManager()
login_manager.init_app(application)

class User(UserMixin, db.Model):
    """Model for user accounts."""

    __tablename__ = 'flasklogin_users'

    id = db.Column(db.Integer,
                   primary_key=True)
    name = db.Column(db.String,
                     nullable=False,
                     unique=False)
    email = db.Column(db.String(40),
                      unique=True,
                      nullable=False)
    password = db.Column(db.String(200),
                         primary_key=False,
                         unique=False,
                         nullable=False)
    website = db.Column(db.String(60),
                        index=False,
                        unique=False,
                        nullable=True)
    created_on = db.Column(db.DateTime,
                           index=False,
                           unique=False,
                           nullable=True)
    last_login = db.Column(db.DateTime,
                           index=False,
                           unique=False,
                           nullable=True)

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)




# Blueprint Configuration
auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login_page():
    """User login page."""
    # Bypass Login screen if user is logged in
    if current_user.is_authenticated:
        #return redirect(url_for('main_bp.dashboard'))
        return redirect(url_for('indexv.index'))
    lgform = login_form.LoginForm(request.form)

    # POST: Create user and redirect them to the app
    if request.method == 'POST' and lgform.validate():
        
        if lgform.validate():
            # Get Form Fields
            email = request.form.get('email')
            password = request.form.get('password')
            # Validate Login Attempt
            user = User.query.filter_by(email=email).first()
            if user:
                if user.check_password(password=password):
                    login_user(user)
                    next = request.args.get('next')
                    #return redirect(next or url_for('main_bp.dashboard'))
                    return redirect(next or url_for('indexv.index'))
        flash('Invalid username/password combination')
        return redirect(url_for('auth_bp.login_page'))
    # GET: Serve Log-in page
    return render_template('login.html',
                           form=lgform,
                           title='Log in | PathogenMemo.',
                           template='login-page',
                           body="Log in with your User account.")


                           
@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup_page():
    """User sign-up page."""
    sigf= signup_form.SignupForm(request.form)
    # POST: Sign user in

    if request.method == 'POST' and sigf.validate():
        if sigf.validate():
            # Get Form Fields
            name = request.form.get('name')
            email = request.form.get('email')
            password = request.form.get('password')
            website = request.form.get('website')
            existing_user = User.query.filter_by(email=email).first()
            if existing_user is None:
                user = User(name=name,
                            email=email,
                            password=generate_password_hash(password, method='sha256'),
                            website=website)
                db.session.add(user)
                db.session.commit()
                login_user(user)
                #return redirect(url_for('main_bp.dashboard'))
                return redirect(url_for('indexv.index'))
            flash('A user already exists with that email address.')
            return redirect(url_for('auth_bp.signup_page'))
    # GET: Serve Sign-up page
    return render_template('/signup.html',
                           title='Create an Account | PathogenMemo.',
                           form=sigf,
                           template='signup-page',
                           body="Sign up for a user account.")

@auth_bp.route("/logout")
@login_required
def logout_page():
    """User log-out logic."""
    logout_user()
    return redirect(url_for('auth_bp.login_page'))


@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in on every page load."""
    if user_id is not None:
        return User.query.get(user_id)
    return None


@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    flash('You must be logged in to view that page.')
    return redirect(url_for('auth_bp.login_page'))