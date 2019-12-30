from flask import Blueprint, render_template, redirect, request
from sys import version
from flask import Flask, jsonify

from pathogen_memo.forms import pathogen_updateform

from pathogen_memo.controllers import updatequery
from pathogen_memo.controllers import getallquery


#Set word_count_site_name
updatev = Blueprint('updatev', __name__)

@updatev.route('/update')
def update():
  tablename = 'pathogens'
  data_update = getallquery.gethemall(tablename)
  return render_template('update.html', data=data_update)



# Update pathogenfile
@updatev.route('/updatebyid', methods=['GET', 'POST'])
def updatebyid():
    form = pathogen_updateform.PathogenUpdateForm(request.form)
    idapth = request.form.get("idtoupdate")
    try:
        mapped_data = updatequery.get_query_by_id(idapth)
        print(mapped_data)
        return render_template('updatebyid.html', data=mapped_data, form= form)
        
    except Exception as e:
        print("Couldn't load data")
        print(e)
        return render_template('newpafailed.html')


# Update pathogenfile
@updatev.route('/updatepatho', methods=['GET', 'POST'])
def updatepatho():
    if request.method == 'GET':
        # send the form
        return render_template('updatebyid.html')
    else: # request.method == 'POST':
        # read data from the form and save in variable
        id =request.form['id']
        organism = request.form['organism']
        taxonid = request.form['taxonid']
        rank = request.form['rank']
        gram = request.form['gram']
        aerobe = request.form['aerobe']
        habitat = request.form['habitat']
        isolation = request.form['isolation']
        pathostate = request.form['pathostate']

        try:
            print(id, organism, taxonid, rank, gram, aerobe, habitat, isolation, pathostate)
            updatequery.update_query_by_id(id, organism, taxonid, rank, gram, aerobe, habitat, isolation, pathostate)       
            return render_template('updatedpatho.html')
        except:
            return render_template('newpafailed.html')