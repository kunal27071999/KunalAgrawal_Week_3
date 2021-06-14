"""
3. Write pythons exceptions hierarchy

"""

"""
BaseException
+-- SystemExit
+-- KeyboardInterrupt
+-- GeneratorExit
+-- Exception
    +-- StopIteration
    +-- StandardError
    |    +-- BufferError
    |    +-- ArithmeticError
    |    |    +-- FloatingPointError
    |    |    +-- OverflowError
    |    |    +-- ZeroDivisionError
    |    +-- AssertionError
    |    +-- AttributeError
    |    +-- EnvironmentError
    |    |    +-- IOError
    |    |    +-- OSError
    |    |         +-- WindowsError (Windows)
    |    |         +-- VMSError (VMS)
    |    +-- EOFError
    |    +-- ImportError
    |    +-- LookupError
    |    |    +-- IndexError
    |    |    +-- UnboundLocalError
    |    +-- ReferenceError
    |    +-- RuntimeError
    |    |    +-- NotImplementedError
    |    +-- ValueError
    |         +-- UnicodeError
    |              +-- UnicodeDecodeError
    |              +-- UnicodeEncodeError
    |              +-- UnicodeTranslateError

"""