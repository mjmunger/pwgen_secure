import secrets
import mmap
import time
import os
from pprint import pprint

class Rpg:


    verbosity = 0
    password_count = 1

    show_time = False
    show_analysis = False

    use_upper = False
    use_lower = False
    use_symbol = False
    use_digits = False
    use_space = False
    use_brackets = False
    use_minus = False
    use_underline = False
    use_pattern = False
    use_words = False

    remove_homoglyphs = False

    list_upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                  "U", "V", "W", "X", "Y", "Z"]

    list_lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                  "u", "v", "w", "x", "y", "z"]

    list_symbol = ["!", "@", "#", "$", "%", "^", "&", "*"]
    list_digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    list_space = [" "]
    list_brackets = ["{", "}", "[", "]", "(", ")", "<", ">"]

    list_minus = ["-"]
    list_underline = ["_"]

    list_homoglyphs = ["1", "i", "I", "O", "0", 'l']

    list_punctuation = [".", ",", ";", ":"]

    list_vowels_upper = ['A', 'E', 'I', 'O', 'U']
    list_vowels_lower = ['a', 'e', 'i', 'o', 'u']

    list_consonant_lower = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w",
                            "x", "y", "z"]
    list_consonant_upper = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W",
                            "X", "Y", "Z"]

    list_final_charset = []

    recipes = {"mac": 'h{2}\:h{2}\:h{2}\:h{2}\:h{2}\:h{2}',
               "google": "l{16}",
               "pin4": "d{4}",
               "pin6": "d{6}",
               "iphone": "l{4} l{4} l{4} l{4}",
               "android": "l{4} l{4} l{4} l{4}",
               "strong": "M{16}",
               "ridiculous": "N{32}",
               "ludicrous": "N{64}",
               "painful": "N{128}",
               "banking": "N{16}"}

    use_magic = False

    password_length = 16

    debug = False

    start_time = None
    end_time = None
    show_time = False

    password_pattern = None
    character_set = None

    def __init__(self, character_class, class_option):
        self.start_time = time.time()
        self.setup_generator(character_class, class_option)

    def setup_options(self, args):

        self.set_verbosity(args['-v'])

        if args['-d']:
            self.verbosity = 11
            self.log("Debug mode enabled. Verbosity = 11", 10)
            self.log("Arguments:")
            pprint(args)

        self.set_count(args['-n'])
        self.show_time = args['-t']
        self.show_analysis = args['-a']

    def log(self, message, required_level = 1):
        if self.verbosity < required_level:
            return True

        print("%s" % message)

    def set_count(self, count):
        self.password_count = 1 if count is False else int(count)
        self.log("Password count: %s" % self.password_count)

    def set_verbosity(self, level):
        self.verbosity = 0 if level is False else int(level)

    def class_is_magic(self, character_class):
        for name, pattern in self.recipes.items():
            if character_class == name:
                self.log("Magic class detected: %s" % name)
                self.use_magic = True
                self.use_pattern = True
                self.password_pattern = pattern
                return self.use_magic

    def setup_generator(self, character_class, class_option):

        if self.class_is_magic(character_class):
            return True

        if "p" in character_class:
            self.use_pattern = True
            if pattern is None:
                self.error_out("You've asked me to create a pattern based password, but failed to provide a pattern!")
            self.password_pattern = pattern
            return True

        if "w" in character_class:
            self.use_words = True
            return True

        self.character_set = character_class

        self.use_upper = True if "u" in character_class else False
        self.use_lower = True if "l" in character_class else False
        self.use_symbol = True if "s" in character_class else False
        self.use_space = True if "c" in character_class else False
        self.use_digits = True if "d" in character_class else False
        self.use_brackets = True if "b" in character_class else False
        self.use_minus = True if "m" in character_class else False
        self.use_underline = True if "n" in character_class else False
        self.remove_homoglyphs = True if "e" in character_class else False
        self.show_time = True if "t" in character_class else False

        self.log("use_upper: %s" % str(self.use_upper), 3)
        self.log("use_lower: %s" % str(self.use_lower), 3)
        self.log("use_symbol: %s" % str(self.use_symbol), 3)
        self.log("use_digits: %s" % str(self.use_digits), 3)
        self.log("use_space: %s" % str(self.use_space), 3)
        self.log("use_brackets: %s" % str(self.use_brackets), 3)
        self.log("use_minus: %s" % str(self.use_minus), 3)
        self.log("use_underline: %s" % str(self.use_underline), 3)
        self.log("use_pattern: %s" % str(self.use_pattern), 3)

    def error_out(self, message):
        print(message)
        print("Use --help to see syntax and usage.")
        exit(1)

    def render_charset(self):
        character_set = []

        if self.use_upper:
            self.log("  -> list_upper requested, adding: %s" % self.list_upper, 10)
            character_set = character_set + self.list_upper
        if self.use_lower:
            self.log("  -> list_lower requested, adding: %s" % self.list_lower, 10)
            character_set = character_set + self.list_lower
        if self.use_symbol:
            self.log("  -> list_symbol requested, adding: %s" % self.list_symbol, 10)
            character_set = character_set + self.list_symbol
        if self.use_digits:
            self.log("  -> list_digits requested, adding: %s" % self.list_digits, 10)
            character_set = character_set + self.list_digits
        if self.use_space:
            self.log("  -> list_space requested, adding: %s" % self.list_space, 10)
            character_set = character_set + self.list_space
        if self.use_brackets:
            self.log("  -> list_brackets requested, adding: %s" % self.list_brackets, 10)
            character_set = character_set + self.list_brackets
        if self.use_minus:
            self.log("  -> list_minus requested, adding: %s" % self.list_minus, 10)
            character_set = character_set + self.list_minus
        if self.use_underline:
            self.log("  -> list_underline requested, adding: %s" % self.list_underline, 10)
            character_set = character_set + self.list_underline

        # Remove homoglpys
        if self.remove_homoglyphs:
            self.log("Removing homoglyphs (look-alike characters): %s " % self.list_homoglyphs, 10)
            character_set = [char for char in character_set if char not in self.list_homoglyphs]

        self.list_final_charset = character_set

    def get_random_character(self, p):

        if p == "u":
            return secrets.choice(self.list_upper)

        if p == "l":
            return secrets.choice(self.list_lower)

        if p == "s":
            return secrets.choice(self.list_symbol)

        if p == "d":
            return secrets.choice(self.list_digits)

        if p == "b":
            return secrets.choice(self.list_brackets)

        if p == "m":
            return secrets.choice(self.list_minus)

        if p == "n":
            return secrets.choice(self.list_underline)

        if p == "p":
            return secrets.choice(self.list_punctuation)

        if p == "a":
            return secrets.choice(self.list_lower + self.list_digits)

        if p == "A":
            return secrets.choice(self.list_upper + self.list_digits)

        if p == "M":
            return secrets.choice(self.list_lower + self.list_digits + self.list_upper)

        if p == "N":
            return secrets.choice(self.list_lower + self.list_digits + self.list_upper + self.list_symbol)

        if p == "h":
            return secrets.choice(self.list_digits + self.list_lower[:6])

        if p == "H":
            return secrets.choice(self.list_digits + self.list_upper[:6])

        if p == "v":
            return secrets.choice(self.list_vowels_lower)

        if p == "V":
            return secrets.choice(self.list_vowels_upper)

        if p == "Z":
            return secrets.choice(self.list_vowels_lower + self.list_vowels_upper)

        if p == "c":
            return secrets.choice(self.list_consonant_lower)

        if p == "C":
            return secrets.choice(self.list_consonant_upper)

        if p == "z":
            return secrets.choice(self.list_consonant_lower + self.list_consonant_upper)

        return p

    def generate_pattern_based_password(self):
        self.log("Generating password based on pattern: %s" % self.password_pattern, 1)
        chars = []
        repeat = 0
        last_pattern = None

        pattern = iter(self.password_pattern)

        for p in pattern:
            # If the character is escaped, use as-is.
            if p == '\\':
                p = next(pattern)
                chars.append(p)
                last_pattern = p
                if self.debug:
                    print("Last pattern: %s" % p)
                continue

            # Repeat characters
            if p == "{":

                r = ""
                while True:
                    p = next(pattern)
                    if p == "}":
                        break
                    r = r + p

                repeat = int(r)

                for i in range(1, repeat):
                    chars.append(self.get_random_character(last_pattern))

                continue

            last_pattern = p
            if self.debug:
                print("Last pattern: %s" % p)
            chars.append(self.get_random_character(p))

            # Default is to ignore the item.

        return "".join(chars)

    def generate_random_password(self):
        self.log("Generating random password %s characters long" % self.password_length, 3)
        chars = []
        for x in range(0, self.password_length):
            chars.append(secrets.choice(self.list_final_charset))

        return "".join(chars)

    def generate_pass_phrase(self):
        self.log("Generating passphrase", 1)
        path = os.path.abspath(os.path.dirname(__file__))
        word_list_path = os.path.join(path, 'words.txt')

        with open(word_list_path) as infile:
            m = mmap.mmap(infile.fileno(), 0, access=mmap.ACCESS_READ)

        if self.debug:
            print("Counting words in dictionary...")

        # Index the file
        index = []
        while True:
            buffer = m.readline().decode("utf-8").strip()
            if buffer == "":
                break
            index.append(buffer)

        self.log("Total words in dictionary: %s " % len(index), 10)

        words = []

        for x in range(0, self.password_length):
            words.append(secrets.choice(index))

        return " ".join(words)

    def generate_password(self):

        if self.use_pattern:
            return self.generate_pattern_based_password()

        if self.use_words:
            return self.generate_pass_phrase()

        return self.generate_random_password()

    def render_password(self):
        self.render_charset()
        passwords = []

        for i in range(0, self.password_count):
            passwords.append(self.generate_password())

        passwords_per_row = int(80 / (self.password_length + 1))

        self.log("Printing %s passwords @ %s per row." % (self.password_count, passwords_per_row), 3)

        count = 0
        row = []

        for password in passwords:
            row.append(password)
            if count == self.password_count - 1 or len(row) == passwords_per_row:
                self.log("Rowcount reached. Printing row.", 10)
                print(" ".join(row))
                row = []
            count = count + 1




        if self.show_time:
            print("\nPassword generated in %s seconds" % (time.time() - self.start_time))
