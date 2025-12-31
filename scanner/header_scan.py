import requests

def scan_headers(domain):
    try:
        response = requests.get(f"http://{domain}", timeout=5)
        return response.headers
    except Exception as e:
        return {"error": str(e)}
