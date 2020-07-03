def add_two_numbers(l1, l2)
    curr1 = l1
    values1 = []
    until curr1 == nil
        values1 << curr1.val
        curr1 = curr1.next
    end
     
    convert1 = values1.map.with_index {|num,idx| num * 10**idx}
    
    values2 = []
    curr2 = l2
    until curr2 == nil
        values2 << curr2.val
        curr2 = curr2.next
    end
     
    convert2 = values2.map.with_index {|num,idx| num * 10**idx}
    
    final = convert1.sum + convert2.sum
      
    first_node = ListNode.new(final % 10)
    final = (final/10).to_i
    curr_node = first_node
    until final == 0
        
        next_node = ListNode.new(final % 10)
        final = (final/10).to_i
        curr_node.next = next_node
        curr_node = next_node
         
    end
    return first_node
end