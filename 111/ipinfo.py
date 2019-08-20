import json

import requests

IPINFO_URL = "http://ipinfo.io/{ip}/json"


def get_ip_country(ip_address):
    """Receives ip address string, use IPINFO_URL to get geo data,
       parse the json response returning the country code of the IP"""
    r = requests.get(IPINFO_URL.format(ip=ip_address))

    try:
        data = json.loads(r.content)
    except json.JSONDecodeError:
        raise Exception("API call content could not be decoded.")

    return data["country"].strip()


if __name__ == "__main__":
    print(get_ip_country("187.190.38.36"))
    print(get_ip_country("185.161.200.10"))
