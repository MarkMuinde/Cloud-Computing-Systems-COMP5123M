import logging
import json
import datetime
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python HTTP trigger function processed a request.')
    start_time = datetime.datetime.now()
    
    try:
        req_body = req.get_json()
    except ValueError:
        return func.HttpResponse(
                "Please pass an integer array as a JSON array in the request body to perform sum of an array of numbers\nUse: curl --request POST --data '[number 1, number 2,..., number n-1, number n]' https://cw2f1.azurewebsites.net/api/CW2F1\nExample: curl --request POST --data '[1, 2, 3]' https://cw2f1.azurewebsites.net/api/CW2F1\nInput and output is via your terminal",
            status_code=400
        )

    if isinstance(req_body, list):
        result = sum(req_body)
        logging.info(f"Input Array: {req_body}\n")
        logging.info(f"Sum of input array: {result}")
        end_time = datetime.datetime.now()
        runtime = (end_time - start_time).total_seconds() * 1000
        
        response = {"Input Array": req_body, "Sum": result, "Runtime(in milliseconds)": runtime}
        final_string = json.dumps(response, indent=5)
        return func.HttpResponse(
                final_string,
            status_code=200
        )
    else:
        return func.HttpResponse(
            "Please pass a JSON array in the request body\nUse: curl --request POST --data '[number 1, number 2,..., number n-1, number n]' https://cw2f1.azurewebsites.net/api/CW2F1\nExample: curl --request POST --data '[1, 2, 3]' https://cw2f1.azurewebsites.net/api/CW2F1\nInput and output is via your terminal",
            status_code=400
        )

