from flask import * 
from flask import Flask
from flask import request
from src.server.pre_annotate import predict_yaw
from os import path

app = Flask(__name__)



@app.route("/predict_rotation", methods=['POST'])
def get_autoLabel():
    rot = predict_yaw(request.json['points'])
    return {
        'x': rot[0],
        'y': rot[1],
        'z': rot[2]
    }

@app.route("/save_annotations", methods=['POST'])
def save_annotations():
    data = request.json

    for i in range(len(data['annotationFiles'])):
        filePath = path.join('input', data['dataset'], data['sequence'], 'annotations', data['fileNames'][i])
        with open(filePath, 'w') as f:
            f.write(data['annotationFiles'][i])

    return {
        'status': 'success'
    }




if __name__ == "__main__":
    app.run(debug=True)

