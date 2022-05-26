import datetime
import glob
import re
import os

# Find latest version
latest_path = ""
latest_version = -1
for path in glob.glob("./Bulletins Templates/*.indd"):
    version = int(re.findall("\d+", path)[0])
    if version > latest_version:
        latest_version = version
        latest_path = path

# Write version file
with open("version.txt", "w") as f:
    f.write(str(latest_version))

# Write timestamp just in case of no changes for git commit
with open("timestamp.txt", "w") as f:
    f.write(str(datetime.datetime.now()))

# Delete older files
for path in glob.glob("./Bulletins Templates/*.indd"):
    version = int(re.findall("\d+", path)[0])
    if version < latest_version:
        os.remove(path)
