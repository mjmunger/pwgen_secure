import os
import tempfile


class FileRandomizer:

    path = None

    def __init__(self, path, Rpg):
        if not os.path.exists(path):
            print("{} does not exist".format(path))
            exit(1)

        self.path = path
        self.Rpg = Rpg

    def process(self, line):
        line = line.strip()
        line = line.replace("#RND#", self.Rpg.generate_password())
        return line

    def set_passwords(self):
        out_fd, out_path = tempfile.mkstemp()
        infile = open(self.path, 'rb')
        outfile = open(out_path, 'w')
        backupfile = open(self.path + ".backup", 'w')

        for line in infile:
            line = line.decode('utf-8')
            backupfile.write(line)
            buff = self.process(line)
            outfile.write(buff + "\n")

        outfile.flush()

        fd = open(out_path, 'r')

        infile.close()
        backupfile.close()

        infile = open(self.path, 'w')
        for line in fd:
            infile.write(line)

        infile.close()
        outfile.close()

        os.remove(out_path)

        print("Done. A backup of the original file was created as {}.backup".format(self.path))

