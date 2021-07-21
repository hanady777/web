from flask import Flask, request, render_template,jsonify , session
import nltk
import numpy as np
import copy
import pandas as pd
import sklearn
from preprocessing import df_wo_actors_details,df_names,df_tracks,df_artists
from descriptor import Descriptor,isinbase

app = Flask(__name__)
app.secret_key="Pres6"

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')



@app.route('/preproc', methods=["GET"])
def pre_process():
    return render_template('preproc.html')


@app.route('/knowledge_level', methods=["GET", "POST"])
def knowledge_level_case():
    print('oupsi')
    text1 = request.form['text']
    word = text1.lower()
    session["knowledge_level"]= int(text1)
    result = {
        "result": word
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)

@app.route('/minimum_length_description', methods=["GET", "POST"])
def minimum_length_description_case():
    text1 = request.form['text']
    word = text1.lower()
    session["minimum_length_description"]= int(text1)
    result = {
        "result": word
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)


@app.route('/isinbase', methods=["GET", "POST"])
def isinbase_case():
    print('oupsi')
    text1 = request.form['text']
    word = isinbase(text1.lower(),df_wo_actors_details,df_names,df_tracks,df_artists)
    print("word",word)
    result = {
        "result": word
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)

@app.route('/describe', methods=["GET", "POST"])
def describe_case():
    text1 = request.form['text']
    
    if "knowledge_level" in session:
        knowledge_level=int(session["knowledge_level"])
    else:
        knowledge_level=6

    if "minimum_length_description" in session:
        minimum_length_description=int(session["minimum_length_description"])
    else:
        minimum_length_description=4


    if "context" in session:
        context=session["context"]
        session["context"]=session["context"]+text1.lower()+','
    else:
        context=""
        session["context"]=""
        session["context"]=session["context"]+text1.lower()+','

    context_list=context.split(",")   
    context_list.reverse()
    context_list=context_list[1::]

    print('contexte',context_list,knowledge_level,minimum_length_description)

    word=Descriptor(text1,df_wo_actors_details,df_names,df_tracks,df_artists,context=context_list,max_complexity= knowledge_level,min_length_description=minimum_length_description).complexity()
    result = {
        "result": word
    }
    result = {str(key): value for key, value in result.items()}

    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)

