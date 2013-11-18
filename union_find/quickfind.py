
class QuickFind:

    search_array=[]

    def __init__(self, n):
        for x in range(0,n):
            search_array[x]=x


    def is_connected(self, node_a, node_b):
        return self.search_array[node_a] == self.search_array[node_b]

    def union(node_a, node_b): # connect

        search_for = search_array[node_a]

        for item in self.search_array:
            if item == search_for:
                self.search_array[node_a] = search_for
