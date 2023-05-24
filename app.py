from chalice import BadRequestError, Chalice, NotFoundError, Response


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
        raise BadRequestError(f"Unknown model {model}, valid choices are: {', '.join(MACHINE_LEARNING_MODELS)}.")
    except Exception as err:
        raise BadRequestError(f"Error occurred: {err}")


OBJECTS = {}


# app.current_request.query_params - A dict of the query params for the request.
# app.current_request.headers - A dict of the request headers.
# app.current_request.uri_params - A dict of the captured URI params.
# app.current_request.method - The HTTP method (as a string).
# app.current_request.json_body - The parsed JSON body (json.loads(raw_body))
# app.current_request.raw_body - The raw HTTP body as bytes.
# app.current_request.context - A dict of additional context information
# app.current_request.stage_vars - Configuration for the API Gateway stage


@app.route("/objects/{key}", methods=["GET", "PUT"])
def crud(key):
    request = app.current_request

    if request.method == "PUT":
        OBJECTS[key] = request.json_body

    elif request.method == "GET":
        try:
            return {key: OBJECTS[key]}
        except KeyError:
            raise NotFoundError(key)


@app.route("/introspect")
def introspect():
    return app.current_request.to_dict()


@app.route("/bye")
def bye():
    return Response(body="Goodbye, world!",
                    status_code=200,
                    headers={"Content-Type": "text/plain"})

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
