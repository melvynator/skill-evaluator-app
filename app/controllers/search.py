import requests
from flask import Blueprint, render_template
from flask import request
from ..forms.search import Search, StackoverflowForm

search = Blueprint('search', __name__, url_prefix='/home')


@search.route('/', methods=['GET'])
def search_form():
    error = None
    form = Search(request.form)
    return render_template("search.html", form=form, error=error)


@search.route('/question', methods=['POST'])
def popularity_search_processing():
    form = StackoverflowForm(request.form)
    # check the form value
    if form.validate_on_submit():
        techno = form.tag.data
        response = requests.post("http://0.0.0.0:5000/api/v1/stats/question_frequency", json={"tags": techno})
        json_response = response.json()
        print(json_response)
        return render_template("question_result.html", result=json_response["result"])
    else:
        return render_template("search.html", form=form)


@search.route('/job', methods=['POST'])
def job_search_processing():
    form = Search(request.form)
    # check the form value
    if form.validate_on_submit():
        techno = form.techno.data
        interval = form.interval.data
        response = requests.post("http://0.0.0.0:5000/api/v1/jobs/", json={"techno": techno, "interval": interval})
        json_response = response.json()
        print(json_response["result"])
        return render_template("job_result.html", result=json_response["result"])
    else:
        return render_template("search.html", form=form)