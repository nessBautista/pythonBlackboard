from flask import render_template, Blueprint, redirect, request, session, url_for
import requests
from pyactiveresource.connection import UnauthorizedAccess
from dotenv import load_dotenv
import shopify
import os
import json
from templates import app

hello_blueprint = Blueprint("hello", __name__)


# @hello_blueprint.route("/")
@hello_blueprint.route("/hello")
def index_test():
    return render_template("index.html")


@hello_blueprint.route("/test")
def test():
    print(app.config)
    return "test"


@hello_blueprint.route("/")
def index():
    load_dotenv("./sample.env")
    API_KEY = "b089e5f0d374b1d1de404998536dbd09"
    API_VERSION = "2019-10"
    API_SECRET = "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"
    print(f"------>api key:{API_KEY}")
    if not is_authenticated():
        print(f"------>not logged In")
        return login()
    print(f"------>Is logged In")
    shopify.Session.setup(api_key=API_KEY, secret=API_SECRET)
    api_session = shopify.Session(session["shop"], API_VERSION, session["access_token"])

    shopify.ShopifyResource.activate_session(api_session)

    try:
        products = shopify.Product.find(limit=10)

        # say hello to flask
        # web_hook_url = "https://hooks.slack.com/services/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"
        # slack_msg = {"text": "Hello from shopify:{}".format(str_url_webhook)}
        # requests.post(web_hook_url, data=json.dumps(slack_msg))

    except UnauthorizedAccess:
        return login()
    except:
        print(f"------>An unknown error occured")
        return "An unknown error occured.", 500

    return render_template("index.html")
    # return render_template("products.html", api_key=API_KEY, products=products)


@hello_blueprint.route("/auth/shopify/callback")
def oauth_callback():
    print("----> got to callback")
    params = request.args
    shop = params["shop"]
    print(f"----> will request token with shop: {shop}")
    try:
        API_VERSION = "2019-10"
        token = shopify.Session(shop, API_VERSION).request_token(params)
        print(f"----> got token {token}")
    except shopify.session.ValidationException:
        return "HMAC signature does not match. Check your API credentials.", 400
    except:
        print("---->An unknown error occured.")
        return "An unknown error occured.", 500

    session["shop"] = shop
    session["access_token"] = token

    return redirect(url_for("hello.index"))


def is_authenticated():
    params = request.args
    if ("shop" in params) & ("shop" in session):
        if session["shop"] != params["shop"]:
            clear_session()
            return False

    return "access_token" in session


def clear_session():
    del session["shop"]
    del session["access_token"]


def login():
    load_dotenv("./sample.env")
    # API credentials are sourced from enviroment variables:
    API_KEY = "b089e5f0d374b1d1de404998536dbd09"

    API_SECRET = "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"
    API_VERSION = "2019-10"
    shopify.Session.setup(api_key=API_KEY, secret=API_SECRET)

    scopes = ["read_products, read_analytics"]

    shop = request.args.get("shop", None)
    print(f"------>rendering login template for:{shop} {API_KEY} ")
    if shop is not None:
        print(f"------>rendering login template")
        return render_template(
            "login.html",
            shop=shop,
            api_key=API_KEY,
            scopes=",".join(scopes),
            redirect_uri=url_for(
                "hello.oauth_callback", _external=True, _scheme="https"
            ),
        )

    else:
        return "No shop parameter provided.", 400


@hello_blueprint.route("/cardEvent")
def cart_created():
    web_hook_url = (
        "https://hooks.slack.com/services/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"
    )
    slack_msg = {"text": "new cart created"}
    requests.post(web_hook_url, data=json.dumps(slack_msg))
