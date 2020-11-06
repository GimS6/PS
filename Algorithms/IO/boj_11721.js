let readline = require('readline');

let r = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

r.on("line", (line) => {
    input.push(line);
}).on("close", () => {
    let str = input[0];
    let length = str.length;
    let count = 0;

    let result = '';

    for (let i = 0; i < length; i++) {
        if (count == 10) {
            count = 0;
            console.log(result);
            result = ''
        }

        result += str.charAt(i);
        count++;
    }

    if (result != '') {
        console.log(result);
    }

    process.exit();
});