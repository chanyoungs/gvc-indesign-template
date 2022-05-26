import datetime
import glob
import re
import os
import shutil

# Find latest version
latest_path = ""
latest_version = -1
for path in glob.glob("./Bulletins Templates/*.indd"):
    version = int(re.findall("\d+", path)[0])
    if version > latest_version:
        latest_version = version
        latest_path = path

os.makedirs("../output", exist_ok=True)
# Write version file
with open("../output/version.txt", "w") as f:
    f.write(str(latest_version))

# Write timestamp just in case of no changes for git commit
with open("../output/timestamp.txt", "w") as f:
    f.write(str(datetime.datetime.now()))

directory = "../output/Bulletins Templates/"
os.makedirs(directory, exist_ok=True)
shutil.copyfile(latest_path, directory+latest_path)
