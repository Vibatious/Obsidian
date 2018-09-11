from flask import Flask,request,render_template
app = Flask(__name__)

@app.route('/'):
	def home():
		return render_template('about_us.html')


@app.route('/main'):
	def main():
	return  render_template("main.html")
if __name__ == '__main__':
	app.run(debug = True)


