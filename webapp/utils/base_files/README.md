# Project M.I.R.R.O.R
> Most Instantaneous Reproducible Research On 'Roids

Setting up the necessary packages, frameworks, and drivers for your research work can be time-consuming and tedious. Packages could fail to install or searching for every single command and running them 1 by 1 takes away your precious time!

What if there was a way to just select all the frameworks, packages and drivers you need and you are good to go with a complete full-fledged editor like VSCode or Jupyter Notebook to compliment you?

What if you could easily share fully reproducible research work with your colleagues in a single small file?

**That's what we intend to make as a reality!**

Fully driven by the best practices in Docker - without having to know its nuances! :)

## setting up your project
- assuming you had set the project name as imagenet_training
- cd imagenet_training

### prerequisites
- setup docker and coker-compose if you don't have already (automated scripts coming soon!)
  - docker setup :
    - for ubuntu :
      - execute : `./install_docker.sh`
      - or refer : https://docs.docker.com/install/linux/docker-ce/ubuntu/
    - for macos : https://docs.docker.com/docker-for-mac/install/
  - docker-compose setup :
    - for ubuntu :
      - execute : `./install_docker-compose.sh`
    - for macos :
      - already comes along with docker!
    - refer : https://docs.docker.com/compose/install/

### now you have all the prerequisites - setting up your project is as simple as `./imagenet_training`
- when starting the very first time: `./imagenet_training all` :
  - first install takes quite a bit of time - post that, things should load up in a jiffy!
  - you should get a shell with all your packages installed
  - vscode will be running on ipaddress:8443 (ipaddress = localhost when running on personal computer)
  - jupyter will be running on ipaddress:8888 (ipaddress = localhost when running on personal computer)
  - you can also edit in your own favourite editor and execute the files inside the container too!
- to stop the container : `./imagenet_training stop`
- to kill the container : `./imagenet_training kill`
- to start a stopped/killed container : `./imagenet_training up`
- to start a stopped/killed container in the background and get a shell : `./imagenet_training upd`
- NOTE:
  - killing the containers will reset the any packages installed by you manually on the container whereas stop will retain them
  - your project file path won't get deleted when killing and all the changes will be saved as long as you save them ;)
  - to change your project path :
    - go to docker-compose.yml and you'll be able to see the project path you set in volumes section
    - there, specify what your new project path is (specify an actual absolute path in your system)
    - execute `./imagenet_training build` to rebuild
  - to add more python libraries to requirements:
    - add the name of the python package to `requirements.txt` and execute `./imagenet_training build` to rebuild