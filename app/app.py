from . import create_app
from app.routes.auth import authBp

app = create_app()


app.register_blueprint(authBp, url_prefix='/')


if __name__ == "__main__":
    app.run(debug=True)
