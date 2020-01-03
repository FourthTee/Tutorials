class LinkList:

    empty = None

    def __init__(self, first, rest=empty):
        assert rest is LinkList.empty or isinstance(rest, LinkList)
        self.first = first
        self.rest = rest

    def __len__(self):
        if self.rest is None:
            return 1
        else:
            return 1 + len(self.rest)

    def __str__(self):
    	lst = self
    	string = "["
    	while (lst is not None):
    		string += (" " + str(lst.first))
    		lst = lst.rest
    	return string + " ]"

    def reverse(self): 
        prev = None
        current = self
        nxt = self
        while(current is not None):
            nxt = nxt.rest
            current.rest = prev
            prev = current
            current = nxt
        return prev    

