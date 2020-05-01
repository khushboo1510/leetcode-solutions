/*
 *https://leetcode.com/problems/find-lucky-integer-in-an-array/
 *
 *Given an array of integers arr, a lucky integer is an integer which has a frequency in the array      equal to its value.
 *
 *Return a lucky integer in the array. If there are multiple lucky integers return the largest of them. If there is no lucky integer return -1.
 */

class Solution {
    public int findLucky(int[] arr) {
        
        Map<Integer, Integer> hashmap = new HashMap<>();
        int result = -1;
        
        for(int i = 0; i < arr.length; i++){
                hashmap.put(arr[i], hashmap.getOrDefault(arr[i], 0) + 1);   
        }
        
        Iterator it = hashmap.entrySet().iterator();
        while (it.hasNext()) {
            Map.Entry<Integer, Integer> pair = (Map.Entry)it.next();
            if(pair.getKey() == pair.getValue()){
                if(pair.getValue().intValue() > result)
                    result = pair.getValue();
            }
        }
        return result;
    }
}