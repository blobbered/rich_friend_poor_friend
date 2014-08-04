from flask import Flask
from flask import render_template
app = Flask(__name__)
app.config.update(
	DEBUG=True,
	)

@app.route("/")
def main(name=None):
  return render_template('main.html', name=name)

if __name__ == "__main__":
  app.run()
