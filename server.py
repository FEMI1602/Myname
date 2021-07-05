import base64
import requests
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html')

@app.route('/my-link/')
def my_link():
  print ('I got clicked!')
  url = 'https://api.github.com/repos/FEMI1602/mashithandu/contents/blackboard/addName.txt'
  req = requests.get(url)
  if req.status_code == requests.codes.ok:
       req = req.json()
       content = base64.b64decode(req['content'])
       print(content)

  return content

if __name__ == '__main__':
  app.run(debug=True)