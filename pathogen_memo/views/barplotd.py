from flask import Flask,jsonify, Blueprint, render_template
from sys import version

import matplotlib.pyplot as plt
import numpy as np

from io import BytesIO
import base64
from flask_login import login_required
from pathogen_memo.controllers import distinctcounting


#Set word_count_site_name
barplotdv = Blueprint('barplotdv', __name__)

def get_habitats_name(habitat_dblist):
    hab_name_list=[]
    for hab in habitat_dblist:
        hab_name_list.append(hab[0])
    return hab_name_list

def get_habitats_counts(habitat_dblist):
    hab_count_list=[]
    for habc in habitat_dblist:
        hab_count_list.append(habc[1])
    return hab_count_list

@barplotdv.route('/dashboard', methods=['GET'])
@login_required
def barplotd():
    gethabitats = distinctcounting.get_distinct_queries_count()
    print("get habitats:",gethabitats)
    print("get habitats names:", get_habitats_name(gethabitats))
    print("get habitats counts:", get_habitats_counts(gethabitats))

    
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    ax.axis('equal')
    #habitats = ['Human(Childhood)', 'Human(intestinal tract)', 'Aquatic environments', 'Human - Animal - Plant', 'NA']
    habitats = get_habitats_name(gethabitats)
    #counthab = [1,1,1,2,5]
    counthab = get_habitats_counts(gethabitats)

    ax.pie(counthab, labels = habitats,autopct='%1.2f%%')
    plt.show()

    plt.savefig('static/img/barplotd.png', ext='png', bbox_inches="tight")
    return render_template('dashboard.html', url='/static/img/barplotd.png')