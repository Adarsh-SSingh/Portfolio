from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')

@app.route('/resume')
def resume():
    """Render the resume page."""
    return render_template('resume.html')

@app.route('/projects')
def projects():
    """Render the projects page."""
    return render_template('project.html')

@app.route('/contact')
def contact():
    """Render the contact page."""
    return render_template('contact.html')

if __name__ == '__main__':
    # Production mode - debug disabled for deployment
    app.run(debug=False)