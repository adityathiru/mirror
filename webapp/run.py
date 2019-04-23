from webapp.api import app
from webapp.webserver import run_server

if __name__ == "__main__":
    run_server(app, host='0.0.0.0', port=8000, debug=True)
