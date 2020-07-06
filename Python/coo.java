class Solution {
    public void duplicateZeros(int[] arr) {
        int zeros = 0;
        
        for (int i : arr) {
            if (i == 0) 
                zeros++;
        }
        
        int len = arr.length;
        int totalLen = len + zeros;
        for (int i = len -1, j = totalLen -1; i < j; i--, j--) {
            int beingChecked = arr[i];
            
            if (j < len ) {
                int copied = arr[j];
                arr[j] = arr[i];    
            }
            
            if (arr[i] == 0) {
                j--;
                if (j < len) {
                    arr[j] = arr[i];
                }
            }   
        }
    }
}