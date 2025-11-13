# Reproduce Transformers offline mode behavior

*Expected behavior*: Both scripts `inprocess-warm_then_offline-load.py` and `subprocess-warm_then_offline-load.py` should succeed in loading a Transformers pipeline in offline mode after warming the cache.

*Observed behavior*: Only `inprocess-warm_then_offline-load.py` succeeds, while `subprocess-warm_then_offline-load.py` fails to load the pipeline in offline mode.
