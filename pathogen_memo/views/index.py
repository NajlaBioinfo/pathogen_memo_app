from flask import Blueprint, render_template
from sys import version
from flask import Flask, jsonify



from controllers import getallquery


#Set word_count_site_name
indexv = Blueprint('indexv', __name__)

@indexv.route('/')
def index():
  tablename = 'pathogens'
  data_index = getallquery.gethemall(tablename)
  #print (data_index)


  #return jsonify({"message": "Welcome to my Flask App"})
  #return render_template('index.html',message="Welcome to my Flask App")

  return render_template('index.html', data=data_index)
