def middle_node(head)
    count = 1
    node = head
    
    until node.next == nil
        count +=1
        node = node.next
    end
    
    mid = count/2
    node = head
    (mid).times {
        node = node.next
    }
    return node
    
end