/*
 *https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
 *
 *Given a m * n matrix mat of ones (representing soldiers) and zeros (representing civilians), return the indexes of the k weakest rows in the matrix ordered from the weakest to the strongest.
 *
 *A row i is weaker than row j, if the number of soldiers in row i is less than the number of soldiers in row j, or they have the same number of soldiers but i is less than j. Soldiers are always stand in the frontier of a row, that is, always ones may appear first and then zeros.
 *
 */
class Solution {
    public int[] kWeakestRows(int[][] mat, int k) {
        
        Map<Integer, Integer> map = new HashMap<Integer,Integer>();
        
        int rows = mat.length;
        int cols = mat[0].length;
        
        for(int i = 0; i < rows; i++){
            int count = 0;
            for(int j = 0; j < cols; j++){
                if(mat[i][j] == 1)
                    count++;
                else
                    break;
            }
            map.put(i, count);
        }
        
        PriorityQueue<Map.Entry<Integer, Integer>> pq = new PriorityQueue<>((a,b) ->
            a.getValue() == b.getValue() ? a.getKey() - b.getKey() : a.getValue() - b.getValue());
        
        for(Map.Entry<Integer, Integer> entry : map.entrySet())
            pq.add(entry);
        int[] result = new int[k];
        
        for(int i = 0; i < k; i++)
            result[i] = pq.poll().getKey();
        
        return result;
    }
}