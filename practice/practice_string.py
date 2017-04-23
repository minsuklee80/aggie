Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import string
>>> dir(string)
['Formatter', 'Template', '_ChainMap', '_TemplateMetaclass', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_re', '_string', 'ascii_letters', 'ascii_lowercase', 'ascii_uppercase', 'capwords', 'digits', 'hexdigits', 'octdigits', 'printable', 'punctuation', 'whitespace']
>>> help(string)
Help on module string:

NAME
    string - A collection of string constants.

DESCRIPTION
    Public module variables:
    
    whitespace -- a string containing all ASCII whitespace
    ascii_lowercase -- a string containing all ASCII lowercase letters
    ascii_uppercase -- a string containing all ASCII uppercase letters
    ascii_letters -- a string containing all ASCII letters
    digits -- a string containing all ASCII decimal digits
    hexdigits -- a string containing all ASCII hexadecimal digits
    octdigits -- a string containing all ASCII octal digits
    punctuation -- a string containing all ASCII punctuation characters
    printable -- a string containing all ASCII characters considered printable

CLASSES
    builtins.object
        Formatter
        Template
    
    class Formatter(builtins.object)
     |  Methods defined here:
     |  
     |  check_unused_args(self, used_args, args, kwargs)
     |  
     |  convert_field(self, value, conversion)
     |  
     |  format(*args, **kwargs)
     |  
     |  format_field(self, value, format_spec)
     |  
     |  get_field(self, field_name, args, kwargs)
     |      # given a field_name, find the object it references.
     |      #  field_name:   the field being looked up, e.g. "0.name"
     |      #                 or "lookup[3]"
     |      #  used_args:    a set of which args have been used
     |      #  args, kwargs: as passed in to vformat
     |  
     |  get_value(self, key, args, kwargs)
     |  
     |  parse(self, format_string)
     |      # returns an iterable that contains tuples of the form:
     |      # (literal_text, field_name, format_spec, conversion)
     |      # literal_text can be zero length
     |      # field_name can be None, in which case there's no
     |      #  object to format and output
     |      # if field_name is not None, it is looked up, formatted
     |      #  with format_spec and conversion and then used
     |  
     |  vformat(self, format_string, args, kwargs)
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    
    class Template(builtins.object)
     |  A string class for supporting $-substitutions.
     |  
     |  Methods defined here:
     |  
     |  __init__(self, template)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  safe_substitute(*args, **kws)
     |  
     |  substitute(*args, **kws)
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  delimiter = '$'
     |  
     |  flags = 2
     |  
     |  idpattern = '[_a-z][_a-z0-9]*'
     |  
     |  pattern = re.compile('\n    \\$(?:\n      (?P<escaped>\\$)..._a-z][_a-...

FUNCTIONS
    capwords(s, sep=None)
        capwords(s [,sep]) -> string
        
        Split the argument into words using split, capitalize each
        word using capitalize, and join the capitalized words using
        join.  If the optional second argument sep is absent or None,
        runs of whitespace characters are replaced by a single space
        and leading and trailing whitespace are removed, otherwise
        sep is used to split and join the words.

DATA
    __all__ = ['ascii_letters', 'ascii_lowercase', 'ascii_uppercase', 'cap...
    ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    hexdigits = '0123456789abcdefABCDEF'
    octdigits = '01234567'
    printable = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTU...
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    whitespace = ' \t\n\r\x0b\x0c'

FILE
    c:\users\user\appdata\local\programs\python\python35-32\lib\string.py


>>> string.digits
'0123456789'
>>> string.ascii_letters
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
>>> string.hexdigits
'0123456789abcdefABCDEF'
>>> from mcpi.minecraft import Minecraft
>>> dir(Minecraft)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'create', 'getBlock', 'getBlockWithData', 'getBlocks', 'getHeight', 'getPlayerEntityIds', 'postToChat', 'restoreCheckpoint', 'saveCheckpoint', 'setBlock', 'setBlocks', 'setting']
>>> help(Minecraft.create)
Help on function create in module mcpi.minecraft:

create(address='localhost', port=4711)

>>> 
