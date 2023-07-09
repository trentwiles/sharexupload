from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
  return "MISS"

@app.route('/', methods=['POST'])
def upload_file():
    file = request.files['file']
    file.save('/var/www/html/trentwil.es/a/' + file.filename)  # Save the file to a desired location
    return 'File uploaded successfully!'

if __name__ == '__main__':
    app.run(port=6565)
