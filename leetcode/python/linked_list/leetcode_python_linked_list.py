# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def lst_toLinkedLst(lst):
    linked_lst = []
    for idx, val in enumerate(lst):
        lst_node = ListNode(val=val)
        linked_lst.append(lst_node)

    for idx, node in enumerate(linked_lst[:-1]):
        node.next = linked_lst[idx+1]

    return linked_lst[0]

def listToInt(lst: list) -> int:
    num_int = 0
    for idx, digit in enumerate(lst):
        num_int += int(digit)*(10**(len(lst)-(idx+1)))
    return num_int

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        """
        Link to LeetCode: https://leetcode.com/problems/linked-list-cycle/
        Given head, the head of a linked list, determine if the linked list has a cycle in it.

        Args:
            head (ListNode): linked list to check cycle

        Returns:
            bool: true if there is a cycle in the linked list. Otherwise, false.
        """
        lst = []
        while head is not None:
                if id(head) in lst: 
                    return True
                lst.append(id(head))
                head = head.next
        return False

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """ 
        Link to LeetCode: https://leetcode.com/problems/add-two-numbers/
        You are given two non-empty linked lists representing two non-negative integers. 
        The digits are stored in reverse order, and each of their nodes contains a single digit. 
        Add the two numbers and return the sum as a linked list.

        Args:
            l1 (ListNode): linked list representation of some number
            l2 (ListNode): linked list representation of some number

        Returns:
            ListNode: linked list representation of sum(l1, l2)
        """
        lst1, lst2 = [], []
        while l1 is not None:
            lst1.append(l1.val)
            l1 = l1.next

        while l2 is not None:
            lst2.append(l2.val)
            l2 = l2.next

        l1_num = listToInt(lst1[::-1])
        l2_num = listToInt(lst2[::-1])
        result_num = l1_num + l2_num
        result_num = list(str(result_num))[::-1]
        result_num = [int(i) for i in result_num]

        linked_lst = lst_toLinkedLst(result_num)
        return linked_lst

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """ 
        Link to LeetCode: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
        Given the head of a linked list, remove the nth node from the end of the list and return its head.

        Args:
            head (ListNode): linked list to remove item
            n (int): index of item to remove

        Returns:
            ListNode: linked list with item removed
        """
        linked_lst = []
        linked_lst_len = 0
        while head is not None:
            linked_lst.append(head.val)
            head = head.next
            linked_lst_len+=1

        del linked_lst[linked_lst_len-n]
        if len(linked_lst) == 0: return None
        else: linked_lst = lst_toLinkedLst(linked_lst)
        return linked_lst

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Link to LeetCode: https://leetcode.com/problems/merge-two-sorted-lists/
        Merge two sorted linked lists and return it as a sorted list.

        Args:
            l1 (ListNode): 1st linked list to merge
            l2 (ListNode): 2nd linked list to merge

        Returns:
            ListNode: linked list made by merging l1 and l2
        """
        lst = []
        while l1 is not None:
            lst.append(l1.val)
            l1 = l1.next
        while l2 is not None:
            lst.append(l2.val)
            l2 = l2.next
        lst.sort()
        if len(lst) == 0: return None
        else: linked_lst = lst_toLinkedLst(lst)
        return linked_lst

    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        """
        Link to LeetCode: https://leetcode.com/problems/merge-k-sorted-lists/
        You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
        Merge all the linked-lists into one sorted linked-list and return it.

        Args:
            lists (List[ListNode]): list of k linked lists

        Returns:
            ListNode: linked list made by merging k linked lists
        """
        lst = []
        for linked_list in lists:
            while linked_list is not None:
                lst.append(linked_list.val)
                linked_list = linked_list.next
            
        lst.sort()
        if len(lst) == 0: return None
        else: linked_lst = lst_toLinkedLst(lst)
        return linked_lst

    def swapPairs(self, head: ListNode) -> ListNode:
        """
        Link to LeetCode: https://leetcode.com/problems/swap-nodes-in-pairs/
        Given a linked list, swap every two adjacent nodes and return its head. 

        Args:
            head (ListNode): linked list to swap nodes

        Returns:
            ListNode: linked list with nodes swapped
        """
        lst = []

        while head is not None:
            lst.append(head.val)
            head = head.next

        for idx in range(0, len(lst),2):
            try:
                lst[idx], lst[idx+1] = lst[idx+1], lst[idx]
            except: pass
        
        if len(lst) > 0: linked_lst = lst_toLinkedLst(lst)
        else: linked_lst = head
        return linked_lst

    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        """
        Link to LeetCode: https://leetcode.com/problems/swapping-nodes-in-a-linked-list/
        You are given the head of a linked list, and an integer k.
        Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

        Args:
            head (ListNode): linked list to swap nodes
            k (int): index for nodes to be swapped

        Returns:
            ListNode: linked list with nodes swapped
        """
        lst = []

        while head is not None:
            lst.append(head.val)
            head = head.next
        k -= 1
        if len(lst) > k:
            lst[k], lst[len(lst)-k-1] = lst[len(lst)-k-1], lst[k]
        if len(lst) > 0: linked_lst = lst_toLinkedLst(lst)
        else: linked_lst = head
        return linked_lst

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        Link to LeetCode: https://leetcode.com/problems/remove-duplicates-from-sorted-list/
        Given the head of a sorted linked list, delete all duplicates such that each element appears only once. 
        Return the linked list sorted as well.

        Args:
            head (ListNode): linked list to remove duplicates

        Returns:
            ListNode: linked list with duplicates removed
        """
        lst = []
        while head is not None:
            lst.append(head.val)
            head = head.next
        
        lst = list(set(lst))
        lst.sort()

        if len(lst) == 0: return None
        else: linked_lst = lst_toLinkedLst(lst)
        return linked_lst

    def deleteDuplicates_2nd(self, head: ListNode) -> ListNode:
        """
        Link to LeetCode: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

        Args:
            head (ListNode): linked list to remove duplicates

        Returns:
            ListNode: linked list with duplicates removed
        """
        lst = []
        while head is not None:
            lst.append(head.val)
            head = head.next

        for elem in lst:
            if lst.count(elem) > 1:
                lst = list(filter(lambda a: a != elem, lst))

        if len(lst) == 0: return None
        else: linked_lst = lst_toLinkedLst(lst)
        return linked_lst
