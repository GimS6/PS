let readline = require("readline");

let r = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

r.on("line", (line) => {
    input.push(line);
}).on("close", () => {
    let length = input.length;
    for (let i = 0; i < length; i++) {
        let numbers = input[i]
            .split(' ')
            .map((a) => {
                return a * 1;
            });
        if (numbers[0] == 0 && numbers[1] == 0) {
            return
        }
        console.log(numbers[0] + numbers[1]);
    }
    process.exit();
});