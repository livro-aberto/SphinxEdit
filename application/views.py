import os
import re
import math
import json
from os.path import isdir, isfile, join, splitext
import flask
import urllib
from flask import render_template, render_template_string, request
from flask import redirect, url_for, Response, flash, Blueprint
from application import app
import string
from shutil import copyfile, rmtree
import traceback

from flask_babel import Babel, gettext as _

import sphinx

# import special tools for this platform
from tools import Command, load_file, write_file

config_path = 'conf'

sphinxedit = Blueprint('sphinxedit', __name__, template_folder='templates')

babel = Babel(app)

@babel.localeselector
def get_locale():
    return 'en'

@app.before_request
def before_request():
    flask.g.locale = get_locale()

@app.context_processor

def package():
    sent_package = {}
    sent_package['_'] = _
    sent_package['url_encode'] = lambda x: urllib.quote(x, safe='')
    sent_package['floor'] = math.floor
    sent_package['len'] = len
    return sent_package

def build(timeout=10):
    # Replace this terrible implementation
    config_path = 'conf'
    source_path = join('repos', 'source')
    build_path = join('repos', 'build/html')
    command = 'sphinx-build -c ' + config_path + ' ' + source_path + ' ' + build_path

    process = Command(command)
    process.run(timeout=timeout)
    return True

def menu_bar():
    left  = [{'url': url_for('sphinxedit.edit'), 'name': 'home'}]
    right  = [{'url': url_for('sphinxedit.edit'), 'name': 'home'}]
    return { 'left': left, 'right': right}

filename = 'index'

@sphinxedit.route('/', methods = ['GET', 'POST'])
def edit():
    html_scroll = 0
    edit_scroll = 0
    branch_source_path = join('repos', 'source', filename + '.rst')
    branch_html_path = join('repos', 'build/html', filename + '.html')
    if request.method == 'POST':
        html_scroll = request.form['html_scroll']
        edit_scroll = request.form['edit_scroll']
        write_file(branch_source_path, request.form['code'])
    build()
    print(branch_source_path)
    rst = load_file(branch_source_path)
    doc = render_template_string(load_file(branch_html_path), barebones=True)
    menu = menu_bar()
    return render_template('edit.html', doc=doc, rst=rst, filename=filename,
                           menu=menu, html_scroll=html_scroll,
                           edit_scroll=edit_scroll, render_sidebar=False)

@sphinxedit.route('/_images/<path:filename>')
#@bookcloud.route('/edit/<project>/<branch>/images/<path:filename>', methods = ['GET'])
def get_tikz(filename):
    images_path = join('repos', 'build/html/_images')
    return flask.send_from_directory(os.path.abspath(images_path), filename)

@sphinxedit.route('/<action>/_static/<path:filename>')
def get_static(action, filename):
    user_repo_path = join('repos', current_user.username)
    return flask.send_from_directory(os.path.abspath(join(user_repo_path, 'build/html/_static/')), filename)


@sphinxedit.route('/_static/<path:filename>')
def get_global_static(filename):
    return flask.send_from_directory(os.path.abspath('conf/biz/static/'), filename)

@sphinxedit.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@sphinxedit.errorhandler(Exception)
def internal_server_error(e):
    print(">>>" + repr(e))
    message = repr(e)
    trace = traceback.format_exc()
    trace = string.split(trace, '\n')
    return render_template('500.html', message=message, trace=trace), 500


