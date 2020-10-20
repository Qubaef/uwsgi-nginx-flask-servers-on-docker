# Intial file of the program to setup container with shared volume to develop app
import os

# Pull image of uwsgi nginx flask server
print("===RUN: docker pull tiangolo/uwsgi-nginx-flask:")
os.system("docker pull tiangolo/uwsgi-nginx-flask")

# Build docker image basing on Dockerfile present in current location  
print("===RUN: docker build -t uwsgi-nginx-flax-webapp .")
os.system("docker build -t uwsgi-nginx-flax-webapp .")

# Create network for docker
network_name = "webapp_net"
print(f"===Run network called {network_name}")
os.system(f"docker network create {network_name}")

# Run two containers of docker image, and set them up on two different ports
name1 = "uwsgi-nginx-flax-webapp-dev"
port1 = 56763
dir = os.getcwd() + "/webapp"

# Run instance:
print(f"===Run instance of container with name: {name1} on port {port1}")
os.system(f"docker run -v {dir}:/app -dit --name {name1} -p {port1}:80 uwsgi-nginx-flax-webapp")

# Connect instance to the network:
print(f"===Connect {name1} to {network_name}")
os.system(f"docker network connect {network_name} {name1}")

print("===Finished")