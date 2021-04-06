// 1, 2, 3 더하기
let result = [];
let ways = 0;
let T;
let n;

function dfs(num) {
    if (num == n) {
        ways++;
        return
    }
    if (num > n) {
        return 
    }

    dfs(num + 1)
    dfs(num + 2)
    dfs(num + 3)
}

const readline = require("readline");
const r = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

r.on("line", (line) => {
    if (!T) {
        T = parseInt(line);
    } else {
        n = parseInt(line);
        for(let i = 1; i <= 3; i++) {
            dfs(i)
        }
        result.push(ways);
        ways = 0;
    }
}).on("close", () => {
    console.log(result.join("\n"));
    process.exit();
});
