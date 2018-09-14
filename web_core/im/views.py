#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

im_bp = Blueprint('im_bp', __name__, template_folder='templates')


@im_bp.route('/im')
def im_index():
    try:
        return render_template('im/index.html')
    except TemplateNotFound:
        abort(404)









