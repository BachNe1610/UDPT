import requests
from tenacity import retry, stop_after_attempt, wait_fixed, retry_if_exception_type

@retry(
    stop=stop_after_attempt(5),             
    wait=wait_fixed(2),                    
    retry=retry_if_exception_type(requests.exceptions.RequestException)
)
def fetch_data():
    print("Đang gọi API...")
    response = requests.get("https://httpstat.us/500")  
    # response = requests.get("https://httpstat.us/200") 

    response.raise_for_status() 
    return response.text

try:
    data = fetch_data()
    print("Thành công:", data)
except Exception as e:
    print("❌ Gọi API thất bại sau nhiều lần thử:", str(e))
