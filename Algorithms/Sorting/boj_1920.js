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
    let nNums = input[1].split(" ").map((a) => { return a * 1 });
    
    let map = new Map();
    for (let i = 0; i < n; i++) {
        let number = nNums[i];
        map.set(number, 0);
    }

    let m = parseInt(input[2]);
    let mNums = input[3].split(" ").map((a) => { return a * 1 });

    for (let i = 0; i < m; i++) {
        let number = mNums[i]
        let exist = 0;

        if (map.has(number)) {
            exist = 1;
        }
        console.log(exist);
    }

    process.exit();
});