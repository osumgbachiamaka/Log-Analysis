from flask import Flask, render_template
from database import get_views

app = Flask(__name__)

@app.route('/')
def index():
   most_viewers = get_views()
   return render_template('index.html', results = most_viewers)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000)