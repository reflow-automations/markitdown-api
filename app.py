from flask import Flask, request, jsonify
from markitdown import MarkItDown
import tempfile, os

app = Flask(__name__)
md = MarkItDown(enable_plugins=False)   # zet op True als je later plugins aanzet

@app.route("/", methods=["GET"])
def health():
    """Eenvoudige health-check voor Coolify (‘/’ moet 200 OK geven)."""
    return "MarkItDown API is running.", 200

@app.route("/convert", methods=["POST"])
def convert():
    """Ontvang één bestand (multipart/form-data, key = file) en geef Markdown terug."""
    if "file" not in request.files:
        return jsonify({"error": "No file provided, use form-data key ‘file’"}), 400

    up = request.files["file"]
    if up.filename == "":
        return jsonify({"error": "Empty filename"}), 400

    # Sla het even op in /tmp zodat MarkItDown het kan lezen
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        up.save(tmp.name)
        tmp_path = tmp.name

    try:
        result = md.convert(tmp_path)          # MarkItDown doet alle type-detectie ✨
        markdown_text = result.text_content
        return jsonify({"markdown": markdown_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        os.remove(tmp_path)                    # altijd opruimen
