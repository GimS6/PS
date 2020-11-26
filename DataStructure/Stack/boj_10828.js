const readline = require("readline");
const r = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let n;
let s = [];
let result = [];

r.on("line", (line) => {
    if (!n) {
        n = parseInt(line);
    } else if (line.startsWith("push")) {
        s.push(line.split(' ')[1]);
    } else if (line.startsWith("pop")) {
        result.push((s.length != 0 ? s.pop() + "" : "-1"));
    } else if (line.startsWith("size")) {
        result.push(s.length + "");
    } else if (line.startsWith("empty")) {
        result.push((s.length == 0 ? "1" : "0"))
    } else {
        result.push((s.length != 0 ? s[s.length - 1] + "" : "-1") + "");
    }
}).on("close", () => {
    console.log(result.join("\n"));
    process.exit();
});

