from flask import Flask, render_template,request
import time
from inference import get_species



app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def hello():
    species_name = ""
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        user_inputs = request.form.to_dict()
        #print(request.form.to_dict())
        ready = False
        species_name = get_species(user_inputs)
        ready=True
        
        #return redirect(url_for("name"))
        return render_template("index.html", prediction=species_name, ready=ready)

    
if __name__ == "__main__":
    app.run(port=80, host="0.0.0.0", debug=True)