from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '49f207b82bd6adbd7e6ae4e69dc8303b'

posts = [
    {
        'author': 'George K mbariah',
        'title': 'Blog Post 1',
        'content': 'My first post content',
        'date_posted': 'May 5, 2020'
    },
    {
         'author': 'Jason Alexander',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'May 6, 2020'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)



@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='login', form=form)



if __name__ ==  '__main__':
    app.run(debug=True)