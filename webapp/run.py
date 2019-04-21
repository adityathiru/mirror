from webapp.api import app
from webapp.api import views

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
