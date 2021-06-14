"""
19. Note on else block with try except finally

"""
"""
Try: This block will test the excepted error to occur
Except:  Here you can handle the error
Else: If there is no exception then this block will be executed
Finally: Finally block always gets executed either exception is generated or not
Syntax:




try:
       # Some Code.... 

except:
       # optional block
       # Handling of exception (if required)

else:
       # execute if no exception

finally:
      # Some code .....(always executed)
Let’s first understand how the try and except works –

First try clause is executed i.e. the code between try and except clause.
If there is no exception, then only try clause will run, except clause will not get executed.
If any exception occurs, the try clause will be skipped and except clause will run.
If any exception occurs, but the except clause within the code doesn’t handle it, it is passed on to the outer try statements. If the exception is left unhandled, then the execution stops.
A try statement can have more than one except clause.
"""