nums = 27
def function(nums):
    while nums > 0:
        if nums == 0:
            return True
        nums = nums/3
    return False

print(function(nums))