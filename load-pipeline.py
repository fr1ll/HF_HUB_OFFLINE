from argparse import ArgumentParser
from transformers import pipeline

def main(model_name: str = "facebook/dinov2-small"):
    _ = pipeline(task="image-feature-extraction",
                 model=model_name
    )
    return None

if __name__ == "__main__":
    parser = ArgumentParser(description="Load a Transformers pipeline.")
    parser.add_argument(
        "--model-name",
        type=str,
        default="facebook/dinov2-small",
    )

    args = parser.parse_args()
    main(model_name=args.model_name)