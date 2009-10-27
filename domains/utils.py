from domains.models import Whois


def get_domain_list_whois(domain_list, tld):
    whois_list = Whois.get_by_key_name(
        ['%s.%s' % (domain.key().name(), tld) for domain in domain_list])
    attr_name = tld + '_expiration'
    for domain, whois in zip(domain_list, whois_list):
        if whois:
            setattr(domain, attr_name, whois.expiration)
