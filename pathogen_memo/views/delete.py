from flask import Blueprint, render_template, redirect, request
from sys import version
from flask import Flask, jsonify

from pathogen_memo.forms import pathogen_updateform

from pathogen_memo.controllers import updatequery
from pathogen_memo.controllers import getallquery
from pathogen_memo.controllers import deletequery


from flask_login import login_required
from flask_login import current_user

#Set word_count_site_name
deletev = Blueprint('deletev', __name__)

@deletev.route('/delete')
@login_required
def delete():
    """Serve logged in Delete."""
    tablename = 'pathogens'
    data_update = getallquery.gethemall(tablename)
    return render_template('delete.html',
                            current_user=current_user,
                            data=data_update)


# Delete pathogenfile
@deletev.route('/deletebyid', methods=['GET', 'POST'])
def deletebyid():
    form = pathogen_updateform.PathogenUpdateForm(request.form)
    idapath = request.form.get("idtodelete")
    print("idapath:",idapath)
    try:
        mapped_data = updatequery.get_query_by_id(idapath)
        print(mapped_data)
        return render_template('deletebyid.html', data=mapped_data, form= form)
        
    except Exception as e:
        print("Couldn't load data")
        print(e)
        return render_template('newpafailed.html')


# Delete pathogenfile
@deletev.route('/deletepatho', methods=['GET', 'POST'])
def deleteepatho():
    if request.method == 'GET':
        # send the form
        return render_template('deletebyid.html')
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
            print("Record deleted: ", id, organism, taxonid, rank, gram, aerobe, habitat, isolation, pathostate)
            deletequery.delete_query_by_id(id)
            return render_template('deletepatho.html')
        except:
            return render_template('newpafailed.html')