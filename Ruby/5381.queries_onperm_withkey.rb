require 'byebug'
# Input: queries = [4,1,2,2], m = 4
# Output: [3,1,2,0]


def process_queries(queries, m)
    arr = []
    perm = *(1..m)
    i = 0
    while i < queries.length
        if perm.include?(queries[i])
            index = perm.find_index(queries[i])
            arr += [index]
            deleted = perm.delete_at(index)
            perm.unshift(deleted)
        end
        i+=1
    end

    return arr
end

queries = [4,1,2,2]
m = 4

p process_queries(queries, m)