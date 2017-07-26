package main

import (
	"strings"
	"fmt"
)

func RepeatStr(repititions int, value string) string {
	return strings.Repeat(value, repititions)
}

func main() {
	str := RepeatStr(4, "hello ")
	fmt.Println(str)
}
