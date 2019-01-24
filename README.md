# pwgen_secure - Secure Python random password generator

Generate cryptographically secure random passwords with specified character sets, patterns, or lengths.

## Quickstart: How do I make passwords?

### Installation

pwgen_secure requires Python 3.6 above because it uses the `secrets` module for cryptographically secure random numbers.
("cryptographically secure" is a relative term. Read the *Security* section below).

If you do not have Python 3.6, you can download and install it from [python.org](https://www.python.org/downloads/).

### Installation script

For your copy / paste pleasure. 

```
sudo su
pip install pwgen_secure docopt
cd /usr/src/
git clone https://github.com/mjmunger/pwgen_secure
cd pwgen_secure
chmod +x ./install.sh
./install.sh
```

### Usage

    usage: spwgen [ -v ... ] [options] <class> [<class-option>] 


### Examples
Here are examples for you, Captain Impatient...

#### Random password for a website, and show the timing

```
spwgen slut 16
```

#### Random MAC address:
```
spwgen p 'h{2}:h{2}:h{2}:h{2}:h{2}:h{2}' 
```

...or using a magic class

```
spwgen mac
```
#### Random three word pass phrase:
```
spwgen w 3
```

#### Create a google-style password:

```
spwgen google
```

#### Create one that's strong and easy to do on a phone
```
spwgen iphone
```

or

```
spwgen android
```

#### Escape the h so it starts with h

```
spwgen p '\hu{12}' 
```
### Full Usage

```
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
```

## But why?

There are a number of reasons we wrote spwgen, but the main reason was: we wanted a password generator that was flexible and which would use the best available sources of entropy.  

### Secure by default
By default, pwgen creates passwords easy for a human to memorize. You have to use the `-s` option to get secure
passwords. `pwgen_secure` generates secure passwords *by default* ... because users rarely rtfm, and usually use
default settings.

### Flexible

`pwgen` is not flexible. Want to generate random mac addresses? Can't. Need some other pattern? Can't.
`pwgen_secure` can.

### Uses the `secrets` module

The secrets module automatically uses the best source of randomness available on your system, which gives us the best
chance and making secure passwords. (See "Cryptographically secure" below). 

# Support and Issues

For support, problems, and issues, [file an issue on github](https://github.com/mjmunger/pwgen_secure) 

# Security

## How secure can it be?

"Cryptographically secure" is a somewhat relative term. The secrets module actually "[...provides access to the most secure source of randomness that your operating system provides](https://docs.python.org/3/library/secrets.html#random-numbers)". Thus, if you do not have a good source of randomness on your computer, you will not get good secure numbers. This is entirely dependent on whether or not your chipset has a [has a TRNG](https://software.intel.com/en-us/articles/intel-digital-random-number-generator-drng-software-implementation-guide).

## Password strength analysis

Password strength is a somewhat nebulous term. We would like it to mean: "This password is hard to crack", however the reality is that there are a number of ways to crack a password. The strength analysis this program performs is a search space calculation, which is compared against current cracking ability.

### How we calculate search space

The command `spwgen.py -a strong` generates a password like: `SSWltcnwo0pARJY7`. This creates a possible search space of 1 match in 48,453,916,488,902,607,769,120,106,730 (4.8 x 10^28) possibilities. Now, we have a 1 in 2 chance of finding the password of we search half of that search space, and so, that reduces the search space to (2.4 x 10^28), which is still enormous. Now, given current cracking ability, we can try 100,000,000,000,000 attempts per second, we can divide out the possible combinations (2.4 x 10^28) by 1 x 10^14. This gives us the total number of seconds required to search 50% of the password's search space.

### What we mean by "crack"

For the purposes of this calculator, a password is deemed to have been "cracked" after 50% of the search space can exhaustively be searched.

### How we calculate "strength"

The strength of a password is determined by how likely a user will die before the password is brute forced, given current cracking technology. The target is to have a password that will take more than 100 years to crack. This way, a person can protect their data with a given password for their lifetime. Of course, as hashing and cracking technology increases, the speed we use to calculate this strength will need to be updated.

Stengths are therefore shown as:

* Requires less than 1 year to crack: "Awful. Don't use this."
* Requires 1-10 years: Very weak
* Requires 10-50 years: Weak
* Requires 50-75 years: OK
* Requires 75-100 years: Strong
* Requires 100+ years: Very strong

This *does not guarantee* your password is strong, but it's a pretty damn good for most applications. Additionally, if you have a poor source of entropy on your computer, these calculations are all but meaningless. If you are really interested in having excellent, high-quality, secure passwords, make sure you have a computer with a chipset that can produce true random numbers with a TRNG or just pseudo-random numbers with a PRNG. See: [Intel's random number generator implementation guide](https://software.intel.com/en-us/articles/intel-digital-random-number-generator-drng-software-implementation-guide) for more discussion.

## Distribution specific installation information

### Debian specific installation of Python 3.6.

Debian stretch does not yet have Python 3.6 in an repository package, therefore, you can compile from scratch:

Prep your system:
```
apt build-dep python
apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
```

Download Python 3.6 for Linux, and extract to /usr/src/, then:
```
./configure
make
make install
```

Secrets is part of the core library as of v3.6, so there is nothing else to install.

## References
* [Python secrets](https://docs.python.org/3/library/secrets.html#random-numbers)

## Sources and contributions
* Pattern functions based on [Keepass password generator](https://keepass.info/help/base/pwgenerator.html)
* mmap usage for words.txt based on [Python fastest way to process large file](https://stackoverflow.com/questions/30294146/python-fastest-way-to-process-large-file)
* English words list provided by [dwyl/englishwords](https://github.com/dwyl/english-words)

## Acknowledgements

Thank you to [Theodore Ts'o](https://en.wikipedia.org/wiki/Theodore_Ts%27o) for his various contributions to the Linux project, including [pwgen](https://github.com/tytso/pwgen), [e2fsprogs](https://en.wikipedia.org/wiki/E2fsprogs), and [ext4 file system](https://en.wikipedia.org/wiki/Ext4), which are things we all use every day. Theodore Ts'o is imminently qualified to write the original pwgen, and this project hopes to follow in it's footsteps.