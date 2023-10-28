/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var subarraySum = function(nums, k) {
  let res=0
	let presum=0
	const dict1={0:1}
	for(let num of nums){
	  presum =presum+num
	  if (presum-k in dict1){
	    res =res+dict1[presum-k]
	  }
	  if (presum in dict1){
	      dict1[presum] ++
	    }else{
      dict1[presum]=1
	      
	    }       
	     
	  
	}

    return res
};