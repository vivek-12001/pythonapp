def hello_world(request):
    request_json = request.get_json()
    if request.args and 'message' in request.args:
        return request.args.get('message')
    elif request_json and 'message' in request_json:
        return request_json['message']
    else:
        return f'Hello i am Vivek Choudhary currently working as a Platform Engineer at Quantiphi !!'
