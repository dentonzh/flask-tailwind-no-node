from flask import Flask, render_template
import subprocess

app = Flask(__name__)
app.debug = True

with app.app_context():
    if app.debug:
        subprocess.Popen(
            [
                './tailwindcss',
                '-i',
                'app/static/css/input.css',
                '-o',
                'app/static/css/output.css',
                '--watch',
            ]
        )

@app.route('/')
def hello():
    return render_template('index.html', title='Hello 👋')


if __name__ == '__main__':
    app.run(debug=True)
