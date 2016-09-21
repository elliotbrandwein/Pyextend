Pyextend
==================================================

What it does
--------------------------------------
This function behaves just the .extend function in Jquery, execpt for all Mapping and Mutable Sequence types (a.k.a dicts and lists). This means you can now get deep and shallow copies of your dicts and lists in python. 

Learn how to use it
--------------------------------------
Read up on how to use the jquery version of this function here: https://api.jquery.com/jquery.extend/


Differences between this and jquery
--------------------------------------
Obviously I couldn’t replicate all the functionality of the .extend but this method replicates 99% of what the .extend function in jquery does. That being said I have made changes in the following cases so that pyextend will behave differently then .extend.

- If there is no dict or list as an argument, pyextend will return a blank dict
- If there is only one dict or list as an argument, pyextend will return that dict/list ( the jquery version merged that dict/list into jquery, obviously something I can’t do) 
- If there is a string as an input, extend in Jquery would parse it. Pyextend however will just ignore it. 
