import json
from flask import Flask, request
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def update():
    payload = request.json

    if payload and "repository" in payload:
        if "name" in payload["repository"]:
            repository = payload['repository']['name']
            Application.update(respository)
    return "ok"


class Application:
    @staticmethod
    def update(repository):
        pass


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
