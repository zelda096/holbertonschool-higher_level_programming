#!/usr/bin/python3
class MyList(list):
    """
    print to stdout list
    """
    def print_sorted(self):
        """
        prints the list
        """
        sort_list = MyList()
        for i in self:
            sort_list.append(i)
        print(sorted(sort_list)) 
