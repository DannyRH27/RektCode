def min_path_sum(grid)
    new_grid = Array.new(grid.length) {Array.new(0,[])}
    new_grid[0][0] = grid[0][0]

    grid.each do |row, i|
        row.each do |ele, j|
            if i==0 && j == 0
                next
            end

            if i-1 >=0
                left = grid
        end
    end

    

end

grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]

p min_path_sum(grid)