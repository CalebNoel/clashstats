import urllib
import json
import environ
env = environ.Env()
environ.Env.read_env()

def get_cards():
    key = env('API_KEY')
    base_url = "https://api.clashroyale.com/v1"
    endpoint = "/cards"
    request =  urllib.request.Request(base_url+endpoint, None, {"Authorization": "Bearer %s" % key})
    response = urllib.request.urlopen(request).read()
    return response

def get_player_info(tag):
    key = env('API_KEY')
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

def get_player_battles(tag):
    key = env('API_KEY')
    base_url = "https://api.clashroyale.com/v1"
    tag = tag.replace('#', "", 1).upper()
    endpoint = "/players/%23" + tag + "/battlelog"

    try:
        assembled_request =  urllib.request.Request(base_url+endpoint, None, {"Authorization": "Bearer %s" % key})
        response = urllib.request.urlopen(assembled_request).read()
    except urllib.error.HTTPError as e:
        print("HTTP Code: {}".format(e.code))
        print("Error Reason: {}".format(e.reason))
        return "error"
    else:
        return response
