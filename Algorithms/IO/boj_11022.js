let readline = require("readline");

let r = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

r.on("line", (line) => {
    input.push(line);
}).on("close", () => {

    let unit = input[0];
    for (let i = 1; i <= unit; i++) {
        let numbers = input[i]
            .split(' ')
            .map((a) => {
                return a * 1
            });

        let result = `Case #${i}: ${numbers[0]} + ${numbers[1]} = ${numbers[0] + numbers[1]}`;
        console.log(result);
    }
    process.exit();
});