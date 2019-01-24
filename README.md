# PyRPG - Secure Python random password generator

Generate cryptographically secure random passwords with specified character sets, patterns, or lengths.

## Quickstart: How do I make passwords?

You have two tools: rpg and frpg.
1. `rpg` generates a random password at the command line.
1. `frpg` reads a file, and replaces instances of `#RND#` with a securely generated password. 

### Usage:

```
rpg [character set options | magic class] [length | pattern]
```
and 
```
frpg /path/to/file [character set options | magic class] [length | pattern]
```

### Examples
Here are examples for you, Captain Impatient...

#### Random password for a website, and show the timing

```
rpg slut 16
```

#### Random MAC address:
```
rpg p 'h{2}:h{2}:h{2}:h{2}:h{2}:h{2}' 
```

...or using a magic class

```
rpg mac
```

#### Create passwords in a file where the #RND# placeholder is

Use the `strong` magic class

```
frpg /path/to/file strong
``` 

Do it the hard way:

```
frpg /path/to/file ul 21
```

Make crappy passwords in the file:

```
frpg /path/to/file d{4}
```

Make your users sorry they were ever born:

```
frpg /path/to/file painful
```
#### Random three word pass phrase:
```
rpg w 3
```

#### Create a google-style password:

```
rpg google
```

#### Create one that's strong and easy to do ona  phone
```
rpg iphone
```

or

```
rpg android
```

#### Escape the h so it starts with h

```
rpg p '\hu{12}' 
```

#### Character set options:

```
u    Include upper case characters: A-Z
l    Include lower case characters: a-z
s    Include symbol characters: !@#$%^&*
d    Include digits: 0-9
b    Include bracket characters: {}[]()<>
m    Include the minus character: -
n    Include the underscore character: _
```

#### Extended options:
```
w    Generate a password based on words
p    Generate the password based on the given pattern (requires the pattern argument)
e    Exclude look-alike characters (homoglyphs): 1iIO0
```

#### Fun stuff:
```
t    Show how long it took to generate the passwords.
g    Show debugging information
```

For all character sets (except pattern generation, "p"), you must specify the password length as the second
argument. For all options except w and p, the length specification will specify the string character length. For
w (word based password), the length argument will specify the number of words in the resulting password.

When p is specified, the second argument must be a pattern, not a length. (See "Pattern" below).

#### Patterns:

The pattern defines the layout of the resulting password. Each character in the pattern dictates a character
class that will be substituted at that position in the pattern. Characters that do not represent a given character
class will be substituted as-is.

For example:

`uull-dddd` will result in:

* Two upper case characters for the first two characters of the pattern, followed by:
* Two lower case characters for the next two characters, followed by:
* "-" followed by:
* Four digits

Use the following place holders to define your pattern:

*Base class place holders:*
```
u  Upper case characters: A-Z 
l  Lower case characters: a-z
s  Symbols: !@#$%^&*
d  Digits: 0-9
b  Bracket characters: {}[]()<>
m  The minus character: -
n  The underscore character: _
p  Punctuation: ,.;:
```

*Combination and sub-class place holders:*

```
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
```

*Special placeholders*
```
\    Escapes the proceeding character, and tells the generator to print it "as-is".
{n}  Print the previous character n times.
```

#### Magic classes

The following magic classes are short hand expressions that will create
random passwords according to a specific recipe.
```
otp         Generate a base32 compliant secret for TOPT 2FA authentication
google      Generate Google-style app passwords e.g, ofgl ruwd ngzs iphh
iphone      Generate passwords that are easy to enter on the default iPhone keyboard
android     Generate passwords that are easy to enter on the default Android keyboard
pin4        Generate a random 4-digit pin
pin6        Generate a random 6-digit pin
mac         Generate a random mac address
strong      Generate a strong password
ridiculous  Generate a ridiculous password
ludicrous   Generate a ludicrously strong password
painful     Really? Wow. 
```

# Security

"Cryptographically secure" is a somewhat relative term. The secrets module actually "[...provides access to the most secure source of randomness that your operating system provides](https://docs.python.org/3/library/secrets.html#random-numbers)". Thus, if you do not have a good source of randomness on your computer, you will not get good secure numbers. This is entirely dependent on [your chipset](https://software.intel.com/en-us/articles/intel-digital-random-number-generator-drng-software-implementation-guide).

# Support and Issues

For support, problems, and issues, file an issue on github:
  https://github.com/mjmunger/pyrpg 

## Installation

PyRPG requires Python 3.6 above because it uses the `secrets` module for cryptographically secure random numbers*.

If you do not have Python 3.6, you can download and install it from [python.org](https://www.python.org/downloads/).

### Installation script

For your copy / paste pleasure. 

```
sudo su
cd /usr/src/
git clone https://github.com/mjmunger/pyrpg.git
cd pyrpg
chmod +x ./install.sh
./install.sh
exit
```

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
