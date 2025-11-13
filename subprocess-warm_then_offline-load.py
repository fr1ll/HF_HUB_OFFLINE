"""
warm cache in a subprocess, then reuse in offline mode
"""

import os
from pathlib import Path
import shutil
from pytest_socket import disable_socket, enable_socket, SocketBlockedError
from subprocess import run


def main(model_name: str = "facebook/dinov2-small",
         cache_loc: str = "/tmp/cache_huggingface_tmp/"):
    cache_path = Path(cache_loc)
    shutil.rmtree(cache_path, ignore_errors=True)
    os.environ["HF_HOME"] = cache_path.as_posix()
    os.environ["HF_HUB_OFFLINE"] = "0"

    # warm cache in a subprocess
    subprocess_args = [".venv/bin/python", "load-pipeline.py",
                       "--model-name", model_name, ]
    result = run(subprocess_args, check=True, env=os.environ)
    print(f"Warm cache subprocess exited with code: {result.returncode}")

    cache_contents = list(cache_path.glob("**/*"))
    print(f"Number of items in cache: {len(cache_contents)}")

    from transformers import pipeline
    os.environ["HF_HUB_OFFLINE"] = "1"
    disable_socket()
    try:
        _ = pipeline(task="image-feature-extraction",
                        model=model_name
                        )
    except SocketBlockedError as e:
        print(f"SocketBlockedError: {e}")
        print("Offline mode tried to access socket.")
    finally:
        enable_socket()
        
    return None

if __name__ == "__main__":
    main()
