import os

SJCLIENT_SOL_HOST = os.environ.get("SJCLIENT_SOL_HOST", "")
SJCLIENT_SOL_VPN = os.environ.get("SJCLIENT_SOL_VPN", "")
SJCLIENT_SOL_USER = os.environ.get("SJCLIENT_SOL_USER", "")
SJCLIENT_SOL_PASSWORD = os.environ.get("SJCLIENT_SOL_PASSWORD", "")

SJCLIENT_SOL_CONNECT_TIMEOUT_MS = int(
    os.environ.get("SJCLIENT_SOL_CONNECT_TIMEOUT_MS", 3000)
)
SJCLIENT_SOL_RECONNECT_RETRIES = int(
    os.environ.get("SJCLIENT_SOL_RECONNECT_RETRIES", 10)
)
SJCLIENT_SOL_KEEP_ALIVE_MS = int(
    os.environ.get("SJCLIENT_SOL_KEEP_ALIVE_MS", 3000)
)
SJCLIENT_SOL_RECONNECT_RETRY_WAIT = int(
    os.environ.get("SJCLIENT_SOL_RECONNECT_RETRY_WAIT", 3000)
)
SJCLIENT_SOL_KEEP_ALIVE_LIMIT = int(
    os.environ.get("SJCLIENT_SOL_KEEP_ALIVE_LIMIT", 3)
)

SJ_PAPIUSER_ID = os.environ.get("SJ_PAPIUSER_ID", "")
SJ_PAPIUSER_PASSWORD = os.environ.get("SJ_PAPIUSER_PASSWORD", "")