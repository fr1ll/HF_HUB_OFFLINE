# 1.py
import os

os.environ["HF_HOME"] = "./tmp_cache_dr"  # to adapt

from transformers import AutoConfig, AutoModel, AutoTokenizer

config = AutoConfig.from_pretrained("hf-internal-testing/tiny-random-bert")
model = AutoModel.from_pretrained("hf-internal-testing/tiny-random-bert")
tokenizer = AutoTokenizer.from_pretrained("hf-internal-testing/tiny-random-bert")
print("CACHE_WARMED")