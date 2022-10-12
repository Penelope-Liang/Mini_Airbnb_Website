import re

# name you reg in the format <name> + Reg
# register reg
emailReg = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
AccNameReg = r'^\w+( +\w+)*$'
passwordReg = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[#@$!%*?&()_])[A-Za-z\d#@$!%*?&()_]{6,}$'

