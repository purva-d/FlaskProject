from flask import Flask , render_template
app = Flask(__name__)

@app.route("/")
def index():
   Name="Dhiraj"
   myDict={"Daniel":"Beautiful day in Paris!","Amar":"Come and meet me soon"}
   return render_template('ans.html', name=Name,msgDict= myDict)

if __name__ == "__main__":
   app.run(debug = True)
