#! /usr/bin/env python3

from argparse import ArgumentParser, RawDescriptionHelpFormatter

import platform
import requests
import re
import sys

module_name = "CreamPyTools: Great System assisten program"
__version__ = "0.0.2"

def main():
    version_string = f"%(prog)s {__version__}\n" + \
                     f"{requests.__description__}:  {requests.__version__}\n" + \
                     f"Python:  {platform.python_version()}"

    parser = ArgumentParser(formatter_class=RawDescriptionHelpFormatter, 
                            description=f"{module_name} (Version {__version__})" )

    parser.add_argument("--version",
                        action="version", version=version_string,
                        help="Display version information and dependencies."
                        )

    # parser.add_argument("add-schedule", dest="add_schedule",
    #                     action="store_true",
    #                     help="Add schedule to Great")

    parser.add_argument("--add", action="store")

    args = parser.parse_args()

    # Check for newer version of CreamPyTools

    try:
        r = requests.get("https://raw.githubusercontent.com/fhudint/CreamPyTools/main/CreamPy.py")

        remote_version = str(re.findall('__version__ = "(.*)"', r.text)[0])
        local_version = __version__

        if remote_version != local_version:
            print("Update Available!\n" +
                  f"You are running version {local_version}.\n" +
                  f"Version {remote_version} is available at https://github.com/fhudint/CreamPyTools")

    except Exception as error:
        print(f"A problem occurred while checking for an update: {error}")

    python_version = sys.version.split()[0]
    
    if sys.version_info < (3, 6):
        print("Sherlock requires Python 3.6+\nYou are using Python %s, which is not supported by Sherlock" % (python_version))
        sys.exit(1)

    if args.add is not None:
        from services import googleChrome
        googleChrome.addChromeUser(args.add)


if __name__ == "__main__":
    main()
    # Notify caller that all queries are finished.
