import dns.name
import dns.message
import dns.query
import dns.flags
import dns.resolver
import sys
import prajwal.resolvertest
import prajwal.recursiontest
def main():
	name_server =sys.argv[1]
	domain = "www.google.com"
	print "sds"
 	prajwal.recursiontest.recursion_test(domain,name_server)
 	prajwal.resolvertest.resolve_test(domain,name_server)

if __name__ == '__main__':
	main()



	