import re
import sys
import os

shortcut_regex = r"^\\d"


def transform_grouping_regex(string):
    # transform my fractions into tex fraction
    # this is work if fraction on one line
    fraction_pattern = re.compile(r"@(.*?)/(.*?)@")
    compiled = fraction_pattern.sub(r"\\frac{\1}{\2}", string) # better for further tex expressions

    sum_pattern = re.compile(r"\\sum from (.*) to (.*?) ")
    compiled = sum_pattern.sub(r"\\sum \\limits_{\1}^{\2} ", compiled)

    overset_pattern = re.compile(r"\\over{(.*?)} ")
    compiled = overset_pattern.sub(r"\\overset{\\text{\1}} ", compiled)

    underset_pattern = re.compile(r"\\under{(.*?)} ")
    compiled = underset_pattern.sub(r"\\underset{\\text{\1}} ", compiled)

    return compiled


def main():
    path_to_file = sys.argv[1]
    filename, file_extension = os.path.splitext(path_to_file)
    output = "../build/" + filename + ".tex"

    # for testing
    #output = filename + ".tex"
    replace_data = {}

    replace_data[r" *"] = r" \cdot "
    replace_data[r"~"] = r"\sim "
    replace_data[r"~~"] = r"\approx "
    replace_data[r"..."] = r"\dots "
    replace_data[r"!="] = r"\neq "
    replace_data[r">="] = r"\ge "
    replace_data[r"<="] = r"\le "
    replace_data[r"—>"] = r" \rightarrow "
    replace_data[r"->"] = r" \rightarrow " # don't ask me about that
    replace_data[r"=>"] = r" \Rightarrow "
    replace_data[r"<=>"] = r" \Leftrightarrow "

    with open(output, "w") as dest:
        with open(path_to_file, "rt") as source:
            for line in source.readlines():
                line = transform_grouping_regex(line)

                if line.startswith(" "):
                    spaces = re.match(r"\s*", line).group()
                    line = line.replace(spaces, "")
                    line = r"\indent " + line + r"\\"
                elif line[0] == "\\" and line[1].isdigit():
                    parts = line.split(" = ", 1)
                    short = parts[0]
                    value = parts[-1].replace("\n", "")

                    replace_data[short] = transform_grouping_regex(value)
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
    reversed_data = list(reversed(sorted(replace_data.keys())))  # because \1 and \11 collapses
    for i in range(1, 5): # Magic. Some shortcuts don't apply properly.
        for shortcut in reversed_data:
            # Read in the file
            with open(output, 'r') as file:
                filedata = file.read()

            # Replace the target string
            filedata = filedata.replace(shortcut, replace_data[shortcut])

            # Write the file out again
            with open(output, 'w') as file:
                file.write(filedata)

    # TODO: remove this bydlo code
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

    # Read in the file
    with open(output, 'r') as file:
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace("\\\\\n\n\\section", "\n\section")
    filedata = filedata.replace("\\\\\n\n\\subsection", "\n\subsection")
    filedata = filedata.replace("\\\\\n\n\\subsubsection", "\n\subsubsection")
    # filedata = filedata.replace("\n\n\n", "\n")

    # Write the file out again
    with open(output, 'w') as file:
        file.write(filedata)


if __name__ == "__main__":
    main()
