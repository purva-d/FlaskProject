from flask import Flask , render_template
app = Flask(__name__)

@app.route("/")
def index():
   Name="Python Flask workshop"
   myLst=[12,43,66,87,90,32,1,9]
   myTuple=(3,4,67,33,21,12)
   return render_template('tmp.html', name=Name,tpl=myTuple, lst=myLst)

@app.route("/table")
def display():
   myDict={"a1":1,"a2":2,"a3":3,"a4":4,"a5":5,"a6":6,"a7":7}
   return render_template('result.html', dict= myDict)

if __name__ == "__main__":
   app.run(debug = True)
