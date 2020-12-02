const readline = require("readline");
const r = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let n;
let A;
let B;

r.on("line", (line) => {
    if (!n) {
        n = parseInt(line);
    } else if (!A) {
        A = line.split(' ').map((e) => { return e * 1 });
        A.sort((a, b) => { return b - a });
    } else if (!B) {
        B = line.split(' ').map((e) => { return e * 1 });
        B.sort((a, b) => { return a - b });
    }
}).on("close", () => {
    let result = 0;
    for (let i = 0; i < n; i++) {
        result += A[i] * B[i]
    }
    console.log(result);

    process.exit();
});
