
This uses the Python inspect library to get information about live modules. It is designed to tell you what modules (and dependencies) are being imported by the target. It runs the target and then inspects the loaded modules.  This is, at best, an alpha PoC release.  

Currently, it gets the Sha1. Sha256 is coming soon.  

To run:  
$ python py_omnibor.py {target.py}  
Ex:  
$ python py_omnibor.py test_1.py  
This will run the target file and create a file called OmniBor.sha1 that will contain the gitoids for the target files.  
  
Output written to OmniBor.sha1 looks like:  

gitoid:blob:sha1:sre_compile.py:73f19a12862e1fb633e6e99444d23cd1bcd9b54f
gitoid:blob:sha1:enum.py:55e688744867714deffaec691627fdb6094384fc

TODO:  
Add the .pyc file (admission: I forgot to do that :-)  
Eliminate "builtins" in the output. They do not represent a file.  
And the code needs to be cleaned, etc. 

Author: Robert Marion  
Date: May 2023  
License: MIT  
