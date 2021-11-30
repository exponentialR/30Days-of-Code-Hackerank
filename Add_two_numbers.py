"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order,
 and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.



Input: l1 = [0], l2 = [0]
Output: [0]

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def addTwoNumbers(self, input1:ListNode, input2: ListNode) -> ListNode:
        prev = result = ListNode(None)
        carry = 0
        while input1 or input2 or carry:
            if input1:
                carry += input1.val
                input1 = input1.next
            if input2:
                carry += input2.val
                input2 = input2.next
            prev.next = ListNode(carry % 10 )
            prev = prev.next
            carry //=10
        return result.next

        # added = ListNode(val = (input1.val, input2.val)%10)
        # carryover = (input1.val + input2.val) //10
        # currntnode = added
        # while (input1.next and input2.next):
        #     input1 = input1.next
        #     input2 = input2.next
        #     currntnode.next = ListNode(val = (carryover + input1.val + input2.val) % 10)
        #     carryover = (carryover + input1.val + input2.val)//10
        #     currntnode = currntnode.next
        #
        # while(input1.next):
        #     input1 = input1.next
        #     currntnode.next = ListNode(val=(carryover + input1.val) % 10)
        #     carryover = (carryover + input1.val ) // 10
        #     currntnode = currntnode.next
        #
        # while(input2.next):
        #     input2 = input2.next
        #     currntnode.next = ListNode(val = (carryover + input2.val) % 10)
        #     carryover = (carryover + input2.val) // 10
        #     currntnode = currntnode.next
        # if (carryover) > 0:
        #     currntnode.next = ListNode(val = 1)
        # return added


    # int1 = ''
    # int2 =''
    # for i in reversed(input1):
    #     int1 += str(i)
    # for i in reversed(input2):
    #     int2 += str(i)
    # addall = int(int1) + int(int2)
    # new_addll = [int(i) for i in reversed(str(addall))]
    # return new_addll

# l1 = [2,4,3]
# l2 = [5,6,4]
# l1 = [9,9,9,9,9,9,9]
# l2 = [9,9,9,9]

