class NodePriority(object):
    def __init__(self, name,h_value):
        self.name = name
        self.h_value = h_value
        return

    def __lt__(self, other):
        return self.h_value < other.h_value
