const readline = require("readline");
const r = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let n;
let q = [];
let result = "";

r.on("line", (line) => {
    if (!n) {
        n = parseInt(line);
    } else if (line.startsWith("push")) {
        q.push(parseInt(line.split(' ')[1]));
    } else if (line.startsWith("pop")) {
        result += (q.length != 0 ? q.shift() : -1) + "\n";
    } else if (line.startsWith("size")) {
        result += q.length + "\n";
    } else if (line.startsWith("empty")) {
        result += (q.length == 0 ? 1 : 0) + "\n";
    } else if (line.startsWith("front")) {
        result += (q.length != 0 ? q[0] : -1) + "\n";
    } else if (line.startsWith("back")) {
        result += (q.length != 0 ? q[q.length - 1] : -1) + "\n";
    }
}).on("close", () => {
    console.log(result);
    process.exit();
});