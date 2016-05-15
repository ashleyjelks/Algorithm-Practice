// Given 2 strings, check if one string is a permutation of the other. 

function isPermutation(str1, str2) {
  var charMap1 = {};
  var charMap2 = {};
  for (i=0; str1.length > i; i++){
     if (!charMap1.hasOwnProperty(str1[i])) {
       charMap1[str1[i]] = 1;
     } else {
       charMap1[str1[i]] = charMap1[str1[i]] + 1;
     }
  }
  for (i=0; str2.length > i; i++){
     if (!charMap2.hasOwnProperty(str2[i])) {
       charMap2[str2[i]] = 1;
     } else {
       charMap2[str2[i]] = charMap2[str2[i]] + 1;
     }
  }
 
  for (var eachChar in charMap1) { 
    if (charMap2.hasOwnProperty(eachChar)) { 
      if (charMap1[eachChar] === charMap2[eachChar]) {
      } else {
        return false;
      } 
     } 
    return true;  
  } else {
    return false;
  }
}