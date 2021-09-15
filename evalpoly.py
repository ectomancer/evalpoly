from typing import List, Tuple, Union

Container = Union[List[int], Tuple[int]]

def evalpoly(c: Container, x: float) -> float:
    '''Pure Python evalpoly, ported from JavaScript by kgryte @github.com
    MIT License Copyright (c) 2016 The Compute.io Authors.
    c is a list or tuple of ordered polynomial coefficents.
    Same syntax as Julia evalpoly, Julia @evalpoly not implemented.
    function evalpoly( c, x ) {
	var p;
	var i;
	
	i = c.length;
	if ( i < 2 || x === 0 ) {
		if ( i === 0 ) {
			return 0;
		}
		return c[ 0 ];
	}
	i -= 1;

	// Use Horner's rule (http://en.wikipedia.org/wiki/Horner's_method) to achieve efficient computation...
	p = c[ i ]*x + c[ i-1 ];
	i -= 2;
	while ( i >= 0 ) {
		p = p*x + c[ i ];
		i -= 1;
	}
	return p;'''
    i = len(c)
    if i < 2 or not x:
        if not i:
            return 0
        return c[0]
    i -= 1
    #Use Horner's rule (http://en.wikipedia.org/wiki/Horner's_method) to achieve efficient computation...
    p = c[i]*x + c[i - 1]
    i -= 2
    while i >= 0:
        p = p*x + c[i]
        i -= 1
    return p
