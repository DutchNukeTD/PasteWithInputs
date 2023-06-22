# PasteWithInputs
## By Golan van der Bend
22-06-2023 Python 3 For Nuke 13.0+
## info 
Copy and paste nodes while pasted nodes keep there original inputs. Script automatically copy and paste for you.  
ctrl+shift+v 
## Install tips
1. Add the file 'GB_pasteWithInputs.py' to the '.nuke' folder location on your computer. If you don't know where that is see: https://support.foundry.com/hc/en-us/articles/207271649-Q100048-Nuke-Directory-Locations.  
2. Add the following text to your menu.py file:
   
   import GB_pasteWithInputs  
   nuke.menu('Nodes').addCommand( 'Golan gizmos/Golan/pasteWithInputs', 'GB_pasteWithInputs.pasteWithInputs()', 'ctrl+shift+v')
