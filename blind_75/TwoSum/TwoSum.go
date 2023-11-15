package main

import "fmt"

func main() {
    fmt.Println("Hello, world!")
	var input = [] int{0,1,2,3,4,5}
	var output = twoSum(input, 1)
	print(output[0])
	print(output[1])
}

func twoSum(nums []int, target int) []int {
	var retArr = []int{-1,1}
	return retArr
}