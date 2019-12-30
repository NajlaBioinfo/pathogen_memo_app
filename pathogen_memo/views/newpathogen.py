from flask import Blueprint, render_template, Flask, jsonify, url_for, redirect, request, flash
from sys import version
from forms import pathogen_form

#from models import pathogen
from controllers import savequery

#Set word_count_site_name
newpathv = Blueprint('newpathv', __name__)

# Create newpathogen
@newpathv.route('/newpathogen', methods=['GET', 'POST'])
def newpathogen():
    if request.method == 'GET':
        # send the form
        return render_template('cud.html')
    else: # request.method == 'POST':
        # read data from the form and save in variable
        organism = request.form['organism']
        taxonid = request.form['taxonid']
        rank = request.form['rank']
        gram = request.form['gram']
        aerobe = request.form['aerobe']
        habitat = request.form['habitat']
        isolation = request.form['isolation']
        pathostate = request.form['pathostate']

        try:
            if savequery.check_if_pathogen_exist(organism, taxonid)== True:
                return render_template('newpawarning.html', data=organism)
            else:
                savequery.save_changes(organism, taxonid, rank, gram, aerobe, habitat, isolation, pathostate)
                return render_template('newpasuccess.html')
        except:
            return render_template('newpafailed.html')