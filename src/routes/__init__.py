from flask import Blueprint
from src.routes.extraction import extraction_api
from src.routes.summarizer import summarize_api
from src.routes.categorizer import categorizer_api
from src.routes.gist import gist_main_api, gist_data_api
from src.routes.gmail import gmail_api

api_blueprint = Blueprint("API", __name__, url_prefix="/api/")
api_blueprint.register_blueprint(extraction_api.extract_bp)
api_blueprint.register_blueprint(summarize_api.summarize_bp)
api_blueprint.register_blueprint(categorizer_api.category_bp)
api_blueprint.register_blueprint(gmail_api.gmail_bp)
api_blueprint.register_blueprint(gist_main_api.gist_bp)
api_blueprint.register_blueprint(gist_data_api.gist_data_bp)


@api_blueprint.route("/", methods=["GET"])
def get_data():
    return "Homepage route setup!"
