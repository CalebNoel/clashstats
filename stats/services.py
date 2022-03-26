import urllib
import json

def get_cards():
    key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjFlMzQyYWJmLTRkZTctNDkwMC1hNTgwLWQ4YjM5YmM5NGZhZSIsImlhdCI6MTY0ODE5NDk4Nywic3ViIjoiZGV2ZWxvcGVyL2ZjMmM2MWFhLWM2MzQtZjViMi04YjcyLTZkMDU0ODkzODFjOCIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyI3My43OC4xMzMuOTYiXSwidHlwZSI6ImNsaWVudCJ9XX0.GYFXN5fduT87L5XvTG5CTDxxt0kLeExhXnN0QCcrvy9q64kU7TMG8sNm9EKyHIxRXHfEEeCxfDfcMxDqpFet2g"
    base_url = "https://api.clashroyale.com/v1"
    endpoint = "/cards"
    request =  urllib.request.Request(base_url+endpoint, None, {"Authorization": "Bearer %s" % key})
    response = urllib.request.urlopen(request).read()
    return response

def get_player_info(tag):
    key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjFlMzQyYWJmLTRkZTctNDkwMC1hNTgwLWQ4YjM5YmM5NGZhZSIsImlhdCI6MTY0ODE5NDk4Nywic3ViIjoiZGV2ZWxvcGVyL2ZjMmM2MWFhLWM2MzQtZjViMi04YjcyLTZkMDU0ODkzODFjOCIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyI3My43OC4xMzMuOTYiXSwidHlwZSI6ImNsaWVudCJ9XX0.GYFXN5fduT87L5XvTG5CTDxxt0kLeExhXnN0QCcrvy9q64kU7TMG8sNm9EKyHIxRXHfEEeCxfDfcMxDqpFet2g"
    base_url = "https://api.clashroyale.com/v1"
    tag = tag.replace('#', "", 1).upper()
    endpoint = "/players/%23" + tag

    try:
        assembled_request =  urllib.request.Request(base_url+endpoint, None, {"Authorization": "Bearer %s" % key})
        response = urllib.request.urlopen(assembled_request).read()
    except urllib.error.HTTPError as e:
        print("HTTP Code: {}".format(e.code))
        print("Error Reason: {}".format(e.reason))
        return "error"
    else:
        return response
