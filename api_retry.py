
import requests
import logging
from tenacity import retry, stop_after_attempt, wait_fixed, retry_if_exception_type


logging.basicConfig(filename="retry_log.txt", level=logging.INFO, format="%(asctime)s - %(message)s")

call_count = {"count": 0}

@retry(
    stop=stop_after_attempt(5),
    wait=wait_fixed(2),
    retry=retry_if_exception_type(requests.exceptions.RequestException),
)
def fetch_data():
    call_count["count"] += 1
    logging.info(f"Lan goi API thu {call_count['count']}")
    print(f"Lan goi API thu {call_count['count']}...")

    response = requests.get("https://httpstat.us/200")  
    response.raise_for_status()
    return response.text

if __name__ == "__main__":
    try:
        data = fetch_data()
        print("Thanh Cong:", data)
        logging.info("Thanh Cong")
    except Exception as e:
        error_msg = f"Goi API that bai sau nhieu lan thu: {str(e)}"
        print(error_msg)
        logging.error(error_msg)
