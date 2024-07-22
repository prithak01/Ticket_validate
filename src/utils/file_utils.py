import os
from werkzeug.utils import secure_filename

def allowed_file(filename, allowed_extensions):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

# def save_file(file, upload_folder):
#     filename = secure_filename(file.filename)
#     filepath = os.path.join(upload_folder, filename)
#     file.save(filepath)
#     return filepath
