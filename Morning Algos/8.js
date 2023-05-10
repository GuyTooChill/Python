/* 
Parens Valid

Given an str that has parenthesis in it
return whether the parenthesis are valid
*/

const str1 = "Y(3(p)p(3)r)s";
const expected1 = true;

const str2 = "N(0(p)3";
const expected2 = false;
// Explanation: not every parenthesis is closed.

const str3 = "N(0)t ) 0(k";
const expected3 = false;
// Explanation: because the second ")" is premature: there is nothing open for it to close.

const str4 = "a(b))(c";
const expected4 = false;
// Explanation: same number of opens and closes but the 2nd closing closes nothing.

/**
 * Determines whether the parenthesis in the given string are valid.
 * Each opening parenthesis must have exactly one closing parenthesis.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {boolean} Whether the parenthesis are valid.
 */
function parensValid(str) { 
    let paranthesis = [];

    for(let i = 0; i < str.length; i++){
        if (str[i] == "("){
            paranthesis.push()
            continue;
        }
        
    }
}

console.log(parensValid(str1))


/*****************************************************************************/


/* 
Braces Valid

Given a string sequence of parentheses, braces and brackets, determine whether it is valid. 
*/

const str5 = "W(a{t}s[o(n{ c}o)m]e )h[e{r}e]!";
const expected5 = true;

const str6 = "D(i{a}l[ t]o)n{e";
const expected6 = false;

const str7 = "A(1)s[O (n]0{t) 0}k";
const expected7 = false;

/**
 * Determines whether the string's braces, brackets, and parenthesis are valid
 * based on the order and amount of opening and closing pairs.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {boolean} Whether the given strings braces are valid.
 */
function bracesValid(str) {
    let paranthesis = "()[]{}";

    for (i=0; i<str.length;i++){

    }
}

console.log(bracesValid(str5))
console.log(bracesValid(str6))
console.log(bracesValid(str7))





// var parentheses = "[]{}()",
// stack = [],
// i, character, bracePosition;

// for(i = 0; character = str[i]; i++) {
// bracePosition = parentheses.indexOf(character);

// if(bracePosition === -1) {
//     continue;
// }

// if(bracePosition % 2 === 0) {
//     stack.push(bracePosition + 1);
// } else {
//     if(stack.length === 0 || stack.pop() !== bracePosition) {
//     return false;
//     }
// }
// }
// return stack.length === 0;