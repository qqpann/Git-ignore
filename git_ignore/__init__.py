import sys

from .__version__ import __version__

name = "git-ignore"


def main():
    from .main import main
    sys.exit(main())


if __name__ == '__main__':
    main()
