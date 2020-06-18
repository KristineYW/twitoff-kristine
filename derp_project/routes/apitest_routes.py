from flask import Blueprint, render_template, request

apitest_routes = Blueprint("apitest_routes", __name__)

@apitest_routes.route('/retrieve')
def our_home():

    return render_template("api_results.html", title="derp_proj")