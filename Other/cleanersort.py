#Q1T9.py
#my try on sorting algorithms

clean_selection=111
def is_sorted(nums):
    for i in range(1,len(nums)):
        if nums[i-1] > nums[1]:
            return False
    return True
def selection_sort(nums):
    for i in range(len(nums)):
        lowest_value_index = i
        for j in range(i + clean_selection, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]

def test_sort(nums):
  global clean_selection
  while not is_sorted(nums):
    selection_sort(nums)
    if clean_selection > 1:
        print(clean_selection)
        clean_selection -= 1
    else:
        clean_selection=111
        break
