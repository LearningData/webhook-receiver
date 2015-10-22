import os
from configparser import ConfigParser
from flask import Flask, request
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def update():
    payload = request.json

    if payload and "repository" in payload:
        if "name" in payload["repository"]:
            name = payload['repository']['name']
            repository = Repository(name)
            if not repository.is_cloned():
                repository.clone()

            repository.update_mirror()

    return "ok"


class Repository:
    origin = ""
    mirror = ""

    def __init__(self, name, config_file="repos.cfg"):
        config = ConfigParser()
        config.read(config_file)
        self.name = name

        if config.has_section(name):
            self.origin = config.get(name, "origin")
            self.mirror = config.get(name, "mirror")

    def path(self):
        return "/tmp/{}".format(self.name)

    def is_cloned(self):
        print(self.path())
        return os.path.exists(self.path())

    def clone(self):
        os.system("cd {} && git clone {}".format("/tmp", self.origin))
        os.system("cd {} && git remote add mirror {}".format(self.path(),
                                                             self.mirror))

    def update_mirror(self):
        os.system("cd {} && git pull origin master".format(self.path()))
        os.system("cd {} && git push mirror master".format(self.path()))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000)
