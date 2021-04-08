// 숫자 카드 2
const readline = require("readline");
const r = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let max = 10000000;
let n;
let cards;
let m;
let checks;

r.on("line", (line) => {
    if (!n) {
        n = parseInt(line);
    } else if (!cards) {
        cards = new Int32Array(20000001);
        let c = line.split(" ").map((a) => { return a * 1; });
        for (i = 0; i < n; i++) {
            cards[max + c[i]]++;
        }
    } else if (!m) {
        m = parseInt(line);
    } else if (!checks) {
        checks = line.split(" ").map((a) => { return a * 1 });
    }
}).on("close", () => {
    let result = [];
    for (let i = 0; i < m; i++) {
        result.push(cards[max + checks[i]] + "");
    }

    console.log(result.join(" "));
    process.exit();
});