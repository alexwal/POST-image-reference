from flask import Flask, request, Response
import json
import numpy as np
import io
from PIL import Image

# Initialize the Flask application
app = Flask(__name__)

# route http posts to this method
@app.route('/api/test', methods=['POST'])
def test():
    image_bytes = io.BytesIO(request.data)
    img = Image.open(image_bytes)
    response = {'message': 'image received. size={}x{}'.format(img.size[0], img.size[1])}
    response = json.dumps(response)
    return Response(response=response, status=200, mimetype='application/json')

# start flask app
app.run(host='0.0.0.0', port=5000, debug=True)

