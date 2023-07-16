import json
import datetime

def handle(req):
    start_time = datetime.datetime.now()

    try:
        req_body = json.loads(req)
    except ValueError:
        return json.dumps({
            "error": "Please pass an integer array as a JSON array in the request body to perform sum of an array of numbers.\nExample Use: curl --request POST --data '[1, 2, 3]' http://172.187.169.185:8080/function/cw2f1"
        })

    if isinstance(req_body, list):
        result = sum(req_body)
        end_time = datetime.datetime.now()
        runtime = (end_time - start_time).total_seconds() * 1000

        response = {"Input Array": req_body, "Sum": result, "Runtime(in milliseconds)": runtime}
        final_string = json.dumps(response, indent=5)
        return final_string
    else:
        return json.dumps({
            "error": "Please pass an integer array as a JSON array in the request body to perform sum of an array of numbers.\nExample Use: curl --request POST --data '[1, 2, 3]' http://172.187.169.185:8080/function/cw2f1"
        })

