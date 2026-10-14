#!/usr/bin/env python3

import os
import random

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

face = random.choice(list(FACES.values()))

print("\033[1;36m" + face + "\033[0m")
print("what?")
print(f"shell: {os.environ.get('SHELL', 'unknown')}")
