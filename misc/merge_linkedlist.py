# this method splits linked list in two halves by iterating over whole list
# It returns head pointers of first and 2nd halves of linked lists in first_second
# Head of 1st half is just the head node of linked list
def split_in_half(head, first_second):

  if head == None:
    
    first_second.first = None
    first_second.second = None
    return

  # Only one element in the list
  if head.next == None:
    
    first_second.first = head
    first_second.second = None
  else:

    # Let's use the classic technique of moving two pointers:
    # 'fast' and 'slow'. 'fast' will move two steps in each 
    # iteration where 'slow' will be pointing to middle element
    # at the end of loop.

    slow = head
    fast = head.next

    while fast != None:
      
      fast = fast.next

      if fast != None:

        fast = fast.next
        slow = slow.next

    first_second.first = head
    first_second.second = slow.next

    # Terminate first linked list.
    slow.next = None

def merge_sorted_lists(first, second):

  if first == None:
    return second

  if second == None:
    return first

  new_head = None

  if first.data <= second.data:
    
    new_head = first
    first = first.next
  else:
    
    new_head = second
    second = second.next

  new_current = new_head
  while first != None and second != None:
    temp = None
    if first.data <= second.data:
      temp = first
      first = first.next
    else:
      temp = second
      second = second.next

    new_current.next = temp
    new_current = temp
  
  if first != None:
    new_current.next = first
  elif second != None:
    new_current.next = second

  return new_head

def merge_sort(head):

  # No need to sort a single element.
  if head == None or head.next == None:
    return head

  first_second = pair(None, None)

  # Let's split the list in half, sort the sublists
  # and then merge the sorted lists.
  split_in_half(head, first_second)

  first_second.first = merge_sort(first_second.first)
  first_second.second = merge_sort(first_second.second)

  return merge_sorted_lists(first_second.first, first_second.second)

class Node:
    def __init__(self, data=None):
        self.data = dataval
        self.next = None

## MAIN

# test_split_in_half()
v1 = [5, 1, 2, 34, 2, 5, 1, 3, 2, 6, 0]
list_head_1 = create_linked_list(v1)
print "Unsorted linked list: \n"
printList(list_head_1)

list_head_1 = merge_sort(list_head_1)
printList(list_head_1)