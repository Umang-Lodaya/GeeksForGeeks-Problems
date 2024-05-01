#User function Template for python3

"""
# Node Class

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

"""

class Solution:
    def swap(self, a, b):
        temp1 = a.next
        temp2 = b.next
        a.next = temp2
        b.next = b.next.next
        temp2.next = temp1

    def arrangeCV(self, head):
        if not head:
            return head
        
        b = {'a','e','i','o','u'}
        vow, cons = 0,0
        temp = head
        while temp:
            if temp.data in b:
                vow = 1
            else:
                cons = 1
                
            if vow and cons:
                break
            
            temp = temp.next
        
        if vow == 0 or cons == 0:
            return head
            
        if head.data not in b:
            temp = head
            while temp.next:
                if temp.next.data in b:
                    break
                else:
                    temp = temp.next
            temp1 = temp.next
            temp.next = temp.next.next
            temp1.next = head
            head = temp1
            
        vow, con = head, head.next
        while vow.next:
            if vow.next.data in b:
                vow = vow.next
            else:
                break
            
        while True:
            if con.data in b:
                con = con.next
            else:
                break
            
        while vow and con.next:
            if con.next.data in b:
                self.swap(vow, con)
                vow = vow.next
            else:
                con = con.next
        
        return head


#{ 
 # Driver Code Starts
# Node Class
class Node:

    def __init__(self, val):
        self.data = val
        self.next = None


# Linked List Class
class Linked_List:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next


def printList(head):
    tmp = head
    while tmp:
        print(tmp.data, end=' ')
        tmp = tmp.next
    print()


if __name__ == '__main__':
    for i in range(int(input())):
        n = int(input())
        arr = [str(x) for x in input().split()]

        lis = Linked_List()
        for i in arr:
            lis.insert(i)

        newHead = Solution().arrangeCV(lis.head)
        printList(newHead)

# } Driver Code Ends