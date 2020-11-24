let readline = require("readline");

let r = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

r.on("line", (line) => {
    input.push(line);
}).on("close", () => {
    let n = parseInt(input[0]);

    for (let i = 1; i <= n; i++) {
        let result = " ".repeat(n - i);

        if (i == 1) {
            result += "*";
        } else if (i == n) {
            result += "*".repeat(n * 2 - 1);
        } else {
            result += "*" + " ".repeat(i * 2 - 3) + "*";
        }

        console.log(result);
    }

    process.exit(0);
});