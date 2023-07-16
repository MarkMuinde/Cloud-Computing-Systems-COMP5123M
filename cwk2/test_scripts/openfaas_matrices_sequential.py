import csv
import json
import requests
import time
import random

openfaas_url = "http://172.187.169.185:8080/function/cw2f2"
matrix1 = [[random.randint(1, 100) for _ in range(3)] for _ in range(3)]  
matrix2 = [[random.randint(1, 100) for _ in range(3)] for _ in range(3)] 
total_calls_list = [100, 500, 1000]

with open("openfaas_matrices_sequential_results.csv", mode="w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Total Calls", "Success Rate", "Total Runtime"])

    for total_calls in total_calls_list:
        ok_count = 0
        start_time = time.time()  
        for i in range(total_calls):
            payload = {"matrix1": matrix1, "matrix2": matrix2}
            response = requests.post(openfaas_url, data=json.dumps(payload))
            if response.status_code == 200:
                ok_count += 1
        end_time = time.time()  
        success_rate = (ok_count / total_calls) * 100
        total_time = end_time - start_time  
        print(f"Success rate ({total_calls} calls): {success_rate:.2f}%, Total runtime: {total_time:.2f} seconds")
        writer.writerow([total_calls, success_rate, total_time])
