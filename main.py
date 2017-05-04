from flask import Flask, request, render_template
app = Flask(__name__)


@app.route("/")
def index():
    return ("This is the index page. Method used:{}".format(request.method))


@app.route("/tuna", methods=["GET", "POST"])
def tuna():
    return ("This is the tuna page. Looks awsome! Method used:{}".format(request.method))


def main():
    pass

if __name__ == '__main__':
    app.run()