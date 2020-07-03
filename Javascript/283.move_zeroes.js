// Given an array nums, write a function to move all 
// 0's to the end of it while maintaining the relative 
// order of the non-zero elements.

var moveZeroes = function (nums) {
    var count = 0

    for (let i = 0; i < nums.length; i++) {
        if (nums[i] !== 0) {
            nums[count] = nums[i];
            count++;
        }
    }

    for (;count < nums.length; count++) {
        nums[count] = 0;
    }
    return nums;
};

console.log(moveZeroes([0,1,0,3,12]))