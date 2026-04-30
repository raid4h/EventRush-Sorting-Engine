class SortEngine:
    def compare_priority(self, a, b):
        #higher urgency first
        if a[1] != b[1]:
            return a[1] > b[1]
        #smaller timestamp first
        if a[4] != b[4]:
            return a[4] < b[4]
        #smaller ID first
        return a[0] < b[0]

    #Task 1 & 2
    def merge_sort_requests(self, arr):
        if len(arr) <= 1: return arr
        mid = len(arr) // 2
        left = self.merge_sort_requests(arr[:mid])
        right = self.merge_sort_requests(arr[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        res = []
        i = j = 0
        while i < len(left) and j < len(right):
            if self.compare_priority(left[i], right[j]):
                res.append(left[i]); i += 1
            else:
                res.append(right[j]); j += 1
        res.extend(left[i:]); res.extend(right[j:])
        return res

    #Task 3 & 4
    def quick_sort_zone(self, arr, low, high):
        if low < high:
            p = self.partition_zone(arr, low, high)
            self.quick_sort_zone(arr, low, p - 1)
            self.quick_sort_zone(arr, p + 1, high)

    def partition_zone(self, arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if (arr[j][3] < pivot[3]) or (arr[j][3] == pivot[3] and arr[j][1] > pivot[1]):
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return i + 1

    #Task 5
    def top_k(self, arr, k):
        if k <= 0: return []
        res = self.merge_sort_requests(arr)
        return res[:k]

    #Task 6
    def is_dangerous(self, arr):
        if len(arr) < 10: return False
        inc = all(arr[i][1] <= arr[i+1][1] for i in range(len(arr)-1))
        dec = all(arr[i][1] >= arr[i+1][1] for i in range(len(arr)-1))
        return inc or dec

    #Task 7
    def merge_custom(self, arr, left, mid, right):
        #helper for custom merge logic
        L = arr[left:mid+1]
        R = arr[mid+1:right+1]
        i = j = 0
        k = left
        while i < len(L) and j < len(R):
            #rule: smaller service time (2), higher urgency (1), smaller timestamp (4)
            if (L[i][2] < R[j][2]) or \
               (L[i][2] == R[j][2] and L[i][1] > R[j][1]) or \
               (L[i][2] == R[j][2] and L[i][1] == R[j][1] and L[i][4] < R[j][4]):
                arr[k] = L[i]; i += 1
            else:
                arr[k] = R[j]; j += 1
            k += 1
        while i < len(L): arr[k] = L[i]; i += 1; k += 1
        while j < len(R): arr[k] = R[j]; j += 1; k += 1

    #Task 8
    def quick_sort_three_way(self, arr, low, high):
        if low >= high: return
        lt, i, gt = low, low + 1, high
        pivot = arr[low][1]
        while i <= gt:
            if arr[i][1] > pivot:
                arr[i], arr[lt] = arr[lt], arr[i]
                i += 1; lt += 1
            elif arr[i][1] < pivot:
                arr[i], arr[gt] = arr[gt], arr[i]
                gt -= 1
            else:
                i += 1
        self.quick_sort_three_way(arr, low, lt - 1)
        self.quick_sort_three_way(arr, gt + 1, high)

    #Task 9
    def merge_sort_desc(self, arr):
        if len(arr) <= 1: return arr
        mid = len(arr) // 2
        left = self.merge_sort_desc(arr[:mid])
        right = self.merge_sort_desc(arr[mid:])
        
        #merging logic for timestamp (index 4) descending
        res = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i][4] >= right[j][4]:
                res.append(left[i]); i += 1
            else:
                res.append(right[j]); j += 1
        res.extend(left[i:]); res.extend(right[j:])
        return res
    
if __name__ == "__main__":
    engine = SortEngine()

    #sample data: [id, urgency, service_time, zone, timestamp]
    data = [
        [101, 5, 20, 3, 15],
        [102, 10, 30, 1, 10],
        [103, 5, 10, 2, 5],
        [104, 10, 15, 1, 8]
    ]

    print("Task 1: Merge Sort (Priority)")
    #should show 104 first (higher urgency 10, earlier timestamp 8)
    print(engine.merge_sort_requests(data))

    print("\nTask 2: Quick Sort (Zone)")
    #should group by zone 1, then 2, then 3
    zone_data = data.copy()
    engine.quick_sort_zone(zone_data, 0, len(zone_data)-1)
    print(zone_data)

    print("\nTask 3: Top-K Urgent (K=2)")
    print(engine.top_k(data, 2))

    print("\nTask 4: Dangerous Input Check")
    dangerous_data = [[i, i, 10, 1, i] for i in range(20)] #already sorted
    print(f"Is already-sorted dangerous? {engine.is_dangerous(dangerous_data)}")

    print("\nTask 5: Custom Merge Only")
    #rule: smaller service time, higher urgency, smaller timestamp
    #we provide an array with two "halves" that are internally sorted by the rule
    custom_data = [
        [101, 5, 10, 1, 20], [102, 10, 15, 1, 20], # Left half (service times 10, 15)
        [103, 8, 5, 1, 20],  [104, 2, 12, 1, 20]   # Right half (service times 5, 12)
    ]
    #merge_custom(arr, left, mid, right)
    engine.merge_custom(custom_data, 0, 1, 3)
    print(f"Merged by custom rules: {custom_data}")

    print("\nTask 6 (TODO 8): 3-Way Quick Sort")
    #sorts by urgency descending, excellent for many duplicates
    three_way_data = [
        [101, 5, 20, 1, 10],
        [102, 10, 20, 1, 10],
        [103, 5, 20, 1, 10],
        [104, 10, 20, 1, 10],
        [105, 1, 20, 1, 10]
    ]
    engine.quick_sort_three_way(three_way_data, 0, len(three_way_data)-1)
    print(f"3-Way Sorted (Urgency Desc): {three_way_data}")

    print("\nTask 7: Reverse Merge Sort (Timestamp)")
    print(engine.merge_sort_desc(data))
