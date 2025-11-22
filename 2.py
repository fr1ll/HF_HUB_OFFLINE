# 2.py
import os
os.environ["HF_HOME"] = "./tmp_cache_dr" # to adapt
os.environ["HF_HUB_OFFLINE"] = "1"

# Import transformers first
# Then block sockets to ensure no network access
import socket
from transformers import AutoConfig, AutoModel, AutoTokenizer

original_socket = socket.socket

def guarded_socket(*args, **kwargs):
    raise RuntimeError("Network access attempted in offline mode!")

socket.socket = guarded_socket

try:
    config = AutoConfig.from_pretrained("hf-internal-testing/tiny-random-bert")
    model = AutoModel.from_pretrained("hf-internal-testing/tiny-random-bert")
    tokenizer = AutoTokenizer.from_pretrained("hf-internal-testing/tiny-random-bert")
    print("OFFLINE_SUCCESS")
except RuntimeError as e:
    if "Network access" in str(e):
        print(f"NETWORK_ATTEMPTED: {e}")
        exit(1)
    raise
except Exception as e:
    print(f"FAILED: {e}")
    import traceback

    traceback.print_exc()
    exit(1)