from flask import Flask, jsonify
from flask_cors import CORS
from database import setup_db


def create_app(test=False):
    app = Flask(__name__)

    setup_db(app, test)

    CORS(app, resources={r"/*": {"origins": "*"}})

    @app.route("/")
    def index():
        return {
            "success": True,
            "message": "API is live and running"
        }

    @app.after_request
    def after_request_func(response):
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response

    ####
    # Error Handlers
    ####

    @app.errorhandler(400)
    def bad_request(error):
        return (
            jsonify(
                {
                    "success": False, "error": 400,
                    "message": "bad request"
                }
            ),
            400
        )

    @app.errorhandler(404)
    def not_found(error):
        return (
            jsonify(
                {
                    "success": False, "error": 404,
                    "message": "resource not found"
                }
            ),
            404,
        )

    @app.errorhandler(422)
    def unprocessable(error):
        return (
            jsonify(
                {
                    "success": False,
                    "error": 422,
                    "message": "unprocessable"
                }
            ),
            422,
        )

    @app.errorhandler(500)
    def internal_error(error):
        return (
            jsonify(
                {
                    "success": False, "error": 500,
                    "message": "internal server failure"
                }
            ),
            500,
        )

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
