from flask import Flask


app = Flask(__name__)

@app.route("/")
def welcome():
    return "welcome to flask with cicd"

# @app.route('/')
# def home():
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run(port=5000, debug=True)

if(__name__=='__main__'):
    app.run(host='0.0.0.0', port = 8080)
    
    