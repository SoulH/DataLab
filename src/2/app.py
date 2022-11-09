from _proj.settings import app
from v1.urls import endpoints_api_v1


# Load endpoints
[app.register_blueprint(bp) for bp in endpoints_api_v1]
