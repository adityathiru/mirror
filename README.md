# M.I.R.R.O.R
## _Most Instantaneous Reproducible Research On 'Roids_
Setting up the necessary packages, frameworks and drivers for your research work can be time consuming and many a times tedious. Packages could fail to install or searching for every single command and running them 1 by 1 takes away your precious time!

What if there was a way to just select all the frameworks, pacakges and drivers you need and you are good to go with a complete full-fleged IDE or Jupyter Notebook to complement you ?

What if there was a way to easily share a fully reproducible research work with your colleagues in a single small file ?   

Fully driven by the best practices in Docker - without having to know its nuances! :)

**That's what we intend to make as a reality!**


### Development
**If you are interested in contributing to this project:**
- You are expected to have `docker` and `docker-compose` running on your local system
- The server development server instantiates the webapp and elk stack (credits to [deviantony/docker-elk](https://github.com/deviantony/docker-elk/tree/x-pack))
- Execute `./deploy_local.sh` for getting all your containers up and running
- To run tests: `python webapp/tests/tests.py`

**Issues and PRs are welcome! :)**

### Deployment
**If you wish to setup the project locally on your own servers:**
- To bring up all the servers: `docker-compose -f docker-compose-prod.yml up`
- This instantiates the webapp, elk stack for monitoring and sets up nginx
