from flask import Flask, redirect, render_template

app = Flask(__name__)

@app.errorhandler(404)
def not_found(e):
    return redirect('/')

@app.route('/')
def index():
    return render_template('grid_layout.html')

@app.route('/gridlayout')
def grid_layout():
    return render_template('grid_layout.html')

@app.route('/flexbox')
def flexbox():
    return render_template('flexbox.html')

if __name__ == '__main__':
    app.run(debug = True)