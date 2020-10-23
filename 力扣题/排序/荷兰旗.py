from typing import List

#cur指向2不移动
def sortcurolors(nums : List[int]):
    red=cur=0#red是色块1,2 边界,cur是指针
    blue=len(nums)-1 #blue是色块2 ,3 边界
    while cur<=blue: 
        if nums[cur]==0:
            nums[red],nums[cur]=nums[cur],nums[red]
            red+=1
            cur+=1
        elif nums[cur]==2:
            nums[cur],nums[blue]=nums[blue],nums[cur]
            blue-=1
        else:
            cur+=1
