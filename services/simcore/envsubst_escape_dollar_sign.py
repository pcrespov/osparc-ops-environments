import sys

# This is intentionally only using vanilla python and no pip packages.
#
# Escape $ characters in environment variables for proper use of envsubst by switching "$" --> "$${empty_var}" (see https://stackoverflow.com/a/61259844/10198629)
assert len(sys.argv) == 3
original = open(sys.argv[1], "r+")
lines = original.readlines()
escaped = open(sys.argv[2], "w+")
for line in lines:
    if len(line) > 0 and len(line.lstrip()) > 0:
        if line.lstrip()[0] != "#":  # Ignore commented lines
            if "$" in line:
                escapedLine = "".join(
                    [
                        x + "$${empty_var}"
                        for x in line.split("$")
                        if x != line.split("$")[-1]
                    ]
                    + [line.split("$")[-1]]
                )
                # print(escapedLine)
                # print(line)
                escaped.write(escapedLine)
            else:
                escaped.write(line)
