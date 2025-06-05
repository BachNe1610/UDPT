import random
from tenacity import retry, stop_after_attempt, wait_fixed

# Giả lập danh sách các "job" lấy từ hàng đợi
queue = ["job_1", "job_2", "job_3"]

@retry(stop=stop_after_attempt(3), wait=wait_fixed(1))
def process_job(job):
    print(f"▶️ Đang xử lý: {job}")
    if random.random() < 0.7:
        raise Exception("❌ Lỗi xử lý job")
    print(f"✅ Xử lý thành công: {job}")

if __name__ == "__main__":
    for job in queue:
        try:
            process_job(job)
        except Exception as e:
            print(f"⛔ Job {job} thất bại sau nhiều lần retry.\n")
