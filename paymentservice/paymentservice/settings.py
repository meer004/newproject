from starlette.config import config
from starlette.datastructures import secret

config = config(".env")

DATABASE_URL = config("DATABASE_URL", cast=secret)
TEST_DATABASE_URL = config("TEST_DATABASE_URL", cast=secret)
STRIPE_API_KEY = config("STRIPE_API_KEY", cast=secret)
STRIPE_PUBLISH_KEY = config("STRIPE_PUBLISH_KEY", cast=secret)
STRIPE_WEBHOOK_SECRET = config("STRIPE_WHBOOK_SECRET", cast=secret)