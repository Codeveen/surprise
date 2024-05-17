from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/propose", methods=['POST'])
def propose():
    return render_template('propose.html')

@app.route("/final", methods=['POST'])
def final():
    return render_template('final.html')


if __name__ == "__main__":
    app.run()