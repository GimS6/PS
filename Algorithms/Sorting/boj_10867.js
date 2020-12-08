// 중복 빼고 정렬하기
const readline = require("readline");
const r = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let n;
let l;

r.on("line", (line) => {
    if (!n) {
        n = parseInt(line);
    } else {
        l = new Set(line.split(" ").map((a) => { return a * 1 }));
    }
}).on("close", () => {
    let result = Array.from(l).
        sort((a, b) => { return a - b; }).
        map((a) => { return a + ""; });

    console.log(result.join(" "));
    process.exit();
});