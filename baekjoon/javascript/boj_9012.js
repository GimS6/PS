// 괄호
function isVPS(ps) {
    let stack = [];
    for (let i = 0; i < ps.length; i++) {
        let a = ps[i];
        if (a == '(') {
            stack.push(a);
        } else if (a == ')') {
            if (stack.length == 0) { return "NO" }
            stack.pop();
        }
    }

    if (stack.length != 0) {
        return "NO"
    }
    return "YES"
}

const readline = require("readline");
const r = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let n;
let result = [];

r.on("line", (line) => {
    if (!n) {
        n = parseInt(line);
    } else {
        result.push(isVPS(line));
    }
}).on("close", () => {
    console.log(result.join('\n'));
    process.exit();
})