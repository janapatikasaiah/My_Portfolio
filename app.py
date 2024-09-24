from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/skills')
def skills():
    return render_template('skill.html')



@app.route('/project')
def project():
    return render_template('project.html')



@app.route('/certification')
def certification():
    return render_template('certification.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)