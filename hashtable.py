# Hash Table
# 1. What is a Hash Table?
# A Hash Table is a data structure that maps keys to values for highly efficient lookup.

# 2. How does Hash Table work?
# Given a (key, value) pair, hash table is data structure which converts the key to an index and then store the value somewhere using that index. It can be implemented by an array of a linked list and a hash code function.

# 3. How does open addressing work?
# Open Addressing (close hashing) is method of collision resolution in hash tables. It’s resolved by probing. Probing includes linear probing, quadratic probing and double hashing.

# 4. What's the problem of linear probing?
# Deletion will be a problem. If one key involves a chain of several probes, it will be lost if somewhere along the chain, one of the other keys is removed, leaving an empty slot. Thus, you can't find the value stored after probing.

# 5. What is separate chaining?
# The idea is to make each cell of hash table point to a linked list of records that have same hash function value.

# 6. Hash Table insertion, deletion, search, and collision
# - Constant, amortized O(1)
# - worst case O(n) for search & deletion (add flag to fix it)

# 7. Hash Table is slow, why?
# - poor hash function
# - bad open addressing strategy

# 8.Use hash table to store data, but there is much more data than the machine's RAM, how to deal with that?
# add one more machine, rehash and reconstruct the hash table


#Open addressing

# # In another strategy, called open addressing, all entry records are stored in the bucket array itself. When a new entry has to be inserted, the buckets are examined, starting with the hashed-to slot and proceeding in some probe sequence, until an unoccupied slot is found. When searching for an entry, the buckets are scanned in the same sequence, until either the target record is found, or an unused array slot is found, which indicates that there is no such key in the table.[16] The name "open addressing" refers to the fact that the location ("address") of the item is not determined by its hash value. (This method is also called closed hashing; it should not be confused with "open hashing" or "closed addressing" that usually mean separate chaining.)
#
# Well-known probe sequences include:
#
# Linear probing, in which the interval between probes is fixed (usually 1)
# Quadratic probing, in which the interval between probes is increased by adding the successive outputs of a quadratic polynomial to the starting value given by the original hash computation
# Double hashing, in which the interval between probes is computed by a second hash function
# A drawback of all these open addressing schemes is that the number of stored entries cannot exceed the number of slots in the bucket array. In fact, even with good hash functions, their performance dramatically degrades when the load factor grows beyond 0.7 or so. For many applications, these restrictions mandate the use of dynamic resizing, with its attendant costs.[citation needed]
#
# Open addressing schemes also put more stringent requirements on the hash function: besides distributing the keys more uniformly over the buckets, the function must also minimize the clustering of hash values that are consecutive in the probe order. Using separate chaining, the only concern is that too many objects map to the same hash value; whether they are adjacent or nearby is completely irrelevant.[citation needed]
#
# Open addressing only saves memory if the entries are small (less than four times the size of a pointer) and the load factor is not too small. If the load factor is close to zero (that is, there are far more buckets than stored entries), open addressing is wasteful even if each entry is just two words.
#
#
# This graph compares the average number of cache misses required to look up elements in tables with chaining and linear probing. As the table passes the 80%-full mark, linear probing's performance drastically degrades.
# Open addressing avoids the time overhead of allocating each new entry record, and can be implemented even in the absence of a memory allocator. It also avoids the extra indirection required to access the first entry of each bucket (that is, usually the only one). It also has better locality of reference, particularly with linear probing. With small record sizes, these factors can yield better performance than chaining, particularly for lookups. Hash tables with open addressing are also easier to serialize, because they do not use pointers.[citation needed]
#
# On the other hand, normal open addressing is a poor choice for large elements, because these elements fill entire CPU cache lines (negating the cache advantage), and a large amount of space is wasted on large empty table slots. If the open addressing table only stores references to elements (external storage), it uses space comparable to chaining even for large records but loses its speed advantage.[citation needed]
#
# Generally speaking, open addressing is better used for hash tables with small records that can be stored within the table (internal storage) and fit in a cache line. They are particularly suitable for elements of one word or less. If the table is expected to have a high load factor, the records are large, or the data is variable-sized, chained hash tables often perform as well or better.[citation needed]
#
# Ultimately, used sensibly, any kind of hash table algorithm is usually fast enough; and the percentage of a calculation spent in hash table code is low. Memory usage is rarely considered excessive. Therefore, in most cases the differences between these algorithms are marginal, and other considerations typically come into play