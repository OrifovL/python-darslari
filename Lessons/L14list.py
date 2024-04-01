# A = int(input('A'))
# D = int(input('D'))
# n = int(input('n'))
# lst = []
# for i in range(A,n,D):



# Davlatlar = ["O'zbekiston", "Qozog'iston", "Avg'oniston", "Tojikiston","Rassiya","Qirg'iziston"]

# print(Davlatlar[0],Davlatlar[1],Davlatlar[2],Davlatlar[3],Davlatlar[4],Davlatlar[5])

# print(len(Davlatlar))

# print(sorted(Davlatlar))

# Davlatlar.reverse()
# print(Davlatlar)

# Davlatlar.sort()
# print(Davlatlar)

# Davlatlar.sort(reverse=True)
# print(Davlatlar)



# nums = []
# for i in range(120,1201,2):
#     nums.append(i)

# print(nums)

# s = 0
# for a in nums:
#     s+=a
# print(s)
    
# a = max(nums)
# b = min(nums)
# c = a - b
# print(c)

# a = len(nums)
# print(a)

# print(nums[:20])

# print(nums[int(len(nums)/2):int(len(nums)/2+20)])

# print(nums[-20:-1])
# print(nums[len(nums)-20:])



taomlar = ["kabob","somsa","osh","manti","barak","shurva","dimlama","amlet"]

nonushta = taomlar.copy()

nonushta.remove("kabob")
nonushta.remove("osh")
nonushta.remove("dimlama")
nonushta.remove("somsa")
nonushta.append("tuxum")
nonushta.append("sut")
print(nonushta)

print(taomlar)

nonushta.insert(0,"qaymoq va non")
print(nonushta)

tuple(nonushta)
print(nonushta)

