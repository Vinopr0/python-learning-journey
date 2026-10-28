# What is PyPi?

PyPi is the location where open-source libraries and packages are stored and are where libraries downloaded from `pip install _` are taken from. There are hundreds of packages. 

# What are modules?

.py files that can be called from another file.

You can import modules as

```
from my_module import my_function

my_function()
```

And you cna aggregate these modules, creating a...


# What is a package?

An aggregation of various python scripts (modules) into a folder. A subpackage would be a subfolder of the package. A `__init__.py` makes python understand it is a package directory. the file does not need anything, but needs to be there so that python knows this is not a regular dir.  