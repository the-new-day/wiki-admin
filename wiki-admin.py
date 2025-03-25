import argparse
import sys
from utils.logger import setup_logger
from scripts.replace_text import replace_text
from scripts.delete_pages import delete_pages

def main():
    global_parser = argparse.ArgumentParser(add_help=False)
    global_parser.add_argument("--pages", nargs="+", help="Pages list")
    global_parser.add_argument("--verbose", action="store_true", help="Print logs")
    global_parser.add_argument("--no-log", action="store_true", help="Disable logging")

    parser = argparse.ArgumentParser(description="MediaWiki management through API", parents=[global_parser])
    subparsers = parser.add_subparsers(dest="command", required=True)

    replace_parser = subparsers.add_parser("replace", help="Mass text replacement")
    replace_parser.add_argument("--old", required=True, help="Text to replace")
    replace_parser.add_argument("--new", required=True, help="New text")

    delete_parser = subparsers.add_parser("delete", help="Mass page deletion")
    delete_parser.add_argument("--reason", required=False, help="Reason for deletion")

    global_args, remaining_args = global_parser.parse_known_args()

    global logger
    logger = setup_logger(verbose=global_args.verbose, disable_logging=global_args.no_log)

    args = parser.parse_args(remaining_args)
    args.pages = global_args.pages

    if args.command == "replace":
        replace_text(args.old, args.new, args.pages)
    elif args.command == "delete":
        delete_pages(args.pages)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
