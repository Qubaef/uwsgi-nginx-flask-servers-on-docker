# Intial file of the program to setup 2 containers from the scratch
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
name1 = "uwsgi-nginx-flax-webapp-1"
port1 = 56763

name2 = "uwsgi-nginx-flax-webapp-2"
port2 = 56764

# Run first instance:
print(f"===Run first instance of container with name: {name1} on port {port1}")
os.system(f"docker run -dit --name {name1} -p {port1}:80 uwsgi-nginx-flax-webapp")

# Run second instance:
print(f"===Run first instance of container with name: {name2} on port {port2}")
os.system(f"docker run -dit --name {name2} -p {port2}:80 uwsgi-nginx-flax-webapp")

# Connect first instance to the network:
print(f"===Connect {name1} to {network_name}")
os.system(f"docker network connect {network_name} {name1}")

# Connect second instance to the network:
print(f"===Connect {name2} to {network_name}")
os.system(f"docker network connect {network_name} {name2}")

print("===Finished")