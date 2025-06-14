class Solution {
public:
    vector<vector<int>> findDifference(vector<int>& nums1, vector<int>& nums2) {
        unordered_set<int> set1(nums1.begin(),nums1.end());
        unordered_set<int> set2(nums2.begin(),nums2.end());

        vector<int> onlyInNums1;
        vector<int> onlyInNums2;

        for(int num : set1){
            if(set2.find(num) == set2.end()){
                onlyInNums1.push_back(num);
            }
        }

        
        for(int num : set2){
            if(set1.find(num) == set1.end()){
                onlyInNums2.push_back(num);
            }
        }

        return {onlyInNums1,onlyInNums2};
        
    }
};

/*

Absolutely! Since you're new to C (and C++), I’ll walk you through the C++ code **line-by-line** and explain what's happening in simple terms. Even if your background is mostly in Python, you'll be able to follow along easily.

---

### ✅ Full C++ Function

```cpp
#include <vector>
#include <unordered_set>
using namespace std;

vector<vector<int>> findDifference(vector<int>& nums1, vector<int>& nums2) {
```

* `#include <vector>` and `#include <unordered_set>`: These are **header files** that include the standard C++ data structures — `vector` is like Python's list, and `unordered_set` is like Python's set.
* `using namespace std;`: This lets us avoid writing `std::` before every standard object (like `vector` or `cout`).
* `vector<vector<int>> findDifference(...)`: This defines a function named `findDifference`. It returns a 2D vector (`vector of vectors of ints`), similar to a list of lists in Python.
* The function takes two arguments: references to vectors of integers (`nums1` and `nums2`).

---

```cpp
    unordered_set<int> set1(nums1.begin(), nums1.end());
    unordered_set<int> set2(nums2.begin(), nums2.end());
```

* This converts `nums1` and `nums2` into sets (to keep only unique elements).
* `unordered_set` is a hash-based set, like Python's `set`.
* `nums1.begin()` and `nums1.end()` give iterators that allow you to copy all values from `nums1` into `set1`.

---

```cpp
    vector<int> onlyInNums1;
    vector<int> onlyInNums2;
```

* These two vectors will store the **output values**:

  * `onlyInNums1`: Values in `nums1` not in `nums2`
  * `onlyInNums2`: Values in `nums2` not in `nums1`

---

```cpp
    for (int num : set1) {
        if (set2.find(num) == set2.end()) {
            onlyInNums1.push_back(num);
        }
    }
```

* This is a **range-based for loop**, similar to `for num in set1` in Python.
* For every number in `set1`, we check if it **does not exist in `set2`**.
* `set2.find(num) == set2.end()` means “`num` is not found in `set2`”.
* If it's unique to `set1`, we add it to `onlyInNums1`.

---

```cpp
    for (int num : set2) {
        if (set1.find(num) == set1.end()) {
            onlyInNums2.push_back(num);
        }
    }
```

* Same logic as above, but reversed: find elements unique to `nums2`.

---

```cpp
    return {onlyInNums1, onlyInNums2};
}
```

* Returns a 2D vector that contains both result lists.

---

### ✅ Summary of Concepts

| Concept              | C++ Code                   | Python Equivalent      |
| -------------------- | -------------------------- | ---------------------- |
| List                 | `vector<int>`              | `list[int]`            |
| Set                  | `unordered_set<int>`       | `set[int]`             |
| Loop over collection | `for (int x : collection)` | `for x in collection:` |
| Append to list       | `vec.push_back(x)`         | `list.append(x)`       |
| Check if in set      | `set.find(x) != set.end()` | `x in set`             |

---

Let me know if you want me to explain the `main()` function or run through an example with input/output — happy to help you gain confidence in C++ step-by-step!


*/