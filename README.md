# M.I.R.R.O.R
> Most Instantaneous Reproducible Research On 'Roids

Setting up the necessary packages, frameworks, and drivers for your research work can be time-consuming and tedious. Packages could fail to install or searching for every single command and running them 1 by 1 takes away your precious time!

What if there was a way to just select all the frameworks, packages and drivers you need and you are good to go with a complete full-fledged editor like VSCode or Jupyter Notebook to compliment you?

What if you could easily share fully reproducible research work with your colleagues in a single small file?

**That's what we intend to make as a reality!**

Fully driven by the best practices in Docker - without having to know its nuances! :)


### Development
**If you are interested in contributing to this project:**
- You are expected to have `docker` and `docker-compose` running on your local system
- The server development server instantiates the webapp and elk stack (credits to [deviantony/docker-elk](https://github.com/deviantony/docker-elk/tree/x-pack))
- Set up environment variables using `direnv`:
  - For Ubuntu: `sudo apt install direnv`
  - For MacOS: `brew install direnv`
  - Hook up your shell using: `direnv hook $SHELL`
  - Enable the environment variables using: `direnv allow .`
- Execute `./deploy_local.sh` for getting all your containers up and running
- To run tests: `python webapp/tests/tests.py`

**Issues and PRs are welcome! :)**


### Deployment
**If you wish to setup the project locally on your own servers:**
- To bring up all the servers: `docker-compose -f docker-compose-prod.yml up`
- This instantiates the webapp, elk stack for monitoring and sets up nginx
