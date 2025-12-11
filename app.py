from flask import Flask, jsonify, send_from_directory
import os

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, World!"

@app.route("/api/health")
def health():
    return jsonify(status="ok")

@app.route('/files/<path:filename>')
def download_file(filename):
    directory = os.path.join(app.root_path, 'files')
    return send_from_directory(directory, filename, as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)