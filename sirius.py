"""
SIRIUS LOCAL AI – Main Entry Point
Spúšťa CLI parser a vykonáva commandy.
"""

import sys
from runtime.cli import CLI


def main():
    cli = CLI()
    cli.run(sys.argv)


if __name__ == "__main__":
    main()
