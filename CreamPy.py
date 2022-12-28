#! /usr/bin/env python3

from argparse import ArgumentParser, RawDescriptionHelpFormatter

import requests
import re

module_name = "CreamPyTools: Great System assisten program"
__version__ = "0.1.2"

def main():
    version_string = f"%(prog)s {__version__}\n" #+ \
                    #  f"{requests.__description__}:  {requests.__version__}\n" + \
                    #  f"Python:  {platform.python_version()}"

    parser = ArgumentParser(formatter_class=RawDescriptionHelpFormatter, 
                            description=f"{module_name} (Version {__version__})" )

    parser.add_argument("--version",
                        action="version", version=version_string,
                        help="Display version information and dependencies."
                        )

    args = parser.parse_args()

    # Check for newer version

    try:
        r = requests.get("https://raw.githubusercontent.com/fhudint/CreamPyTools/main/CreamPy.py")

        remote_version = str(re.findall('__version__ = "(.*)"', r.text)[0])
        local_version = __version__

        if remote_version != local_version:
            print("Update Available!\n" +
                  f"You are running version {local_version}. Version {remote_version} \
                  is available at https://github.com/fhudint/CreamPyTools.git")

    except Exception as error:
        print(f"A problem occurred while checking for an update: {error}")

if __name__ == "__main__":
    main()