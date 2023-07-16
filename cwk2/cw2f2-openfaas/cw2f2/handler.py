import logging
import json
import numpy as np
import datetime

def handle(req):
    logging.info('OpenFaaS function processed a request.')
    start_time = datetime.datetime.now()

    try:
        req_body = json.loads(req)
    except ValueError:
        return json.dumps({
            "error": "Please pass two matrices as JSON objects in the request body to perform matrix multiplication\nUse: curl --request POST--data '{"'matrix1'": [[n1,n2,n3],[n4,n5,n6],[n7,n8,n9]], "'matrix2'": [[n10,n11,n12],[n13,n14,n15],[n16,n17,n18]]}' http://172.187.169.185:8080/function/cw2f2\nExample: curl --request POST --data '{"'matrix1'": [[1,2,3],[4,5,6],[7,8,9]], "'matrix2'": [[9,8,7],[6,5,4],[3,2,1]]}' http://172.187.169.185:8080/function/cw2f2\nEnsure that the key names(matrix1 and matrix2) are encapsulated in double quotation marks\nInput and output is via your terminal"
        })

    if isinstance(req_body, dict) and 'matrix1' in req_body and 'matrix2' in req_body:
        matrix1 = req_body['matrix1']
        matrix2 = req_body['matrix2']
        try:
            result = np.dot(matrix1, matrix2).tolist()
            logging.info(f'Matrix 1: {matrix1}')
            logging.info(f'Matrix 2: {matrix2}')
            logging.info(f'Result: {result}')
            end_time = datetime.datetime.now()
            runtime = (end_time - start_time).total_seconds() * 1000
            response = {"Matrix 1" : matrix1, "Matrix 2" : matrix2, "Result of Matrix Multiplication" : result, "Runtime (in milliseconds)" : runtime}
            final_string = json.dumps(response)
            return final_string
        except ValueError:
            return json.dumps({
                "error": "Please pass two matrices as JSON objects in the request body to perform matrix multiplication\nUse: curl --request POST--data '{"'matrix1'": [[n1,n2,n3],[n4,n5,n6],[n7,n8,n9]], "'matrix2'": [[n10,n11,n12],[n13,n14,n15],[n16,n17,n18]]}' http://172.187.169.185:8080/function/cw2f2\nExample: curl --request POST --data '{"'matrix1'": [[1,2,3],[4,5,6],[7,8,9]], "'matrix2'": [[9,8,7],[6,5,4],[3,2,1]]}' http://172.187.169.185:8080/function/cw2f2\nEnsure that the key names(matrix1 and matrix2) are encapsulated in double quotation marks\nInput and output is via your terminal"
           })
    else:
        return json.dumps({
            "error": "Please pass two matrices as JSON objects in the request body to perform matrix multiplication\nUse: curl --request POST--data '{"'matrix1'": [[n1,n2,n3],[n4,n5,n6],[n7,n8,n9]], "'matrix2'": [[n10,n11,n12],[n13,n14,n15],[n16,n17,n18]]}' http://172.187.169.185:8080/function/cw2f2\nExample: curl --request POST --data '{"'matrix1'": [[1,2,3],[4,5,6],[7,8,9]], "'matrix2'": [[9,8,7],[6,5,4],[3,2,1]]}' http://172.187.169.185:8080/function/cw2f2\nEnsure that the key names(matrix1 and matrix2) are encapsulated in double quotation marks\nInput and output is via your terminal"
            })
