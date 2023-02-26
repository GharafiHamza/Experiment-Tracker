import trace
import numpy as np

def extrace(fun):
    def wrapper(*args):
        tracer = trace.Trace(trace=1, count=1)
        tracer.runfunc(fun,*args)
        return tracer.results()
    return wrapper

if __name__ == "__main__":

    @extrace
    def add(a, b):
        if a < b:
            arr = np.array([a, b])
        else:
            arr = [0]
        return np.sum(arr)

    add(2,3).write_results(show_missing=True, summary=False, coverdir="coverage")