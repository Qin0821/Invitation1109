from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/hello/')
def hello():
    return 'Nice to meet you!'


@app.route('/cbg/')
def cbg():
    return render_template('cbg.html')


@app.route('/sign/')
@app.route('/sign/<name>')
def sign(name=None):
    return render_template('index.html', name=name)


@app.route('/user/<username>')
def show_user_profile(username):
    # TypeError: not all arguments converted during string formatting
    return 'Welcome %s' % username


@app.route('/user/<int:post_id>')
def show_post(post_id):
    return 'Post id: %d' % post_id


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'post'
    else:
        return 'get'


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
