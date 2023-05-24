from chalice import BadRequestError, Chalice


app = Chalice(app_name="helloworld")
app.debug = True


@app.route("/")
def index():
    return testy()
    # return {"hello": "world"}


@app.route("/testy")
def testy():
    return {"hello": "test"}


@app.route("/add/{a}/{b}")
def add(a, b):
    a = int(a)
    b = int(b)
    return {"sum": a + b}


MACHINE_LEARNING_MODELS = {
    "gp": "Gaussian Process",
    "nn": "Neural Network",
    "pce": "Polynomial Chaos Expansion",
}


@app.route("/models/{model}")
def models(model):
    try:
        return {"model": MACHINE_LEARNING_MODELS[model]}
    except KeyError:
        raise BadRequestError(f"Unknown model {model}, valid choices are: {", ".join(MACHINE_LEARNING_MODELS)}.")
    except Exception as err:
        raise BadRequestError(f"Error occurred: {err}")


@app.route("/my_route", methods=["POST"])
def my_route_post():
    pass


@app.route("/my_route", methods=["PUT"])
def my_route_put():
    pass


# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to "/".
#
# Here are a few more examples:
#
# @app.route("/hello/{name}")
# def hello_name(name):
#    # "/hello/james" -> {"hello": "james"}
#    return {"hello": name}
#
# @app.route("/users", methods=["POST"])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We"ll echo the json body back to the user in a "user" key.
#     return {"user": user_as_json}
#
# See the README documentation for more examples.
#
