class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
    def __repr__(self):
        # return "Node({})".format(self.data)
        return f"Node({self.data})"

def circle(head):
    fast=head
    slow=head
    while fast and fast.next:
        fast=fast.next.next
        slow=slow.next
        if fast==slow:
            return True
    return False

def circle_point(head):
    fast = head
    slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            break
    slow=head
    while slow!=fast:
        fast=fast.next
        slow=slow.next
    return slow

n=Node(1)
n1=Node(2)
n2=Node(3)
n3=Node(4)
n4=Node(4)
n5=Node(5)
n6=Node(6)
n.next=n1
n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5
n5.next=n6
n6.next=n3

print(circle(n))
print(circle_point(n))

