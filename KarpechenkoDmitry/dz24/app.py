from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def wiki():
    return render_template('index.html')

@app.route('/git', methods=['GET'])
def git():
    return render_template('GitHub.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
