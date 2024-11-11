from flask import Flask
app = Flask(__name__)

@app.get("/")
def home():
    return "hello from flask"

# Endpoints
@app.get("/test")
def test():
    return "Hello from test server"
# Endpoint using Json
app.get("/api/about")
def aboutGet():
    name = {"name": "Jesus"}
    return json.dumps(name)

# create a new route /greet/{name}, this route should accept name 
# as part of the url and return an html message saying hello

@app.get("/greet/<name>")
def greet(name):
    return f"""
<h1 style=color:blue>Hello {name}!</h1>"""

# by creating the farewell message

@app.get("/farewell/<name>")
def farewell(name):
    return f"""
<h1 style=color:red>Farewell {name}!</h1>"""

app.run(debug=True)