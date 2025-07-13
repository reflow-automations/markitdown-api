from flask import Flask, request, jsonify
from markitdown import MarkItDown
import tempfile
import os

app = Flask(__name__)
md = MarkItDown(enable_plugins=False)

@app.route("/convert", methods=["POST"])
def convert_file():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    uploaded_file = request.files["file"]
    if uploaded_file.filename == "":
        return jsonify({"error": "Empty filename"}), 400

    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        uploaded_file.save(temp_file.name)
        result = md.convert(temp_file.name)
        os.unlink(temp_file.name)

    return jsonify({"markdown": result.text_content})
