# 2b.py
"""basically same as 2.py, just using pytest_socket to disable"""
import os
os.environ["HF_HOME"] = "./tmp_cache_dr" # to adapt
os.environ["HF_HUB_OFFLINE"] = "1"

# Import transformers first
# Then block sockets to ensure no network access
from pytest_socket import disable_socket, SocketBlockedError
from transformers import AutoConfig, AutoModel, AutoTokenizer

disable_socket()

try:
    config = AutoConfig.from_pretrained("hf-internal-testing/tiny-random-bert")
    model = AutoModel.from_pretrained("hf-internal-testing/tiny-random-bert")
    tokenizer = AutoTokenizer.from_pretrained("hf-internal-testing/tiny-random-bert")
    print("OFFLINE_SUCCESS")
except SocketBlockedError as e:
    if "Network access" in str(e):
        print(f"NETWORK_ATTEMPTED: {e}")
        exit(1)
    raise
except Exception as e:
    print(f"FAILED: {e}")
    import traceback

    traceback.print_exc()
    exit(1)