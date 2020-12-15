from dotenv import load_dotenv
import os

if os.path.isfile(".env"):
    load_dotenv()

# Auth0 env variables
AUTH0_DOMAIN = os.getenv("AUTH0_DOMAIN", None)
ALGORITHMS = os.getenv("ALGORITHMS", None)
API_AUDIENCE = os.getenv("API_AUDIENCE", None)

# Database paths
DATABASE_URL = os.getenv("DATABASE_URL", None)
TEST_DATABASE_URL = "sqlite:///database/testing.db"
