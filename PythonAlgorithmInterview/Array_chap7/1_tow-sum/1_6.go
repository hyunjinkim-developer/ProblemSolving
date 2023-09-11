// same algorith with 1_3.ipynb
// with the same algorithm, go language is 6 times faster than python

func twoSum(nums []int, target int) []int {
    numsMap := make(map[int]int)

    // save as dictionary by swaping key, value pair
    for i, num := range nums {
        numsMap[num] = i
    }

    // search with target - number that is chosen
    for i, num := range nums {
        if j, ok := numsMap[target - num]; ok && i != j {
            return []int{i, j}
        }
    }

    return []int{}
}