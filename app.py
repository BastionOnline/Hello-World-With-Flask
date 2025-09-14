from flask import Flask, render_template
import webbrowser
import threading

app = Flask(__name__)   #  Create a Flask app instance

@app.route('/')
def hello_world():
    return render_template('index.html') # Render the HTML template


def open_browser():
    webbrowser.open_new("http://127.0.0.1:8000/")

if __name__ == '__main__':  # Run the app
    threading.Thread(target=open_browser).start()
    app.run(port=8000) # Enable debug mode for development


# Packaging with PyInstaller
# create pyinstaller --onefile myAppName.py

# edit newly created .spec file with either:
#   datas=[('templates', 'templates')],
#   datas=[('templates', 'templates'), ('static', 'static')],

# run
# pyinstaller nameOfFile.spec