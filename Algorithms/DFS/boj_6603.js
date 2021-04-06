// 로또
const max = 13;
let S = new Array(max).fill(0);
let lotto = new Array(max).fill(0);
let k;
let subresult = [];
let result = [];

function dfs(start, depth) {
    if (depth == 6) {
        subresult.push(lotto.slice(0, 6).join(" "))
        return
    }

    for (let i = start; i < k; i++) {
        lotto[depth] = S[i];
        dfs(i + 1, depth + 1);
    }
}

const readline = require("readline");
const r = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

r.on("line", (line) => {
    k = line.split(" ")[0]
    if (k == 0) {
        console.log(result.join("\n\n"))
        process.exit();
    }
    S = line.split(" ").slice(1);

    dfs(0, 0);
    result.push(subresult.join("\n"));
    subresult = [];
});