# -*- coding: utf-8 -*-

from celeryconfig import app


@app.task(time_limit=10)
def add(a, b):
    return a + b
