# main.py, another module in the same folder
import greetings              # module name = file name
print(greetings.hello("Antti"))

from greetings import hello   # import one name
print(hello("Class"))

import greetings as g         # alias
print(g.hello("Aliases"))
