from flask import Flask

app = Flask(__name__)



@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run()

'''
The forward slash / in @app.route('/') means like the home page.
You can pass a function around as an argument.
The syntax '@app.route("/")' is called a Python decorator
A decorator function is a function that adds additional functionality to the functions in that
module or class.
for example:
def delay_decorator(function):
    def wrapper():
        time.sleep(1)
        function()
    return wrapper
that function above is like makeup so it it added to another function via @ sign before the function.
@delay_decorator
def say_hello():
    return "Hello, World!"
say_hello()
what say_hello would do is that it would would use its decorator and perform the way, the
decorator has assigned it to.
another way is:
decorated = delay_decorator(say_hello)
decorated()
'''
