#!/usr/bin/env python3

import sys
from pwgen_secure import rpg

r = rpg.Rpg(sys.argv)
r.render_password()
