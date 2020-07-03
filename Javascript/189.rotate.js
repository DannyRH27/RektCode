var rotate = function (nums, k) {

    for (let i = 0; i < k; i++) {
        pop = nums.pop();
        nums.unshift(pop)
    }
};