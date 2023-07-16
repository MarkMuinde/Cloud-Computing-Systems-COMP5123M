import csv
import random
import requests
import time

openfaas_url = "http://172.187.169.185:8080/function/cw2f1"
total_calls_list = [100, 500, 1000]

with open("openfaas_array_sequential_results.csv", mode="w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Total Calls", "Success Rate", "Total Runtime"])

    for total_calls in total_calls_list:
        ok_count = 0
        start_time = time.time()  
        for i in range(total_calls):
            json_array = [random.randint(1, 100) for _ in range(10)]  
            response = requests.post(openfaas_url, json=json_array)
            if response.status_code == 200:
                ok_count += 1
        end_time = time.time()  
        success_rate = (ok_count / total_calls) * 100
        total_time = end_time - start_time  
        print(f"Success rate ({total_calls} calls): {success_rate:.2f}%, Total runtime: {total_time:.2f} seconds")
        writer.writerow([total_calls, success_rate, total_time])
