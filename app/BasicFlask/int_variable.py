from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
   return "Hello World!"

@app.route("/hi/<int:myVal>")
def hello_val(myVal):
   return "Hello %d " %myVal

@app.route("/hi/<float:myVal>")
def hello_fval(myVal):
   return "Hello %f " %myVal

if __name__ == "__main__":
   app.run(debug = True)
