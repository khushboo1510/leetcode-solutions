/*
 *https://leetcode.com/problems/lru-cache/

 *Design and implement a data structure for Least Recently Used (LRU) cache. It should support the
 *following operations: get and put.
 *
 *get(key) - Get the value (will always be positive) of the key if the key exists in the cache,
 *otherwise return -1.
 *
 *put(key, value) - Set or insert the value if the key is not already present. When the cache reached
 *its capacity, it should invalidate the least recently used item before inserting a new item.
 *
 *The cache is initialized with a positive capacity.
 *
 *Follow up:
 *Could you do both operations in O(1) time complexity?
 
 *Another Method: create doubly linkedlist. Front points to most recently used nodes and rear points
 *to least used pages. Maintain hashmap pointing to each node for fetching nodes in O(1) and
 *maintaining capacity of cache.
*/

class LRUCache {
    
    LinkedHashMap<Integer, Integer> linkedmap;
    int s = 0;
    
    public LRUCache(int capacity) {
        linkedmap = new LinkedHashMap<Integer, Integer>(capacity); 
        s = capacity;
    }
    
    public int get(int key) {
        if(linkedmap.containsKey(key)){
            int value = linkedmap.remove(key);
            linkedmap.put(key, value);
            return value;
        }else
            return -1;
    }
    
    public void put(int key, int value) {
        if(linkedmap.containsKey(key)){
            linkedmap.remove(key);
        }else if(linkedmap.size() == s){
            linkedmap.remove(linkedmap.entrySet().iterator().next().getKey());
        }
        linkedmap.put(key, value);
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */