/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    if (s.length == 1){ return true }
    
    s = s.replace(/[^a-zA-Z0-9]/g, "").toLowerCase()
    
    var p1 = 0;
    var p2 = s.length-1
    
    while (p1<=p2){
         if (s[p1] != s[p2]){
             return false
         }
        p1++
        p2--
    }
    
    return true
       
};