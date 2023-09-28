# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            
            tail= tail.next

        tail.next = list2 if list1 is None else list1
        return dummy.next

        # if list1 is None:
        #     return list2
        # if list2 is None:
        #     return list1
        # if list1.next is None and list1.val < list2.val:
        #     list1.next=list2
        #     return list1
        # if list1.val > list2.val:
        #     temp = list1
        #     list1=list2
        #     list2=temp
        # result=list1
        # while list1 !=None and list2 !=None:
        #     temp = None
        #     if list1 !=None and list1.val <= list2.val:
        #         temp=list1
        #         list1=list1.next
        #     temp.next=list2
        #     temp=list1
        #     list1=list2
        #     list2=temp
        # return result

        # if list1 is None and list2 is None:
        #     return None
        # if list1 is None and list2 is not None:
        #     return list2
        # if list1 is not None and list2 is None:
        #     return list1
        # if list1.val > list2.val:
        #     temp=list1.val
        #     list1=list2
        #     list2=temp
        # if list1.next is None:
        #     list1.next=list2
        #     return list1
        # if list2.next ==None and list1.next is None:
        #     list1.next=list2 
        #     return list1
        # curr1= list1
        # next1= curr1.next
        # curr2=list2
        # next2=curr2.next
        
        # while next1 !=None and curr2 !=None :
        #     if curr2.val >= curr1.val and next1.val >=curr2.val:
        #         curr1.next = curr2
        #         next2= curr2.next
        #         curr2.next =next1
        #         curr1=curr2
        #         curr2=next2
        #     else:
        #         curr1=next1
        #         next1=next1.next
        #         if next1==None:
        #             curr1.next=curr2
        #             return list1
        # return list1

        
        
            
            

        
        


