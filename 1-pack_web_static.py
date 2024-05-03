#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the web_static folder
"""

from fabric.api import local
from datetime import datetime

def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder

    Returns:
        str: Path to the archive if generated successfully, None otherwise
    """
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    archive_name = "web_static_" + timestamp + ".tgz"
    local("mkdir -p versions")
    result = local("tar -cvzf versions/{} web_static".format(archive))
    if result is not None:
        return archive
    else:
        return None

if __name__ == "__main__":
    do_pack()

