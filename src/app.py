from flask import Flask
from app import app

def test_home():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert response.data == b"Hello, Jenkins!"

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Jenkins!"

if __name__ == '__main__':
    app.run(debug=True)
