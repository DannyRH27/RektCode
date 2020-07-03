# Input: orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]
# Output: [["Table","Beef Burrito","Ceviche","Fried Chicken","Water"],["3","0","2","1","0"],["5","0","1","0","1"],["10","1","0","0","0"]] 



def display_table(orders)
    table_hash = Hash.new([])
    tables = []
    items = []
    orders.each do |order|
        items << order[2]
        if !table_hash.has_key?(order[1])
            table_hash[order[1]] = []
        end
        table_hash[order[1]] << order[2]
    end

    header = items.uniq.sort.unshift("Table")
    tables << header
    table_hash.keys.map {|key| key.to_i}.sort.each do |table|
        table = table.to_s
        hash = Hash.new(0)
        table_order = table_hash[table]
        table_order.each do |item|
            if !hash.has_key?(item)
                hash[item] = 0
            end
            hash[item] += 1
        end
        new_row = [table]
        items.uniq.sort.each do |item|
            if !hash.has_key?(item)
                hash[item] = 0
            end
            new_row << hash[item].to_s
        end
        tables << new_row
    end

    return tables
end


orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]


p display_table(orders)