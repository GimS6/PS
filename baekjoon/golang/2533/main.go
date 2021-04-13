package main

import (
	"bufio"
	"os"
	"strconv"
)

var (
	N         int
	graph     [][]int
	isVisited []bool
	d         [][2]int
)

func main() {
	defer wr.Flush()
	N = scanInt()
	graph = make([][]int, N+1)

	for i := 0; i < N-1; i++ {
		x, y := scanInt(), scanInt()
		graph[x] = append(graph[x], y)
		graph[y] = append(graph[y], x)
	}

	isVisited = make([]bool, N+1)
	d = make([][2]int, N+1)

	dfs(1)

	wr.WriteString(strconv.Itoa(min(d[1][0], d[1][1])))
}

func dfs(root int) {
	isVisited[root] = true

	// 초깃값 설정
	d[root][1] = 1

	for i := 0; i < len(graph[root]); i++ {
		child := graph[root][i]

		if isVisited[child] {
			continue
		}

		dfs(child)

		d[root][0] += d[child][1]
		d[root][1] += min(d[child][0], d[child][1])
	}
}

func min(a, b int) int {
	if a > b {
		return b
	}
	return a
}

var (
	sc *bufio.Scanner
	wr *bufio.Writer
)

func init() {
	sc = bufio.NewScanner(os.Stdin)
	sc.Split(bufio.ScanWords)
	wr = bufio.NewWriter(os.Stdout)
}

func scanInt() int {
	sc.Scan()
	num, _ := strconv.Atoi(sc.Text())
	return num
}
