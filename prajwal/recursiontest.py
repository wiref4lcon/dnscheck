import dns.name
import dns.message
import dns.query
import dns.flags
import dns.resolver
import sys
def recursion_test(domain,name_server):
	ADDITIONAL_RDCLASS = 65535
	domain = dns.name.from_text(domain)
	if not domain.is_absolute():
	    domain = domain.concatenate(dns.name.root)
	request = dns.message.make_query(domain, dns.rdatatype.ANY, )
	request.flags |= dns.flags.AD
	request.find_rrset(request.additional, dns.name.root, ADDITIONAL_RDCLASS,
	                   dns.rdatatype.OPT, create=True, force_unique=True )
	try:
		response = dns.query.udp(request, name_server, timeout=3)
		falgs = str(response)
		falgs = falgs.split("\n")
		for lines in falgs:
			if ("flags" in lines) and ("RA" in lines):
				print name_server +" : supports recursion"
	except:
		pass