## resources/routes.py

from .auth import SignupApi, LoginApi
from .search import SearchApi
from .feed import FeedApi
from .tuning import FeedTunerApi

def initialize_routes(api):
    api.add_resource(SignupApi, '/api/auth/signup')
    api.add_resource(LoginApi, '/api/auth/login')

    api.add_resource(FeedApi, '/api/auth/feed')
    api.add_resource(SearchApi, '/api/auth/search/<food_search>')
    api.add_resource(FeedTunerApi, '/api/auth/tune/uri')
