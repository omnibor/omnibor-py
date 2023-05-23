
This uses the Python inspect library to get information about live modules. It is designed to tell you what modules (and dependencies) are being imported by the target. It runs the target and then inspects the loaded modules.  This is a beta PoC release.  

Currently, it gets the Sha1. Sha256 is coming soon.  

To run:  
$ python py_omnibor.py {target.py}  
Ex:  
$ python py_omnibor.py test_1.py  
This will run the target file and create a file called OmniBor.sha1 that will contain the gitoids for the target files.  
  
There is an optional flag: --append-manifest  
Ex:  
$ python  py_omnibor.py --append-manifest test_1.py  
This will add the manifest to the .pyc file. This feature, at this time, is debatable because pyc files are defined as having the following:  
* A four-byte magic number,  
* A four-byte modification timestamp, and  
* A marshalled code object.  
I have tested adding the manifest using Python version 3.8.10 on both Windows and Ubuntu. I was able to run the modified pyc files. However, there is no guarantee this will work on future (or even older versions) of Python as doing so is undefined.  

Output written to OmniBor.sha1 looks like:  

gitoid:blob:sha1:sre_compile.py:73f19a12862e1fb633e6e99444d23cd1bcd9b54f
gitoid:blob:sha1:enum.py:55e688744867714deffaec691627fdb6094384fc

Note: test_2.py requires the "requests" library. Doing so is optional but you will get more results if you include it. py_omnibor will let you know that something has not been included.  

Author: Robert Marion  
Date: May 2023  
License: MIT  
