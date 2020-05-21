/**
 * https://leetcode.com/problems/find-the-distance-value-between-two-arrays/
 * 
 * Given two integer arrays arr1 and arr2, and the integer d, return the distance value between the two arrays.
 * The distance value is defined as the number of elements arr1[i] such that there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.
 */

/**
 * @param {number[]} arr1
 * @param {number[]} arr2
 * @param {number} d
 * @return {number}
 */
var findTheDistanceValue = function(arr1, arr2, d) {
    
  let count = 0;
  
  for(let i = 0; i < arr1.length; i++){
      for(let j = 0; j < arr2.length; j++){
          if(Math.abs(arr1[i] - arr2[j]) <= d){
              count -= 1;
              break                
          }
      }
      count += 1
  }
  
  return count
};