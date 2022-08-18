import os
import subprocess
import rp


from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    
    return render_template('index.html')

@app.route("/dns", methods = ['GET', 'POST'])
def page():

    address = None

    if request.method == 'POST':
        address = request.form['address']
        cmd = 'dig a ' + str(address)
    return """
     <html>
       <body>""" + "Result:\n<br>\n" + (str(subprocess.check_output(cmd, shell=True)) if address else "") + """
          <form action = "/dns" method = "POST">
             <p><h3>Enter address</h3></p>
             <p><input type = 'text' name = 'address'/></p>
             <p><input type = 'submit' value = 'Lookup'/></p>
          </form>
       </body>
    </html>
    """


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)