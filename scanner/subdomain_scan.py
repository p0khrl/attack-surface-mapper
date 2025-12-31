import dns.resolver

COMMON_SUBDOMAINS = ["www", "mail", "ftp", "api", "dev", "test"]

def scan_subdomains(domain):
    found = []
    for sub in COMMON_SUBDOMAINS:
        try:
            full = f"{sub}.{domain}"
            dns.resolver.resolve(full, "A")
            found.append(full)
        except:
            pass
    return found
