import os
API_ID = os.getenv("API_ID", "7948888")
API_HASH = os.getenv("API_HASH", "48285ac512613754f7913b310e884222")
BOT_TOKEN = os.getenv("BOT_TOKEN", "AAEqr0qHkncbPANl4sIyY3Zsrz08qg88tkc")
DATABASE_URL = os.getenv("DATABASE_URL")
OWNER_ID = list({int(x) for x in os.environ.get("OWNER_ID", "6033604536")
