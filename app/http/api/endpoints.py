from app.http.api.middlewares import login_required
from flask import Flask, json, g, request
from app.kudo.service import Service as KudoService
from app.kudo.schema import GithubRepoSchema
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


def json_response(payload, status=200):
    return json.dumps(payload), status, {'content-type': 'application/json'}


@app.route("/kudos", methods=["GET"])
@login_required
def index():
    print("Got request to create Kudo")
    return json_response(KudoService(g.user).find_all_kudos())


@app.route("/kudos", methods=["POST"])
@login_required
def create():
    print("Got request to create Kudo")
    github_repo = GithubRepoSchema(unknown='EXCLUDE').loads(request.data)
    kudo = KudoService(g.user).create_kudo_for(github_repo)
    return json_response(kudo)


@app.route("/kudo/<int:repo_id>", methods=["DELETE"])
@login_required
def delete(repo_id):
    print("Got request to delete Kudo")
    kudo_service = KudoService(g.user)
    if kudo_service.delete_kudo_for(repo_id):
        return json_response({})
    else:
        return json_response({'error': 'kudo not found'}, 404)
