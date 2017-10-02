import pickle

def as_string(net):
    str = pickle.dumps(net)
    return str

def save_net(net, filename):
    file = open(filename, 'w')
    str = as_string(net)
    file.write(str)
    file.close()

def from_string(str):
    net = pickle.loads(str)
    return net

def load_net(filename):
    file = open(filename, 'r')
    str = file.read()
    net = from_string(str)
    file.close()

    return net