# Galadriel Cho
# Bergen County Academies
# Junior Division

file = open("jr-sample-input.txt", "r")

for line in file:
    changing = []
    nums = line.strip().split()
    for i in str(nums[0]):
        changing.append(int(i))
    p = int(nums[1]) * -1
    d = int(nums[2])
    if 0 <= changing[p] <= 4:
        dummy = str(changing[p] + d)
        changing[p] = int(dummy[-1])
    elif 5 <= changing[p] <= 9:
        dummy = changing[p] - d
        if dummy < 0:
            dummy *= -1
        dummy = str(dummy)
        changing[p] = int(dummy[0])
    for x in range(p + 1, 0, +1):
        changing[x] = 0
    for i in changing:
        print(i,end="")
    print()
