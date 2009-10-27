from domains.models import Whois


def get_domain_list_whois(domain_list, tld):
    key_domains = {}
    for domain in domain_list:
        key_name = '%s.%s' % (domain.name, tld)
        key_domains[key_name] = domain
    whois_list = Whois.get_by_key_name(key_domains.keys())
    attr_name = tld + '_expiration'
    for whois in whois_list:
        if whois:
            key_name = whois.key().name()
            domain = key_domains[key_name]
            setattr(domain, attr_name, whois.expiration)
