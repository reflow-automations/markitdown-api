from flask import Flask, request, jsonify
from markitdown import convert_file  # zorg dat dit klopt met jouw import

app = Flask(__name__)

@app.route("/")
def health():
    return "MarkItDown API is running.", 200

@app.route("/convert", methods=["POST"])
def convert():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    try:
        markdown = convert_file(file)
        return jsonify({"markdown": markdown})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
