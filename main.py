from flask import Flask, request, render_template
app = Flask(__name__)


class Story_class:
    def __init__(self, title, long_desc, accept, value, estim, status):
        self.title = title
        self.long_desc = long_desc
        self.accept = accept
        self.value = value
        self.estim = estim
        self.status = status


@app.route("/")
@app.route("/list/")
def list():
    return ("This will be the list page")


@app.route("/story/", methods=["GET", "POST"])
def add_new_story():
    if request.method == "GET":
        story = Story_class(None, None, None, None, None, None)
        return render_template("form.html", title="Add new Story", story=story)
    elif request.method == "POST":
        return ("I am doing it...")


def main():
    pass

if __name__ == '__main__':
    app.run()