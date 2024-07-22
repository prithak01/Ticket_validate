from flask import Flask, request, jsonify
# from flask_cors import CORS
from config import config
from ocr_module import perform_ocr
from ticket_validator import validate_ticket
from utils.file_utils import allowed_file
# from utils.image_utils import read_image
from text_parser import parse_ticket_data 
import os
from werkzeug.utils import secure_filename
from PIL import Image # Import the Image module from Pillow
import io # Import io for handling in-memory file operations

app = Flask(__name__)
#app.config['UPLOAD_FOLDER'] = config.UPLOAD_FOLDER

@app.route('/validate', methods=['POST'])
def validate():
    if 'image' not in request.files:
        return jsonify({"error": "No image file provided"}), 400
    file = request.files['image']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    if file and allowed_file(file.filename, config.ALLOWED_EXTENSIONS):
        #filepath = save_file(file, app.config['UPLOAD_FOLDER']) 
        #image = read_image(filepath)
        image = Image.open(io.BytesIO(file.read()))
        extracted_text = perform_ocr(image)
        ticket_data = parse_ticket_data(extracted_text)  # Use the moved function
        uts_no = ticket_data.get('uts_no')
        if uts_no:
            # Append the UTS number to a file
            with open('uts_numbers.txt', 'a') as f:
                f.write(f"{uts_no}\n")

        validation_result = validate_ticket(ticket_data)
        response = {
            "validation_result": validation_result,
            "extracted_text": extracted_text,
            "UTS No.": uts_no
        }
        return jsonify(response)
    else:
        return jsonify({"error": "Invalid file type"}), 400

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "OK"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
