from flask import Flask,jsonify, Blueprint, render_template
from sys import version
import numpy
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from flask_login import login_required

import os 
from pathogen_memo.controllers import countbyquery

#Set word_count_site_name
barplotbv = Blueprint('barplotbv', __name__)

@barplotbv.route('/dashboard', methods=['GET'])
@login_required
def barplotb():
    a1 = countbyquery.get_query_count('aerobe', 'Aerobic')
    a2 = countbyquery.get_query_count('aerobe', 'Aerophilic')
    a3 = countbyquery.get_query_count('aerobe', 'Anaerobic')
    a4 = countbyquery.get_query_count('aerobe', 'Facultative Anaerobic')
    a5 = countbyquery.get_query_count('aerobe', 'NA')

    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    colors = ['Aerobic', 'Aerophilic','Anaerobic', 'Facultative Anaerobic', 'NA']
    pathomemb = [a1,a2,a3,a4,a5]
    tick_label = ['Aerobic', 'Aerophilic','Anaerobic', 'Facultative Anaerobic', 'NA']
    ax.bar(colors,pathomemb, tick_label=tick_label, width=0.8, color=['navy','blue','cyan','lightcyan','gray'])
    # naming the y-axis
    plt.ylabel('Pathogens - Counts')
    # naming the x-axis
    plt.xlabel('Pathogens categories')
    # plot title
    plt.rc('legend',fontsize=35) 
    plt.title('Aerobe categories counts')
    

    plt.show()

    filePath = 'pathogen_memo/static/img/barplotb.png'
    if os.path.exists(filePath):
        os.remove(filePath)
    plt.savefig(filePath, ext='png', bbox_inches="tight")
    return render_template('dashboard.html', url='/static/img/barplotb.png')
