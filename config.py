import os

# ================= CONFIG =================
BOT_TOKEN = os.getenv("BOT_TOKEN") or ""
API_ID = int(os.getenv("API_ID") or 23806754)
API_HASH = os.getenv("API_HASH") or "0b52aa37a124eb867ee42cbddcfbcb9f"
OWNER_ID = int(os.getenv("OWNER_ID") or 8425759821)
MONGO_URI = os.getenv("MONGO_URI") or ""
OPENROUTER_KEY = os.getenv("OPENROUTER_KEY") or ""
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
WARN_DELETE_DELAY = 3  # seconds
# ==========================================

