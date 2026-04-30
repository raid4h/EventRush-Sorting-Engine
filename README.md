An assignment for my Design & Analysis of Algorithms course.

Algorithm Analysis: EventRush Sorting Engine

Merge Sort (Stability & Reliability):
In Task 1 and 7, I implemented Merge Sort. This algorithm uses a Divide and Conquer approach, splitting the array into halves until they reach a size of one, then merging them back in order. I chose Merge Sort for priority requests because it is stable. Stability ensures that if two requests have the same urgency and timestamp, their original relative order is preserved, which is critical for fairness in emergency services.

Quick Sort (In-Place Efficiency):
In Task 3 and 8, I implemented Quick Sort and 3-Way Quick Sort. Quick Sort works by selecting a pivot and partitioning the array around it. It is generally faster than Merge Sort and uses less memory (In-place). However, Task 8 uses 3-Way Partitioning (Dutch National Flag algorithm), which is significantly more efficient when there are many duplicate values (like many requests having the same "Urgency" level).

Computational Complexity and Dangerous Inputs:
While Quick Sort has an average time complexity of O(n log n), it has a "dangerous" worst-case of O(n²). This happens when the input is already sorted or reverse-sorted and the pivot is chosen naively (Task 6). In contrast, Merge Sort maintains a guaranteed O(n log n) complexity regardless of the input order, making it more predictable for high-stakes emergency systems.

Conclusion:
By combining these two paradigms, the EventRush engine can handle different scenarios: using Merge Sort when stability and guaranteed timing are needed, and Quick Sort when memory efficiency and raw speed are the priority for localized zones.

