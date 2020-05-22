/**
 * https://leetcode.com/problems/sort-characters-by-frequency/
 *
 * Given a string, sort it in decreasing order based on the frequency of characters.
**/

class Solution {
    public String frequencySort(String s) {
       
        String result = "";
        
        HashMap<String, Integer> hmap = new HashMap<String, Integer>();
        
        for(String ch : s.split("")) {
            hmap.put(ch, hmap.getOrDefault(ch,0) + 1);
        }
        
        PriorityQueue<Map.Entry<String, Integer>> pq = new PriorityQueue<>((a, b) -> 
            a.getValue() == b.getValue() ? a.getKey().compareTo(b.getKey()) : b.getValue() - a.getValue());
        
        Iterator it = hmap.entrySet().iterator();
        for(Map.Entry e : hmap.entrySet()) {
            pq.add(e);
        }
        int n = pq.size();
        for(int i = 0; i < n; i++){
            Map.Entry<String, Integer> e = pq.poll();
            result += e.getKey().repeat(e.getValue());           
        }
        return result;
    }
}