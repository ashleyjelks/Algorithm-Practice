/*Implement an algorithm to determine if a string has all
  unique characters. (This solution assumes that a string with 1 
  character or an empty string is valid and thus contains unique characters.)*/

function isUnique(str1) {
  var charMap = {};
  if (str1 === '' || str1.length === 1) {
    return true;
  } else {
    for (i=0; str1.length > i; i++) {
        charMap[str1[i]] = i
        if (Object.keys(charMap).length > 1){
            return false
        } else {
            return true
        }
    } 
  }    
}