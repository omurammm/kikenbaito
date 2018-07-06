#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request

import json

f = open('static/job_db.json', 'r')
job_ = json.load(f)



app = Flask(__name__)

@app.route("/")
def index():
    job_list = []
    for job in job_.values():
        job_list.append(job)
    job_sorted=sorted(job_list, key=lambda x:-x['危険度'])
    return render_template('index.html', jobs=job_sorted)

@app.route("/safe")
def index_safe():
    job_list = []
    for job in job_.values():
        job_list.append(job)
    job_sorted=sorted(job_list, key=lambda x:x['危険度'])
    return render_template('index.html', jobs=job_sorted)


@app.route("/job")
def job():
    name_ = request.args.get('name')
    info = job_[name_]
    return render_template('job.html', job_info=info) 


if __name__ == "__main__":
    # flaskの起動
    app.run(debug=True, host="0.0.0.0")
