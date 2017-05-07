from flask import Flask, request, render_template, redirect
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


def save_stories_to_file(file_name, story_list):
    with open(file_name, "w") as file:
        for story in story_list:
            row = ";".join([str(story.id),
                            story.title,
                            story.long_desc,
                            story.accept,
                            str(story.value),
                            story.estim,
                            story.status
                            ])
            file.write(row + "\n")


def get_new_id(story_list):
    id_list = [x.id for x in story_list]
    return max(id_list) + 1


def get_index_from_id(story_list, id):
    for i in range(len(story_list)):
        if story_list[i].id == id:
            break
    return i


@app.route("/")
@app.route("/list/")
def list_of_stories():
    if request.method == "GET":
        story_list = load_stories_from_file("stories.csv")
        return render_template("list.html", story_list=story_list)


@app.route("/list/del@id=<int:id>")
def delete_story(id):
    story_list = load_stories_from_file("stories.csv")



@app.route("/story/", methods=["GET", "POST"])
def add_new_story():
    if request.method == "POST":
        story_list = load_stories_from_file("stories.csv")
        new_story = Story_class(get_new_id(story_list),
                                request.form["story.title"],
                                request.form["story.long_desc"],
                                request.form["story.accept"],
                                request.form["story.value"],
                                request.form["story.estim"],
                                request.form["story.status"]
                                )
        story_list.append(new_story)
        save_stories_to_file("stories.csv", story_list)
        return redirect("/", code=302)
    else:
        story = Story_class("", "", "", "", "", "", "")
        return render_template("form.html", title="Add new Story", story=story)


@app.route("/story/<int:story_id>", methods=["GET", "POST"])
def edit_story(story_id):
    if request.method == "POST":
        story_list = load_stories_from_file("stories.csv")
        for i in range(len(story_list)):
            if story_list[i].id == request.form["story.id"]:
                break
        story_list[i].title = request.form["story.title"]
        story_list[i].long_desc = request.form["story.long_desc"]
        story_list[i].accept = request.form["story.accept"]
        story_list[i].value = request.form["story.value"]
        story_list[i].estim = request.form["story.estim"]
        story_list[i].status = request.form["story.status"]
        save_stories_to_file("stories.csv", story_list)
        return redirect("/", code=302)
    else:
        story_list = load_stories_from_file("stories.csv")
        story = [x for x in story_list if x.id == story_id][0]
        return render_template("form.html", title="Edit Story", story=story)


def main():
    pass

if __name__ == '__main__':
    app.run(debug=True)