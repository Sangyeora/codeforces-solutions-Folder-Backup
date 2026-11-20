class Solution:
    def addTwoNumbers(self, l1, l2):
        head = ListNode(0)
        now = head
        carry = 0

        while l1 or l2 or carry:
            total = carry

            if l1:
                total += l1.val
                l1 = l1.next

            if l2:
                total += l2.val
                l2 = l2.next

            digit = total % 10
            carry = total // 10

            now.next = ListNode(digit)
            now = now.next

        return head.next