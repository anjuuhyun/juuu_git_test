from flask import Blueprint

blue_first = Blueprint("first", __name__, url_prefix= "/first")

@blue_first.route("/test")


