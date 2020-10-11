#!python3
import os
import re


sourceFile = "./requirements.txt"


if not os.path.exists("./pyproject.toml"):
    os.system("poetry init")

with open(sourceFile) as fh:
    requirements = fh.read()

noComments = re.sub("^#.*$", "", requirements, 0, re.IGNORECASE | re.MULTILINE)
bareRequirements = re.sub(
    "\n+", "\n", noComments, 0, re.IGNORECASE | re.MULTILINE
).strip()

pipPoetryMap = {">": "^", "=": ""}

reqList = list()
for line in bareRequirements.splitlines():
    package, match, version = re.sub(
        r"^(.*?)\s*([~>=<])=\s*v?([0-9\.\*]+)",
        r"\1,\2,\3",
        line,
        0,
        re.IGNORECASE | re.MULTILINE,
    ).split(",")
    try:
        poetryMatch = pipPoetryMap[match]
    except KeyError:
        poetryMatch = match
    poetryLine = f"{package}:{poetryMatch}{version}"
    reqList.append(poetryLine)

print("Found dependencies:")
print(reqList)

while True:
    ans = input("Confirm dependency migration? [Y/n]")
    if ans == "Y":
        break
    elif ans == "n":
        exit()
    print("Please confirm [Y] or abort [n]")

for req in reqList:
    os.system(f"poetry add {req}")
