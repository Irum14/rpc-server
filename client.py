import requests

SERVER_URL = "https://rpc-server-1.onrender.com"

def call_rpc(endpoint, data):
    try:
        response = requests.post(f"{SERVER_URL}{endpoint}", json=data, timeout=2)
        response.raise_for_status()  # raises error for 4xx/5xx responses
        return response.json()
    except requests.exceptions.Timeout:
        print("Request timed out")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

if __name__ == "__main__":
    # Test add(2,3)
    result = call_rpc("/add", {"x": 2, "y": 3})
    if result:
        print(f"add(2,3) = {result['result']}")

    # Test multiply(4,5)
    result = call_rpc("/multiply", {"x": 4, "y": 5})
    if result:
        print(f"multiply(4,5) = {result['result']}")
