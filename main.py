from flask import Flask, request, render_template
app = Flask(__name__)


class Story_class:
    def __init__(self, id, title, long_desc, accept, value, estim, status):
        self.id = id
        self.title = title
        self.long_desc = long_desc
        self.accept = accept
        self.value = value
        self.estim = estim
        self.status = status


def load_stories_from_file(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
    story_list = []
    for element in lines:
        temp_list = element.replace("\n", "").split(";")
        story = Story_class(int(temp_list[0]),
                            temp_list[1],
                            temp_list[2],
                            temp_list[3],
                            int(temp_list[4]),
                            temp_list[5],
                            temp_list[6]
                            )
        story_list.append(story)
    return story_list


@app.route("/")
@app.route("/list/")
def list():
    story_list = load_stories_from_file("stories.csv")
    return render_template("list.html", story_list=story_list)


@app.route("/story/", methods=["GET", "POST"])
def add_new_story():
    if request.method == "GET":
        story = Story_class(None, None, None, None, None, None, None)
        return render_template("form.html", title="Add new Story", story=story)
    elif request.method == "POST":
        return ("I am doing it...")


def main():
    pass

if __name__ == '__main__':
    app.run()