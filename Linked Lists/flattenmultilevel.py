class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: Node) -> Node:
        # We must keep track of the current node, if we find a node that has a child node, then we start traversing the child node, but we have to save the current node
        # so that after we finish traversing the child node, we set the current node's child node to None.

        current = head

        while current != None:
            if current.child != None:
                self.loop_through_child(current, current.child)
                current.child = None

            current = current.next
        
        return head 
        
    def loop_through_child(self, current: Node, child: Node) -> None:
        current_next = current.next
        current.next = child
        child.prev = current

        while child.next != None:
            if child.child != None:
                self.loop_through_child(child, child.child)
                child.child = None
        child = child.next # We don't do an else since if we did do an else, then child would never increment, we would stay with the same child variable, and infinitely loop since
            # we're staying with the same child, which has a child itself.

        child.next = current_next
        # if this child node is the last node, (so the last node in the top row of nodes has children), current_next will be None, so in that case over here
        # we don't have a current_next to update the previous pointer of
        if current_next != None:
            current_next.prev = child
        
        current.child = None