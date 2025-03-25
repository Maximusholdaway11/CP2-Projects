#What is tracing
#python -m trace --trace C:\Users\max.holdaway\Documents\CP2-Projects\debugging_notes\tracing.py
import trace
import sys

"""

Event types:
call - when function is called
line - when a new line is executed
return - when the function returns a value
exception - when an exception is raised

"""

def trace_calls(frame, event, arg):
    if event == 'call':
        print(f'Caling function {frame.f_code.co_name}')
    elif event == 'line':
        print(f'Executing line: {frame.f_lineno} in {frame.f_code.co_name}')
    elif event == 'return':
        print(f'{frame.f_code.co_name} returned {arg}')
    elif event == 'exception':
        print(f'Exception in {frame.f_code.co_name}: {arg}')
    return trace_calls


sys.settrace(trace_calls)

"""

--trace (displays function lines as they are executed)
--count (displays amont of times functions are used)
--listfuncs (displays which functions are in the project)
--trackcalls (displays the relationship between all the functions)

"""

tracer = trace.Trace(count=False, trace=True)

def add(a, b):
    c = a + b
    return c

def subtract(a, b):
    c = a - b
    return c

addition = add(1, 2)
sub = subtract(1, 2)
print(addition)
print(sub)
tracer.run('print(subtract(1, 2))')