import dns.name
import dns.message
import dns.query
import dns.flags
import dns.resolver
import sys
def resolve_test(domain,name_server):
	resolver = dns.resolver.Resolver()
	resolver.lifetime =3
	resolver.nameservers = [name_server]
	try:
		answers = resolver.query(domain, 'A')
		for rdata in answers:
			ipaddrlist = rdata.address
		if len(ipaddrlist) >0 :
			print name_server+ " : has open resolver"
	except:
		return "none"