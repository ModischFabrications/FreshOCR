#!/usr/bin/env python3

import platform

# pipenv decided to forbid specification of min versions, so we need to check manually to prevent weird errors
py_version = platform.python_version_tuple()
if int(py_version[0]) < 3 or int(py_version[1]) < 6:
    raise OSError("Python versions older than 3.6 are not supported")


def main():
    print("Starting, this might take a while...")

    # TODO anything

    print("Done.")


if __name__ == '__main__':
    main()
