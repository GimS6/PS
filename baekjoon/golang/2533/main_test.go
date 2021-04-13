package main

import (
	"fmt"
	"log"
	"testing"
)

func TestSolution(t *testing.T) {
	defer func() {
		if err := recover(); err != nil {
			log.Println("panic occurred:", err)
		}
	}()

	N = 8
	graph = [][]int{
		[]int(nil),
		{2, 3, 4},
		{1, 5, 6},
		{1},
		{1, 7, 8},
		{2},
		{2},
		{4},
		{4},
	}

	isVisited = make([]bool, N+1)
	d = make([][2]int, N+1)

	dfs(1)

	fmt.Println(min(d[1][0], d[1][1]))
}
