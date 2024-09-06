from flask import Flask, request, jsonify
import socket
import json

# Create the Flask app
app = Flask(__name__)

# IP list to store added IPs
ips = []

# Add IP address to the list
@app.route('/add', methods=['POST'])
def add_ip():
    ip = request.json.get('ip')
    if ip and ip not in ips:
        ips.append(ip)
        return jsonify({"status": "success", "message": f"IP {ip} added successfully"}), 201
    return jsonify({"status": "fail", "message": "Invalid or existing IP"}), 400

# Get the list of stored IP addresses
@app.route('/get', methods=['GET'])
def get_ips():
    return jsonify({"ips": ips})

# Remove an IP address from the list
@app.route('/remove', methods=['DELETE'])
def remove_ip():
    ip = request.json.get('ip')
    if ip in ips:
        ips.remove(ip)
        return jsonify({"status": "success", "message": f"IP {ip} removed successfully"}), 200
    return jsonify({"status": "fail", "message": "IP not found"}), 404

# Catch all other requests to show available routes
@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "Welcome to the IP manager API.",
        "routes": ["/add (POST)", "/get (GET)", "/remove (DELETE)"]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
