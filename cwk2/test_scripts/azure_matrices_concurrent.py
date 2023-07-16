import concurrent.futures
import csv
import json
import random
import requests
import time

azure_url = "https://cw2f2.azurewebsites.net/api/CW2F2"
total_calls_list = [100, 500, 1000]

def make_request(index):
    matrix1 = [[random.randint(1, 100) for _ in range(3)] for _ in range(3)] 
    matrix2 = [[random.randint(1, 100) for _ in range(3)] for _ in range(3)]  
    payload = {"matrix1": matrix1, "matrix2": matrix2}
    response = requests.post(azure_url, data=json.dumps(payload))
    if response.status_code == 200:
        return response.json()
    else:
        return None

with open("azure_matrices_concurrent_results.csv", mode="w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Total Calls", "Success Rate", "Total Runtime"])

    for total_calls in total_calls_list:
        start_time = time.time()  
        with concurrent.futures.ThreadPoolExecutor(max_workers=total_calls) as executor:
            results = list(executor.map(make_request, range(total_calls)))
        end_time = time.time()  
        ok_count = len([result for result in results if result is not None])
        success_rate = (ok_count / total_calls) * 100
        total_time = end_time - start_time  
        print(f"Success rate ({total_calls} calls): {success_rate:.2f}%, Total runtime: {total_time:.2f} seconds")
        writer.writerow([total_calls, success_rate, total_time])
