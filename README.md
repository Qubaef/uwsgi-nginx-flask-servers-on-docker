# uwsgi-nginx-flask-servers-on-docker
## Usage
Project's setup scripts were writtern for Windows. Using them on Linux systems may require manual setup. To run the project on Windows with installed docker client:
- Pull repository to workspace.
- To run two containers connected by internal network, run:
   `./setup.py`
- To run one container, but with usage of shared volume to peform live changes, run:
   `./setup_dev.py`
   In such case, `/webbapp` directory will be shared on the server.
   
- Setup script should pull the original server image from docker hub repository, then build it and run two instances.
- In some cases, error with ports might occur. In such case it is required to change port values in the setup file to those that are not excluded. You can see excluded ranges using this instruction (different every reboot): 
    `netsh interface ipv4 show excludedportrange protocol=tcp`
