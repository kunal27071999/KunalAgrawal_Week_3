"""
12. Write not one finally block	

"""
"""
In programming, there may be some situation in which the current method ends up while handling some exceptions. But the method may require some additional steps before its termination, like closing a file or a network and so on.
So, in order to handle these situations, Python provides a keyword finally, which is always executed after try and except blocks. The finally block always executes after normal termination of try block or after try block terminates due to some exception.

Syntax:

try:
       # Some Code.... 

except:
       # optional block
       # Handling of exception (if required)

finally:
      # Some code .....(always executed)      

Important Points –

finally block is always executed after leaving the try statement. In case if some exception was not handled by except block, it is re-raised after execution of finally block.
finally block is used to deallocate the system resources.
One can use finally just after try without using except block, but no exception is handled in that case.
"""