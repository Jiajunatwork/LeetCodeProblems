
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class AddTwoNumbers(object):
    def addTwoNumbers(self, l1, l2):
        numOne = 0
        numTwo = 0
        tens = 1
        while l1 != None:
            numOne = numOne + (l1.val*tens)
            tens = tens * 10
            l1 = l1.next
        
        tens = 1
        while l2 != None:
            numTwo = numTwo + (l2.val*tens)
            tens = tens * 10
            l2 = l2.next

        sum = numOne + numTwo
        resultNode = None
        currentNode = resultNode
        sumDigitList = [int(temp) for temp in str(sum)]
        sumDigitList.reverse()
        for digit in sumDigitList:
            if resultNode == None:
                resultNode = ListNode(digit, None)
                currentNode = resultNode
            else:
                currentNode.next = ListNode(digit, None)
                currentNode = currentNode.next
        
        if resultNode == None:
            resultNode = ListNode(0,None)
        return resultNode

    