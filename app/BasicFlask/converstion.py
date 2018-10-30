from flask import Flask , render_template
app = Flask(__name__)

@app.route("/")
def index():
   user={'username':"Dhiraj"}
   posts= [
      {
         "author":{'username':'Daniel'},
         "body": "Beautiful day in Paris!"
       },
      {
         "author":{'username':'Amar'},
         "body": "Come and meet me soon!"
         }
      ]
         
            

   return render_template('ans1.html', user=user, posts=posts)

if __name__ == "__main__":
   app.run(debug = True)
