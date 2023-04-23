from flask import Flask, render_template, request
app = Flask(__name__,template_folder='templates')
app.debug = True

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "GET":
        return render_template("file_input.html")
    else:
        x=[]
        file = request.files['file']
        # Open the file for reading
        with open(file.filename, 'r') as f:
            # Read data from the file
            file_data = f.read()
            # Do something with the file data
            x.append(file_data)
            print(x)
            return render_template('tp', data=x)
        
    
