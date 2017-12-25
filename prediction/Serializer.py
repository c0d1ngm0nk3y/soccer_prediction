import pickle

def as_string(net):
    string = pickle.dumps(net)
    return string

def save_net(net, filename):
    a_file = open(filename, 'w')
    string = as_string(net)
    a_file.write(string)
    a_file.close()

def from_string(string):
    net = pickle.loads(string)
    return net

def load_net(filename):
    a_file = open(filename, 'r')
    string = a_file.read()
    net = from_string(string)
    a_file.close()
    return net