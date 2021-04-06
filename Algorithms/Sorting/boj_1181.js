const readline = require("readline");
const r = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let n;
let text = [];

r.on("line", (line) => {
    if(!n) {
        n = parseInt(line);
    } else {
        text.push(line);
    }
}).on("close", () => {
    let mapped = text.map((el, i) => {
        return { index: i, value: el, len: el.length };
    });

    mapped.sort((a, b) => {
        return +(a.value > b.value) || +(a.value === b.value) -1;
    });

    mapped.sort((a, b) => {
        return +(a.len > b.len) || +(a.len === b.len) -1;
    });

    let result = new Set(mapped.map((el) => {
        return text[el.index];
    }));

    console.log(Array.from(result).join("\n"));

    process.exit();
})