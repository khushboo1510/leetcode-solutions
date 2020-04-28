/*
 *You have a queue of integers, you need to retrieve the first unique integer in the queue.
 *
 *Implement the FirstUnique class:
 *FirstUnique(int[] nums) Initializes the object with the numbers in the queue.
 *int showFirstUnique() returns the value of the first unique integer of the queue, and returns -1 if there is no   such integer.
 *void add(int value) insert value to the queue.
 *
 */

class FirstUnique {

    LinkedHashSet<Integer> linkedset;
    HashSet<Integer> set;
    public FirstUnique(int[] nums) {
        linkedset = new LinkedHashSet<Integer>();
        set = new HashSet<>();
        for(int i = 0; i < nums.length; i++){
            if(set.contains(nums[i])){
                linkedset.remove(nums[i]);
            }
            else{
                linkedset.add(nums[i]);
                set.add(nums[i]);
            }
        }
    }
    
    public int showFirstUnique() {
        Iterator<Integer> iterator = linkedset.iterator();
        if(iterator.hasNext())
            return iterator.next();
        return -1;
    }
    
    public void add(int value) {
        if(set.contains(value)){
            linkedset.remove(value);
        }
        else{
            linkedset.add(value);
            set.add(value);
        }
    }
}

/**
 * Your FirstUnique object will be instantiated and called as such:
 * FirstUnique obj = new FirstUnique(nums);
 * int param_1 = obj.showFirstUnique();
 * obj.add(value);
 */