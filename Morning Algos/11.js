/* 
    Balance Index

    Here, a balance point is ON an index, not between indices.

    Return the balance index where sums are equal on either side
    (exclude its own value).

    Return -1 if none exist.
*/

const nums1 = [-2, 5, 7, 0, 3];
const expected1 = 2;

const nums2 = [9, 9];
const expected2 = -1;

/**
 * Finds the balance index in the given array where the sum to the left of the
 *    index is equal to the sum to the right of the index.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums
 * @returns {number} The balance index or -1 if there is none.
 */
function balanceIndex(nums) {
    var left = []
    var right = []
    if (nums.length % 2 == 0){
        return -1
    }
    for (let i = 0; i < nums.length; i++) {
        for (let j = nums.length - 1; j < nums.length; j--) {
            if(i=j){
                break
            }
            left.push(i)
        }
    }
        return left.length
    }


console.log(balanceIndex(nums1))
console.log(balanceIndex(nums2))

/*****************************************************************************/