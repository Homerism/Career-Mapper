from flask import Blueprint, redirect, render_template, request, jsonify, send_from_directory

jobs_views = Blueprint('jobs_views', __name__, template_folder='../templates')

from App.models import Jobs