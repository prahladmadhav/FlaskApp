from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
	return '<h1>Hello World!</h1>'

if --name--='__main__':
	app.run(debug=True)