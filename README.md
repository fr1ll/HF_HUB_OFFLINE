# Reproduce Transformers offline mode behavior

*Expected behavior*: Both scripts `inprocess-warm_then_offline-load.py` and `subprocess-warm_then_offline-load.py` should succeed in loading a Transformers pipeline in offline mode after warming the cache.

~*Observed behavior*: Only `inprocess-warm_then_offline-load.py` succeeds, while `subprocess-warm_then_offline-load.py` fails to load the pipeline in offline mode.~

Update 2025-11-22: Reason for offline-mode behavior previously is
that I was setting HF_HUB_OFFLINE = 1 *after* importing transformers,
when it needs to be set before.
Update part 2: also works with same library versions I tested in main

Detailed here:
https://github.com/huggingface/transformers/pull/42308
