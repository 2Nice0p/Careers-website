from flask import Flask, render_template, jsonify

#from flask module we are using the Flask class

app = Flask(__name__)        #creating an instance of the Flask class
                             #app is an object name and the __name__ is inbulit name ........ use -  print(__name__) to check


#this is templeting syntax provided by flask as i can access the things from app file and use the below info in job opening in home.html
JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 10,00,000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Delhi, India',
    'salary': 'Rs. 15,00,000'
  },
  {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote',
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'San Francisco, USA',
    'salary': '$150,000'
  }
]

@app.route("/")              #creating a route for the app and @ is decorator
def hello_world():           #creating a function
  return render_template('home.html',jobs=JOBS)


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
  