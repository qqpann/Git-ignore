import sys

name = "git-ignore"
__version__ = '0.2'


def main():
    from .main import main
    sys.exit(main())


if __name__ == '__main__':
    main()
