#!/usr/bin/env python3
"""
usage: spwgen [ -v ... ] [options] <class> [<class-option>]

options:
    -v          Be verbose.
    -d          Debug mode. Same as -vvvvvvvvvvv
    -t          Show how long it took to generate that password.
    -n=<count>  Generate n passwords.
    -a          Show strength analysis of the generated password

classes:

    There are three classes:
      1. magic classes        Known good patterns to generate passwords for every day use. (You probably want this).
      2. character classes    Allows you to specifically define which character sets are used to generate your password.
      3. pattern classes      Allows you to define a custom pattern for password generation.

    magic classes:

        The following magic classes are short hand expressions that will create random passwords according to a
        specific recipe:

        google      Generate Google-style app passwords e.g, ofgl ruwd ngzs iphh
        iphone      Generate passwords that are easy to enter on the default iPhone keyboard
        android     Generate passwords that are easy to enter on the default Android keyboard
        pin4        Generate a random 4-digit pin
        pin6        Generate a random 6-digit pin
        mac         Generate a random mac address
        banking     Generate a random password suitable for protecting bank accounts.
        strong      Generate a strong password
        ridiculous  Generate a ridiculous password
        ludicrous   Generate a ludicrously strong password
        painful     Really? Wow.

        Examples:

            `spwgen strong` outputs something like: `f5BjepTYdpUeJOhG`
            `spwgen mac` outputs something like: `46:06:e3:86:30:79`

    character classes:

        Character classes tell the password generator what character sets to use when generating the password. Each
        character class is represented by a single letter.

        When you use character classes, you *must* specify a password length as the class option.

        Available character classes are:

        u    Include upper case characters: A-Z
        l    Include lower case characters: a-z
        s    Include symbol characters: !@#$%^&*
        d    Include digits: 0-9
        b    Include bracket characters: {}[]()<>
        m    Include the minus character: -
        n    Include the underscore character: _

        Extended options:
        w    Generate a password based on words
        p    Generate the password based on the given pattern (requires the pattern argument)
        e    Exclude look-alike characters (homoglyphs): 1iIO0

        Examples:
            `spwgen slu 16` outputs something like: `#eZRnU%HlShbB**^`
            `spwgen dbmslu 32`  outputs something like: `hahdJ(]Vizk@SW5RpKc(x($<8fwRC7HX`

    pattern classes:

        Pattern classes generate passwords based on the user specified pattern. The pattern defines the layout of the
        resulting password. Each character in the pattern dictates a character class that will be substituted at that
        position in the pattern.

        Characters that do not represent a specific character class will be substituted as-is.

        Use the following place holders to define your pattern:

        Base class place holders:
            u  Upper case characters: A-Z
            l  Lower case characters: a-z
            s  Symbols: !@#$%^&*
            d  Digits: 0-9
            b  Bracket characters: {}[]()<>
            m  The minus character: -
            n  The underscore character: _
            p  Punctuation: ,.;:

        Combination and sub-class place holders:
            a  lower-case alphanumeric: a-z and 0-9
            A  Upper-case alphanumeric: A-Z and 0-9
            M  Mixed-case alphanumeric: a-z, A-Z, and 0-9
            N  Mixed-case alphanumeric + symbols: a-z, A-Z, 0-9 + !@#$%^&*
            h  Lower case hex character: 0-9 and a-f
            H  Upper case hex character: 0-9 and A-F
            v  Lower case vowel: aeiou
            V  Upper case vowel: AEIOU
            Z  Mixed case vowel: AEIOU and aeiou
            c  Lower case consonant: bcdfghjklmnpqrstvwxyz
            C  Upper case consonant: BCDFGHJKLMNPQRSTVWXYZ
            z  Mixed case consonant: bcdfghjklmnpqrstvwxyz and BCDFGHJKLMNPQRSTVWXYZ

        Special placeholders
            \    Escapes the proceeding character, and tells the generator to print it "as-is".
            {n}  Print the previous character n times.

        Example:
            `uull-dddd` will result in:
            1. Two upper case characters for the first two characters of the pattern, followed by:
            2. Two lower case characters for the next two characters, followed by:
            3. "-" followed by:
            4. Four digits

"""
from docopt import docopt
from pwgen_secure import rpg
from pprint import pprint

if __name__ == "__main__":
    args = docopt(__doc__)

    r = rpg.Rpg(args['<class>'], args['<class-option>'])
    r.setup_options(args)
    r.render_password()
