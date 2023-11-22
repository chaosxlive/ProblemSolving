# https://leetcode.com/problems/find-the-maximum-achievable-number/

# @param {Integer} num
# @param {Integer} t
# @return {Integer}
def the_maximum_achievable_x(num, t)
    return num + (t << 1)
end