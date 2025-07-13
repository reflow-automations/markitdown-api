from flask import Flask, request, jsonify
import markdownify
import os
import tempfile

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert_to_markdown():
    if 'file' not in request.files:
        return jsonify({"error": "Geen bestand meegegeven"}), 400

    uploaded_file = request.files['file']
    if uploaded_file.filename == '':
        return jsonify({"error": "Leeg bestandsveld"}), 400

    # Tijdelijk opslaan
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        uploaded_path = tmp_file.name
        uploaded_file.save(uploaded_path)

    try:
        # Detecteer bestandstype
        ext = os.path.splitext(uploaded_file.filename)[1].lower()

        if ext in ['.txt', '.md']:
            with open(uploaded_path, 'r', encoding='utf-8') as f:
                content = f.read()
            markdown = content

        elif ext in ['.html', '.htm']:
            with open(uploaded_path, 'r', encoding='utf-8') as f:
                html = f.read()
            markdown = markdownify.markdownify(html)

        else:
            # Alles anders → stuur door naar MarkItDown core CLI-tool (later geavanceerd maken)
            result = os.popen(f"markitdown \"{uploaded_path}\"").read()
            markdown = result

        return jsonify({"markdown": markdown})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        os.remove(uploaded_path)

@app.route('/', methods=['GET'])
def home():
    return "MarkItDown API is running."

if
