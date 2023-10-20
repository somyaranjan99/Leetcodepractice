/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    let newMap={}
for (let i=0;i<=nums.length;i++){
    if(nums[i] in newMap){
        newMap[nums[i]] +=1
    }else{
        newMap[nums[i]] =1
        
    }
}
for (const [key,value] of Object.entries(newMap)){
    if (value ===1){
        return key
    }

}
return -1
};