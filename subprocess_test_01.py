import subprocess

clone_cmd = ' --branch main git@gitatron.local:support/pipeline_setup.git D:/PLE/pipeline/pipeline_setup/main-1'

# d = subprocess.Popen(['git', 'clone', clone_cmd], stdout=subprocess.PIPE, universal_newlines=True)
# print(d)
# output = d.stdout
# print(output)
# r = subprocess.call("git clone {}".format(clone_cmd), shell=True)
# print('r: ', r)
# print(r == 0)
d = subprocess.call('git clone{}'.format(clone_cmd), stdout=subprocess.PIPE, universal_newlines=True)
print(d)
output = d.stdout
print(output)
# output = r.stdout
# print(output)
# print(r.stdout)
# print(r.stderr)
# x = subprocess.Popen(['git', 'clone', clone_cmd], stdout=subprocess.PIPE, shell=True)
# print(x.communicate())
rr = ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
      '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__',
      '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
      '__subclasshook__', '__weakref__', 'args', 'check_returncode', 'returncode', 'stderr', 'stdout']
rrr = ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__',
       '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__',
       '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__',
       '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__',
       '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__',
       '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__',
       '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__',
       '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag',
       'numerator', 'real', 'to_bytes']
