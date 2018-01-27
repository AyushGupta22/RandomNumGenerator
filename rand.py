import sys
from time import gmtime, strftime

def random(min, max,n=1, seed=-1):
    limit = max-min+1
    sLimit = limit*2
    if seed == -1:
        seed = int(strftime("%Y%m%d%H%M%S", gmtime()))
    result = list()
    for i in range(n):
        seed = (((seed * 214013 + 2531011) >> 16) & 32767)
        t = (seed)%sLimit + 1
        if t > int(1.5*limit):
            t=t-limit;
        elif t > limit:
            t = t-int(limit/2);
        result.append(min+t)
    return result;
