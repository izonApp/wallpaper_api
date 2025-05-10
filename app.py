# app.py
import os
from flask import Flask, request, jsonify
from wallpapers_data import wallpapers

app = Flask(__name__)

@app.route("/get_wallpapers", methods=["POST"])
def get_wallpapers():
    return jsonify({"status": True, "data": wallpapers})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=True)
