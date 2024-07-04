"""According to wikipedia - Debugging is the process of finding and resolving
defects or problems within a computer program that prevent correct operation
of computer software or a system."""


"""modules :
modules contains useul  classes and functions written by developers"""

# why debugging
# 1.) our program is not running and causing unexpected errors.
# 2.) our program is working fine but not working the same way we want.

"""to use debugging we will use PDB module 
i,e  import pdb 

# Steps for debugging
# 1.) set trace
# 2.) execute code Line by line
# 
write pdb.set_trace() in any line from which you want to start debugging
terminal commands:

l > you are at which line
n > to execute the line
q > quite debugger
c > execute the code line by line 

"""

import pdb

pdb.set_trace()