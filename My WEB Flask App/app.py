from flask import Flask
import redis

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379)

@app.route('/')
def hello():
    return "Welcome to Abbas Web Page !"

@app.route('/count')
def count():
    r.incr('visits')
    visit_count = r.get('visits').decode('utf-8')
    return f"This page has been visited {visit_count} times."

# 👇 THIS IS CRUCIAL: It keeps Flask running on port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
