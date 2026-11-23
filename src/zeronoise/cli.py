import argparse
import sys
from pathlib import Path
def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description= "Mark silent stretches in a video as a DaVinci Resolve timeline")
    parser.add_argument(
        "video",
        type = Path,
        help = "Path to the source video"
    )
    args = parser.parse_args(argv)
    if args.video.is_file(): 
        print(args.video)
        return 0
    else:
        print (f"error: video not found: {args.video}", file=sys.stderr)
        return 1
    