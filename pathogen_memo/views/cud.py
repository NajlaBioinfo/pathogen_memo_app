from flask import Blueprint, render_template, Flask, jsonify, url_for, redirect, request, flash
from sys import version
from pathogen_memo.forms import pathogen_form

#from models import pathogen
from pathogen_memo.controllers import savequery

#Set word_count_site_name
cudv = Blueprint('cudv', __name__)


@cudv.route("/cud",methods=['GET', 'POST'])
def cud():
    
    #Create new pathogen
    form = pathogen_form.PathogenForm(request.form)

    if request.method == 'POST' and form.validate():
        pathogen_member = pathogen.Pathogen()

        savequery.save_changes(pathogen_member,form)

        flash('The new pathogen was created successfully!')

        return redirect('/hello')
    #else:
    #    flash('Some thing wrong occured please contact the admin.!')

    #    return redirect('/')
    return render_template("cud.html",form=form)