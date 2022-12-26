# Return the head of the merged linked list.
# class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next

def mergeSortedLists(list1, list2):
    dummy = ListNode()  # create a dummy Node
    curr = dummy  # point curr to dummy
    if not list1 and not list2:
        return None
    pointer1, pointer2 = list1, list2
    # pointer1 and pointer2 point at head of list1 and list2 respectively
    while pointer1 and pointer2:
        if pointer1.val < pointer2.val:
            curr.next = pointer1
            pointer1 = pointer1.next
        else:
            curr.next = pointer2
            pointer2 = pointer2.next
        curr = curr.next
    if not pointer2 and pointer1:
        curr.next = pointer1
    if not pointer1 and pointer2:
        curr.next = pointer2
    return dummy.next  # return head of new sorted list
