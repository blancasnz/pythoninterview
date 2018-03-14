

def remove_dup(head):
    visited = set()
    runner = head

    visited.add(head.val)
    while runner.next:
        if runner.next.val in visited:
            pending_removal = runner.next
            runner.next = pending_removal.next
            pending_removal.next = None
        else:
            visited.add(runner.next.val)
            runner = runner.next
    return head
