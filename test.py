from tenacity import retry, stop_after_attempt, wait_fixed, RetryError

@retry(stop=stop_after_attempt(3), wait=wait_fixed(1))
def do_something():
    print("Trying...")
    raise Exception("Fail")

try:
    do_something()
except RetryError as e:
    print("All retries failed. Error:", e)
