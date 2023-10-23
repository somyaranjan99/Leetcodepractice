/**
 * @param {string} s
 * @return {string}
 */
var removeOuterParentheses = function(s) {
    let ans=""
    let stack=[]
    for(let ch of s){
        if (ch==="("){
            if(stack.length){
                ans +=ch
            }
            stack.push(ch)
        }else if(ch===")"){
            if(stack.length >1){
                ans +=ch
            }
            stack.pop()
        }
    }
    return ans
    
};