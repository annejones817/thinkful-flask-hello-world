from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def say_hi(): 
    return render_template('base.html')

@app.route("/hello/<name>")
def hi_person(name):
    return render_template('template.html', 
                            name = name.title())
    
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
    return render_template('jedi.html',
                            jediName = jediName.title())
    
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)