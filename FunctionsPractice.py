# string = "abbghjkhffjygbffghbvfvdasfkjhuehffjiuosyitgbewffj"
# substring = "ffj"

# sub_pos = (string.find(substring))
# newstart = (sub_pos+ len(substring))




# nums = [1,2,3,4,5]
# print(nums.sort())

# if nums.sort() == nums:
#     result = True
# elif nums.sort(reverse=True) == nums:
#     result = True
# else:
#     result = False
# print(result)


nums = [2,7,14,75,6]
new_array=[]
for i in range (len(nums)):
    for num in nums:
        if num + nums[i] == 9:
            print(num,nums[i])
print (new_array)