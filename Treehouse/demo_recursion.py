def tri_recursion(k):
	if(k>0):
	   x = tri_recursion(k-1)
	   result = k+x
	   print("{} + ({}) = {}".format(k, x, result))
	else:
	   result = 0
	return result

print("\n\nRecursion Example Results")
tri_recursion(6)
