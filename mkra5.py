import requests
import socket
from ping3 import ping
import time

def get_ip_addresses(url):
    try:
        response = requests.get(url)
        domain = url.split("//")[-1].split("/")[0]
        ip_addresses = socket.gethostbyname_ex(domain)
        return ip_addresses
    except Exception as e:
        print("An error occurred:", e)

def test_website_responsiveness(url, country_name, country_code):
    target_url = url.split("//")[-1].split("/")[0]
    response_time = ping(target_url, unit='ms', timeout=2, size=32)
    if response_time is not None:
        if response_time < 100:
            speed_status = "Very fast"
            color = "\033[92m"
        elif response_time < 300:
            speed_status = "Fast"
            color = "\033[93m"
        else:
            speed_status = "Slow"
            color = "\033[91m"
        print(f"Response time from \033[94m{country_name}\033[0m ({country_code}): {color}{response_time} ms ({speed_status})\033[0m - {time.strftime('%H:%M:%S')}")
    else:
        print(f"\033[91mConnection timeout out from {country_name}\033[0m ({country_code}) - {time.strftime('%H:%M:%S')}")
url = input("Please enter the website URL: ")
ip_addresses = get_ip_addresses(url)
ip_addresses_list = ip_addresses[2]
print("IP addresses and ports associated with the weite:")
previous_color = ""
for index, ip in enumerate(ip_addresses_list, start=1):
    color = "\033[91m" if ip.startswith('104') else "\033[93m" if ip.startswith('172') else "\033[92m"
    port = 80
    reset_color = "\033[0m"
    print(f"Address number {index}: {color}{ip}\033[0m (Default port {color}\033[95m{port}{reset_color}\033[0m)")
print("\033[0m")
print("Testing website responsiveness from different countries...")
countries = [
    ("United States", "US"),
    ("United Kingdom", "GB"),
    ("Germany", "DE"),
    ("France", "FR"),
    ("Japan", "JP"),
    ("Saudi Arabia", "SA"),
    ("United Arab Emirates", "AE"),
    ("Egypt", "EG"),
    ("Iraq", "IQ"),
    ("Syria", "SY"),
    ("Jordan", "JO"),
    ("Lebanon", "LB"),
    ("Kuwait", "KW"),
    ("Bahrain", "BH"),
    ("Qatar", "QA"),
    ("Oman", "OM"),
    ("Yemen", "YE"),
    ("Sudan", "SD"),
    ("Libya", "LY"),
    ("Tunisia", "TN"),
    ("Algeria", "DZ"),
    ("Morocco", "MA")
]
for country_name, country_code in countries:
    test_website_responsiveness(url, country_name, country_code)
    time.sleep(1)
