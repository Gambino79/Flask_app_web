from flask import Blueprint, render_template, request, flash, jsonify 
from flask_login import login_required, current_user
from .models import Expenses, Revenues, User
from datetime import datetime
from . import db
import json


views = Blueprint('views', __name__)

@views.route('/accounting', methods=['GET','POST'])
@login_required
def accounting():
    
    if request.method == 'POST' and request.form.get('company_name') != None:
        company_name = request.form.get('company_name')
        amount_expense = request.form.get('amount_expense')
        date_paid = request.form.get('date_paid')
        date_paid = datetime.strptime(date_paid, "%Y-%m-%d")
        switch = request.form.get('switch')
        
        
        if company_name == "":
            flash("Please fill in the company", category='error')
        elif amount_expense == "":
            flash("Please fill in the amount", category='error')
        elif date_paid == "":
            flash("Please fill in the date", category='error')
        elif switch == "":
            flash("Please fill in the switch", category='error')
        else:
            new_expenses = Expenses(company_name=company_name, amount_expense=amount_expense, date_paid=date_paid, switch_paid=switch)
            db.session.add(new_expenses)
            db.session.commit()
            flash('Expense added!', category='success')
            
    elif request.method == 'POST' and request.form.get('name') != None:
        name = request.form.get('name')
        amount_revenue = request.form.get('amount_revenue')
        date_received = request.form.get('date_received')
        date_received = datetime.strptime(date_received, "%Y-%m-%d")
        switch = request.form.get('switch')
        
        print(amount_revenue)
        
        if name == "":
            flash("Please fill the name of person", category='error')
        elif amount_revenue == "":
            flash("Please fill in the amount revenue", category='error')
        elif date_received == "":
            flash("Please fill in the date", category='error')
        elif switch == "":
            flash("Please fill in the switch", category='error')
        else:
            new_revenue = Revenues(name=name, amount_revenue=amount_revenue, date_received=date_received)   
            db.session.add(new_revenue)
            db.session.commit()
            flash('Revenue added!', category='success')
    return render_template("accounting.html", user=current_user) 

@views.route('/', methods=['GET','POST'])
@login_required
def home():
    if request.method == 'GET':
        expenses = Expenses.query.all()
        
        revenues = Revenues.query.all()
        
        return render_template("Home.html", expenses=expenses, user=current_user, revenues=revenues)    


