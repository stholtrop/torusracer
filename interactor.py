from subprocess import Popen, PIPE
import sys

p1 = Popen([sys.argv[1]], stdin=PIPE, stdout=PIPE)
p2 = Popen([sys.argv[2]], stdin=PIPE, stdout=PIPE)


