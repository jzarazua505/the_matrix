from time import time

def bubble_sort(nums):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = (nums[i+1], nums[i])
                sorted = False
    return nums

def insertion_sort(nums):
    for i in range(1, len(nums)):
        j = i
        while j > 0 and nums[j-1] > nums[j]:
            nums[j-1], nums[j] = (nums[j], nums[j-1])
            j = j - 1
    return nums

if __name__ == "__main__":
    list_1 = [1, 7, 9, 4, 3, 4, 2]
    start_time = time()
    print(bubble_sort(list_1))
    print((time() - start_time) * 100000)
    start_time = time()
    print(insertion_sort(list_1))
    print((time() - start_time) * 100000)
