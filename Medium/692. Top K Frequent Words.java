/*
 *https://leetcode.com/problems/top-k-frequent-words/
 *
 *Given a non-empty list of words, return the k most frequent elements.
 *
 *Your answer should be sorted by frequency from highest to lowest. If two words have the same         frequency, then the word with the lower alphabetical order comes first.
 *
 */

class Solution {
    public List<String> topKFrequent(String[] words, int k) {
        
        Map<String, Integer> m = new HashMap<>(words.length);
        
        for(String word : words){
            
            if(m.containsKey(word)){
                m.put(word, m.get(word) + 1);
            }else
                m.put(word, 1);
        }

        PriorityQueue<Map.Entry<String, Integer>> pq = new PriorityQueue<>(m.size(), (a,b) -> {
           return a.getValue() == b.getValue() ? a.getKey() .compareTo(b.getKey()) : b.getValue() - a.getValue();
        });
    
        for (Map.Entry<String, Integer> e : m.entrySet()) {
            pq.add(e);
        }
        
        List<String> result = new ArrayList<>(k);
        for(int i = 0; i < k; i++){
            result.add(pq.poll().getKey());
        }
        
        return result;
    }
}