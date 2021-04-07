def bubble_sort(nums):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = (nums[i+1], nums[i])
                sorted = False
    return nums

if __name__ == "__main__":
    list_1 = [1, 7, 9, 4, 3, 4, 2]
    print(bubble_sort(list_1))
