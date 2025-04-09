This system allows any user to Create, Read, Update and Delete items in a virtual database using sqlite3. This project is simple and yet handles lots of missinputs made on purpose of by mistake by the user. 
it should be easy for any user to understand how it works and should inform most problems and its causes so users can use it properly. Also, it consists of 4 archives, each has it's own classes separated 
by function and are all called on main.py.

Here are some of the key breakpoints in the code:

Message of item added if there is an error is still appearing --> changed the logic of how the function was called. 
It only receives the name parameter now and it compares. the pront was moved to be outside the original block

Update and deleted functions not being recongnized inside class item_manager --> identation error, easy but took a while to notice

There is a cache file that needs to be deleted, because it doesn't update as the code is updated --> change in some IDE configurations so it updates automatically.(It won't be a problem to any user,
no need to create a automated process to delete cache folder.)

The user can add an item without name --> just accept a name if its length is >= 1.

The user can crash the program if the quantity value exceeds 2**32 -1. --> put a error case if he tries to do so.
