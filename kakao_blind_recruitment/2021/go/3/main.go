package main

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
	"sync"
)

// 4가지 항목을 반드시 선택해야 함
// 각각 개발언어, 지원 직군, 지원 경력, 소울푸드
// and 코딩테스트 결과 점수
// 인재영입을 위해 지원 조건을 선택하면 해당 조건에 맞는
// 지원자가 몇 명인지 쉽게 알 수 있는 도구를 만들려고 함

// "코딩테스트에 java로 참여했으며, backend 직군을 선택했고, junior 경력이면서,
// 소울푸드로 pizza를 선택한 사람 중 코딩테스트 점수를 50점 이상 받은 지원자는 몇 명인가?"

func Iter(params ...[]string) chan []string {
	c := make(chan []string)

	var wg sync.WaitGroup

	wg.Add(1)
	iterate(&wg, c, []string{}, params...)

	go func() {
		wg.Wait()
		close(c)
	}()

	return c
}

func iterate(wg *sync.WaitGroup, channel chan []string, result []string, params ...[]string) {
	defer wg.Done()

	if len(params) == 0 {
		channel <- result
		return
	}

	p, params := params[0], params[1:]

	for i := 0; i < len(p); i++ {
		wg.Add(1)

		resultCopy := append([]string{}, result...)

		go iterate(wg, channel, append(resultCopy, p[i]), params...)
	}
}

func BinarySearch(numbers []int, length int, searchNum int) int {
	answer := -1
	start := 0
	end := length - 1

	for start <= end {
		middle := (start + end) / 2

		if numbers[middle] == searchNum {
			answer = middle
			end = middle - 1

			// 검색된 숫자가 찾는 숫자보다 클 때
			// 찾는 숫자보다 같거나 큰 숫자들의 위치를 검색하므로
			// 이 경우에도 answer에 위치를 저장한다.
		} else if numbers[middle] > searchNum {
			answer = middle
			end = middle - 1

			// 검색된 숫자가 찾는 숫자보다 작을 때
		} else {
			start = middle + 1
		}

	}

	return answer
}

func solution(info []string, query []string) []int {
	answer := []int{}
	groups := make(map[string][]int)

	for _, v := range info {
		spl := strings.Split(v, " ")

		// 다양한 조건을 만족하는 그룹을 만든다.
		langs := []string{spl[0], "-"}
		jobs := []string{spl[1], "-"}
		careers := []string{spl[2], "-"}
		souls := []string{spl[3], "-"}
		score, err := strconv.Atoi(spl[4])
		if err != nil {
			panic(err)
		}

		products := Iter(langs, jobs, careers, souls)
		for p := range products {
			group := strings.Join(p, " ")
			scoreList := groups[group]
			scoreList = append(scoreList, score)
			groups[group] = scoreList
		}
	}

	for _, v := range query {
		// 조건에 일치하는 정보 개수
		repl := strings.ReplaceAll(v, " and ", " ")
		spl := strings.Split(repl, " ")

		condition := strings.Join(spl[:len(spl)-1], " ")

		score, err := strconv.Atoi(spl[4])
		if err != nil {
			panic(err)
		}

		if _, ok := groups[condition]; !ok {
			answer = append(answer, 0)
			continue
		}

		infoScoreList := groups[condition]

		// 이진 탐색 전, 점수표 정렬
		sort.Ints(infoScoreList)

		// Binary search
		location := BinarySearch(infoScoreList, len(infoScoreList), score)

		answer = append(answer, len(infoScoreList)-location)
	}

	return answer
}

func main() {
	info := []string{
		"java backend junior pizza 150",
		"python frontend senior chicken 210",
		"python frontend senior chicken 150",
		"cpp backend senior pizza 260",
		"java backend junior chicken 80",
		"python backend senior chicken 50",
	}

	query := []string{
		"java and backend and junior and pizza 100",
		"python and frontend and senior and chicken 200",
		"cpp and - and senior and pizza 250",
		"- and backend and senior and - 150",
		"- and - and - and chicken 100",
		"- and - and - and - 150",
	}

	answer := solution(info, query)
	fmt.Println(answer)
}
