from flask import render_template, request, url_for, redirect, flash, send_file, abort
from flask import Blueprint
from ntb_marine import app_config, auth, __version__, app
from ntb_marine import ms_file_control 
import requests

document = Blueprint('document', __name__)
