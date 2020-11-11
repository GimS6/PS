const { stdin } = require("process");
let readline = require("readline");

let r = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

r.on("line", (line) => {
    input.push(line);
}).on("close", () => {
    let n = input[0];

    for (let i = 0; i < n; i++) {
        let result = "";

        for (let j = n; j > i; j--) {
            result += "*";
        }

        for (let k = 0; k < i; k++) {
            result += "";
        }

        console.log(result);
    }

    process.exit();
})