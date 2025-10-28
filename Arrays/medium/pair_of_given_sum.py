#finding the pair of given sum

def pair_of_sum(a,target_num):
    left = 0
    right = len(a)-1

    while left < right:
        current_sum = a[left] + a[right]

        if current_sum == target_num:
            print("pair found", a[left],a[right])
            left+=1
            right+=1
    
        if current_sum < target_num:
            left+=1
        else:
            right-=1

if __name__=="__main__":
    a = [1,2,3,4,5,6]
    pair_of_sum(a,7)



