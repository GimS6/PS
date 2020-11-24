// 문제: https://www.acmicpc.net/problem/2751
// 소스코드: https://www.acmicpc.net/source/24022617
const readline = require("readline");

const r = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

r.on("line", (line) => {
    input.push(line);
}).on("close", () => {
    const n = parseInt(input[0]);
    let numbers = [];

    for (let i = 1; i <= n; i++) {
        numbers.push(parseInt(input[i]));
    }

    let mapped = numbers.map((el, i) => {
        return { index: i, value: el };
    });

    mapped.sort((a, b) => { return a - b });

    let result = mapped.map((el) => { return numbers[el.index] + "" }).join("\n");
    console.log(result);

    process.exit();
});

// 정렬한 배열을 for문으로 출력하는 건 효율성 테스트를 통과하지 못한다.
// 미리 배열을 '\n'으로 join 해 놓아야 그나마 성능이 나온다.

// input: 
// 5
// 5
// 4
// 3
// 2

// output:
// 1
// 1
// 2
// 3
// 4
// 5