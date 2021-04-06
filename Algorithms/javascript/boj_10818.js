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

    let numbers = input[1]
    .split(" ")
    .map((a) => {
        return a*1
    });

    let max = numbers[0];
    let min = numbers[0];
    for (let i = 0; i < n; i++) {
        if (max < numbers[i]) {
            max = numbers[i];
        }

        if (min > numbers[i]) {
            min = numbers[i];
        }
    }
    
    console.log(min + " " + max);

    process.exit();
})