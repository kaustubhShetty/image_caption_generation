import os
from PIL import Image
import io
from flask import Flask,Blueprint,request,render_template,jsonify,Response,send_file
import jsonpickle
import numpy as np
import json
import base64
import generate_caption as gc

app = Flask(__name__)
static_dir='images/'

@app.route('/api', methods=['GET','POST'])
def apiHome():
    r = request.method
    if(r=="GET"):
        with open("text/data.json") as f:
            data=json.load(f)
        print(data)
        return data
    elif(r=='POST'):
        with open(static_dir+'sample.jpg',"wb") as fh:
            fh.write(base64.decodebytes(request.data))
        captions=gc.generate_captions(static_dir+'sample.jpg')
        cap={"captions":captions}
        with open("text/data.json","w") as fjson:
                    json.dump(cap,fjson)
        return captions
    else:
        return jsonify({
        "captions":"Refresh again !"
        })  

@app.route('/result')
def sendImage():
    return send_file(static_dir+'sample.jpg',mimetype='image/gif')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)