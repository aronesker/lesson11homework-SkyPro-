from flask import Flask, request, render_template
import utils

app = Flask(__name__)


@app.route('/')
def page_index():
    candidates = utils.load_candidates()

    return render_template("list.html", candidates=candidates)

@app.route("/candidate/<int:uid>")
def page_candidate(uid):
    candidate = utils.get_candidate_by_id(uid)

    return render_template("card.html", candidate=candidate)

@app.route("/candidate/<name>")
def page_candidate_name(name):
    candidates = utils.get_candidate_by_name(name)
    counter = len(candidates)

    return render_template("search.html", candidates=candidates, counter=counter)

@app.route("/candidate/skill/<skill_name>")
def page_candidate_skill(skill_name):
    candidates = utils.get_candidates_by_skill(skill_name)
    counter = len(candidates)

    return render_template("skill.html", candidates=candidates, counter=counter, skill_name=skill_name)

app.run()