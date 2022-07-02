/**
 * @param {string[]} words
 * @return {string}
 */
function isPalindrome(x){
    var p1 = 0
    var p2 = x.length - 1
    while (p1<=p2){
        if(x[p1]!=x[p2]){
            return false
        }
        p1++
        p2--
    }
    return true
}
var firstPalindrome = function(words) {
   
    for(let i=0;i<words.length;i++){
        if(isPalindrome(words[i])){
            let word = words[i]
            console.log(word)
            return word
        }
    }
    return ""

};