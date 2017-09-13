import re
import sys
import os

shortcut_regex = r"^\\d"
# TODO : definitions
# TODO : lists

def main():
    path_to_file = sys.argv[1]
    filename, file_extension = os.path.splitext(path_to_file)
    output = "../build/" + filename + ".tex"

    replace_data = {}
    with open(output, "w") as dest:
        with open(path_to_file, "r") as source:
            for line in source.readlines():
                if line.startswith(" "):
                    spaces = re.match(r"\s*", line).group()
                    line = line.replace(spaces, "")
                    line = r"\indent" + line + r"\\"
                elif line[0] == "\\" and line[1].isdigit():
                    parts = line.split(' ')
                    short = parts[0]
                    value = parts[-1]

                    replace_data[short] = value
                    line = ''
                elif line.startswith("#"):
                    parts = line.split(" ", 1)
                    header_type = parts[0]
                    header = parts[1]

                    length = len(header_type)
                    if length == 1:
                        line = r"\section*{" + header + r'}' + '\n'

                    if length == 2:
                        line = r"\subsection*{" + header + r'}' + '\n'

                    if length == 3:
                        line = r"\subsubsection*{" + header + r'}' + '\n'
                else:
                    line = r"\noindent " + line.replace('\n', '') + r' \\' + '\n'
                dest.write(line)

    # Out files are not big
    for shortcut in replace_data:
        # Read in the file
        with open(output, 'r') as file:
            filedata = file.read()

        # Replace the target string
        filedata = filedata.replace(shortcut, replace_data[shortcut])

        # Write the file out again
        with open(output, 'w') as file:
            file.write(filedata)

    # Read in the file
    with open(output, 'r') as file:
        filedata = file.read()

    # Replace the target string
    empty_string = r"\noindent  \\"
    double_empty = empty_string + '\n' + empty_string
    filedata = filedata.replace(empty_string, "")

    # Write the file out again
    with open(output, 'w') as file:
        file.write(filedata)


if __name__ == "__main__":
    main()