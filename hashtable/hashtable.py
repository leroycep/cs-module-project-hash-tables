class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.items = [None] * max(capacity, MIN_CAPACITY)
        self.stored_items = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.items)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.stored_items / len(self.items)

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        hash = 0xcbf29ce484222325
        for byte in key.encode():
            hash *= 0x100000001b3
            hash ^= byte
        return hash

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        pass

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % len(self.items)
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        if self.get_load_factor() > 0.7:
            self.resize(len(self.items) * 2)

        index = self.hash_index(key)
        if self.items[index] is None:
            self.items[index] = HashTableEntry(key, value)
        else:
            prev_entry = self.items[index]
            current_entry = self.items[index]
            while current_entry != None:
                if current_entry.key == key:
                    current_entry.value = value
                    # Return here so that:
                    # - we skip iterating through the rest of the entries
                    # - the number of stored items is not incremented
                    return
                prev_entry = current_entry
                current_entry = current_entry.next
            # Append HashTableEntry to end of linked list of entries
            prev_entry.next = HashTableEntry(key, value)
        self.stored_items += 1

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        if self.get_load_factor() < 0.2:
            self.resize(len(self.items) // 2)

        index = self.hash_index(key)

        prev_entry = None
        current_entry = self.items[index]
        while current_entry is not None:
            if current_entry.key == key:
                if prev_entry is not None:
                    prev_entry.next = current_entry.next
                else:
                    self.items[index] = current_entry.next
                self.stored_items -= 1
                return
            prev_entry = current_entry
            current_entry = current_entry.next
        print("Value was not found in hashmap")

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        if self.items[index] is None:
            return None
        else:
            current_entry = self.items[index]
            while current_entry != None:
                if current_entry.key == key:
                    return current_entry.value
                current_entry = current_entry.next
            return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        old_list = self.items
        self.items = [None] * max(new_capacity, MIN_CAPACITY)
        self.stored_items = 0
        for entry in old_list:
            current_entry = entry
            while current_entry is not None:
                self.put(current_entry.key, current_entry.value)
                current_entry = current_entry.next


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
