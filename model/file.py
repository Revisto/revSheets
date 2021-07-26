class File:
    def read(self, filename):
        with open(filename, 'r') as f:
            lines = f.readlines()
        return lines

    def remove_extra_spaces(self, line):
        line_splitted = line.split(" ")
        line_splitted_without_none_strings = list(filter(None, line_splitted))
        line_joined = " ".join(line_splitted_without_none_strings)
        return line_joined