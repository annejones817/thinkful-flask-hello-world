from flask import Flask
from os import environ

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def say_hi(): 
    return "Hello World!"

@app.route("/hello/<name>")
def hi_person(name):
    #Why do you have to put the three quotes? 
    html = """
        <h1>
        Hello {}!
        </h1>
        <p>
        Here's a picture of a kitten. Aww...
        </p>
        <img src = "http://placekitten.com/g/200/300" />
    """
    return html.format(name.title())
    
@app.route("/jedi/<first>/<last>")
def jedi(first, last): 
    jediName = ''
    if (len(last) >= 3):
        for n in range (0, 3): 
            jediName += last[n]
    else: 
        jediName = 'Xxx'
        
    if (len(first)>=2):
        for m in range(0,2): 
            jediName += first[m]
    else: 
       jediName += 'xx'
    return 'Your jedi name is {}.'.format(jediName.title())   
    
if __name__ == "__main__":
    app.run(host=environ['IP'], 
            port=int(environ['PORT']))