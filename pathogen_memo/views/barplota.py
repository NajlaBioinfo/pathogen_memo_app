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
barplotav = Blueprint('barplotav', __name__)


@barplotav.route('/dashboard', methods=['GET'])
@login_required
def barplota():
    gramnegcount = countbyquery.get_query_count('gram', 'Gram-negative')
    gramposcount = countbyquery.get_query_count('gram', 'Gram-positive')
    gramnacount = countbyquery.get_query_count('gram', 'NA')

    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    colors = ['Gram-positive', 'Gram-negative', 'NA']
    pathomemb = [gramposcount,gramnegcount,gramnacount]
    tick_label = ['Gram+', 'Gram-', 'NA']
    ax.bar(colors,pathomemb, tick_label=tick_label, width=0.8, color=['purple', 'pink','gray'])
    # naming the y-axis
    plt.ylabel('Pathogens - Counts')
    # naming the x-axis
    plt.xlabel('Pathogens categories')
    # plot title
    plt.rc('legend',fontsize=35) 
    plt.title('Gram-negative/Gram-positive counts')
    

    plt.show()

    filePath = 'static/img/barplota.png'
    if os.path.exists(filePath):
        os.remove(filePath)
    plt.savefig(filePath, ext='png', bbox_inches="tight")
    return render_template('dashboard.html', url='/static/img/barplota.png')
