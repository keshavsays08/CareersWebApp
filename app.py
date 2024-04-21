# from module flask import class Flask 
from flask import Flask, render_template,jsonify

# app is nothing but the object of the class Flask
app = Flask(__name__)
# when you create a flask app or instantiate Flask class you require a name of variable here it is __name__

JOBS = [
  {
    'id':1,
    'title': 'Data Analyst',
    'location':'Bangaluru, IN',
    'salary':'$70,000'
  },
  {
    'id':1,
    'title': 'Data Scientist',
    'location':'Delhi, IN',
    'salary':'$120,000'
  },
  {
    'id':1,
    'title': 'Data Engineer',
    'location':'Remote',
    'salary':'$95,000'
  },
  {
    'id':1,
    'title': 'Full Stack Engineer',
    'location':'San Francisco, USA',
    'salary':'$120,000'
  },
]

@app.route("/")
def hello_world():
  return render_template('index.html',
                         jobs=JOBS)
# when you create a route you require a decorator which is @app.route("/")

# created a json doc
@app.route("/api/jobs")
def jobs_json_api():
  return jsonify(JOBS)

# 2nd way of running the flask web-app
# if this script is invoked it will the flask web-app
if __name__ == "__main__":
  # serve(app, host='0.0.0.0', port=8080, threads=4)

  # By default there are 4 threads in the flask web-app  
  # it require two arguments first the host port and debug=True (it will enable the debug mode and updates the web-app automatically))
  # this below line is the way of running the flask web-app generally but due to some development reasons it is not working
  app.run(host="0.0.0.0", port=8080, debug=True)

# PROBLEM-1 
# this is a development server. do not use it in a production deployment 

# SOLUTION-1
# what is WSGI(Web Server Gateway Interface)
# WSGI is a standard interface for web servers to communicate with web applications.

# Why use waitress
# 1. The default flask server is not production ready it is single-threaded and does not support multiple requests at the same time
# 2. Waitress is a production ready server that supports multiple requests at the same time
# 3. It is a pure python server that is lightweight and fast


