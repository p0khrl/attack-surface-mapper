from scanner.subdomain_scan import scan_subdomains
from scanner.header_scan import scan_headers

def main():
    target = input("Enter target domain (example.com): ").strip()

    print(f"[+] Scanning subdomains for {target}")
    subdomains = scan_subdomains(target)
    for s in subdomains:
        print(f"  - {s}")

    print(f"\n[+] Scanning headers for {target}")
    headers = scan_headers(target)
    for k, v in headers.items():
        print(f"{k}: {v}")

if __name__ == "__main__":
    main()
