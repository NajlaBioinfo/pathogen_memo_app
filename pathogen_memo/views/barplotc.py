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
barplotcv = Blueprint('barplotcv', __name__)

@barplotcv.route('/dashboard', methods=['GET'])
@login_required
def barplotc():
    p1 = countbyquery.get_query_count('pathostate', 'Non Pathogen')
    p2 = countbyquery.get_query_count('pathostate', 'Potential Pathogen')
    p3 = countbyquery.get_query_count('pathostate', 'Pathogen')
    p4 = countbyquery.get_query_count('pathostate', 'NA')

    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    colors = ['Non Pathogen', 'Potential Pathogen','Pathogen', 'NA']
    pathomemb = [p1,p2,p3,p4]
    tick_label = ['Non Pathogen', 'Potential Pathogen','Pathogen', 'NA']
    ax.bar(colors,pathomemb, tick_label=tick_label, width=0.8, color=['bisque','lightcoral','firebrick','gray'])
    # naming the y-axis
    plt.ylabel('Pathogens - Counts')
    # naming the x-axis
    plt.xlabel('Pathogens categories')
    # plot title
    plt.rc('legend',fontsize=35) 
    plt.title('Pathogen categories counts')
    

    plt.show()

    filePath = 'static/img/barplotc.png'
    if os.path.exists(filePath):
        os.remove(filePath)
    plt.savefig(filePath, ext='png', bbox_inches="tight")
    return render_template('dashboard.html', url='/static/img/barplotc.png')
