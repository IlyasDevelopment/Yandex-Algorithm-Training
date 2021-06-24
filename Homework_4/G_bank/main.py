with open('input.txt', 'r') as input_file:
    requests = []
    for line in input_file.readlines():
        requests.append(line.split())


def check_client(clients, name):
    if name not in clients:
        clients[name] = 0


def get_request(clients, req):
    key_word = req[0]
    if key_word == 'DEPOSIT' or key_word == 'WITHDRAW':
        client_name = req[1]
        value = int(req[2])
        check_client(clients, client_name)
        if key_word == 'DEPOSIT':
            clients[client_name] += value
        else:
            clients[client_name] -= value
    elif key_word == 'BALANCE':
        client_name = req[1]
        if client_name not in clients:
            return 'ERROR'
        return clients[client_name]
    elif key_word == 'TRANSFER':
        sender = req[1]
        receiver = req[2]
        value = int(req[3])
        check_client(clients, sender)
        check_client(clients, receiver)
        clients[sender] -= value
        clients[receiver] += value
    elif key_word == 'INCOME':
        p = float(req[1])
        for key, value in clients.items():
            if value > 0:
                clients[key] *= (1 + p/100)
                clients[key] = int(clients[key])


clients = {}
for request in requests:
    result = get_request(clients, request)
    if result is not None:
        print(get_request(clients, request))
