from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def hi():
  return render_template("index.html")

@app.route('/about')
def about():
  return render_template("about.html")

@app.route('/proyects')
def proyects():
  return render_template("proyects.html")
  


if __name__ == '__main__':
  app.run(port=2000,debug=True)