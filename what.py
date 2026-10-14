#!/usr/bin/env python3

import sys
import os
import random

NULL="\033[0m"
CYAN = "\033[1;36m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
PURPLE = "\033[1;35m"

FACES = {
    "happy": r"""
       |         |

    \               /
     \             /
      \___________/
    """,

    "sad": r"""
        |        |

        __________
       /          \
      /            \  
    """,

    "neutral": r"""
        |        |

    _________________
    """,

    "angry": r"""
        \        /
        |        |
        __________
       /          \
      /            \        
    """,

    "sleepy": r"""  
                     z 
                    Z
        _         _

           _____
    """,            
}

if len(sys.argv) > 1:
    name = sys.argv[1].lower()

    if name in FACES:
        face = FACES[name]
    else:
        print(f"unknown face: {name}")
        print("available faces:", ", ".join(FACES.keys()))
        sys.exit(1)
else:
    face = random.choice(list(FACES.values()))

print(CYAN + face + NULL)
print("what?")
print(f"shell: {os.environ.get('SHELL', 'unknown')}")
