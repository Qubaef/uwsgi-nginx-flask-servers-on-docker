from app import app
from flask import request, redirect, url_for, jsonify
from flask import render_template
import requests
import os

from .service import ChatService
from .models import Schema

# Initialize db schema
Schema()

def get_ip_addr():
    # Create file with ip
    os.system("/sbin/ifconfig eth1 | grep 'inet addr' | cut -d: -f2 | awk '{print $1}' > ip.txt")
    
    # Read ip
    f = open("ip.txt", "r")
    ip_address = f.read()
    f.close()

    return ip_address

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/ip")
def get_ip():
    return "Requester IP: " + str(get_ip_addr())


@app.route("/chat/send", methods=["GET", "POST"])
def message_send():
    if request.method == 'POST':
        print(f"Sending: {(request.form.get('message'))} to: {request.form.get('adress')}")
        # Send post request to given adress, containing message and referer ip
        requests.post(f"http://{request.form.get('adress')}/chat", {'message': request.form.get('message'), 'referer': get_ip_addr()})
    return render_template("msg-send.html")


@app.route("/chat", methods=["GET"])
def message_list():
    return jsonify(ChatService().list())


@app.route("/chat", methods=["POST"])
def message_create():
    print("Received " + str(request.form))
    return jsonify(ChatService().create(request.form))


@app.route("/chat/<id>", methods=["DELETE"])
def message_delete(id):
    return jsonify(ChatService().delete(id))