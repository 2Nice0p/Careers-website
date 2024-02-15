from flask import Flask       #from flask module we are using the Flask class

app = Flask(__name__)        #creating an instance of the Flask class
                             #app is an object name and the __name__ is inbulit name ........ use -  print(__name__) to check

@app.route("/")              #creating a route for the app and @ is decorator

def hello_world():           #creating a function
  return "Hello JaanMan"

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
  