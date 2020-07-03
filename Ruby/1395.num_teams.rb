def num_teams(rating)
    
    count = 0
    combinations = rating.combination(3).to_a
    teams = []
    
    combinations.each do |combo|
        if combo[0] < combo[1] && combo[1] < combo[2] 
            teams << combo
        elsif combo[0] > combo[1] && combo[1] > combo[2]
            teams << combo
        end
    end
    return teams.count
end