def quick_sort(arr):
    if len(arr) <= 1: # 遞迴結束條件
        return arr
    else:
        star = arr[0]
        less = [x for x in arr[1:] if x <= star] # 左邊指標、生成左半部分arr
        greater = [x for x in arr[1:] if x > star] # 右邊指標、生成右半部分arr
        return quick_sort(less) + [star] + quick_sort(greater) #合併


test = [33, 67, 8, 13, 54, 119, 3, 84, 25, 41]
print("BEFORE:",test)
sorted_test = quick_sort(test)
print("AFTER:",sorted_test)


