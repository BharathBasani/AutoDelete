import os

API_ID = int(os.environ.get("API_ID", 12345))
API_HASH = os.environ.get("API_HASH", None)
SESSION = os.environ.get("SESSION")
ADMINS = set(int(x) for x in os.environ.get("ADMINS", "1420903394").split())
TIME = os.environ.get("TIME", None)
