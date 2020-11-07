let readline = require("readline");

let r = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

let input = [];

r.on("line", (line) => {
    input.push(line);
}).on("close", () => {
    let n = input[0];
    let str = []

    for (let i = 1; i <= 9; i++) {
        str.push(`${n} * ${i} = ${n*i}`)
    }

    console.log(str.join("\n"));

    process.exit();
})