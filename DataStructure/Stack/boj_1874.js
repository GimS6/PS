// 스택 수열
const readline = require("readline");
const r = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let n;
let nums = [];

r.on("line", (line) => {
    if (!n) {
        n = parseInt(line);
    } else {
        nums.push(parseInt(line));
    }
}).on("close", () => {
    let stack = [];
    let result = [];
    let idx = 1;

    for (let i = 0; i < n; i = i) {
        num = nums[i];
        if (idx <= num) {
            stack.push(idx);
            result.push("+");
            idx++;
        } else if (stack[stack.length - 1] == num) {
            stack.pop()
            result.push("-");
            i++;
        } else {
            break;
        }
    }

    console.log(stack.length == 0 ? result.join("\n") : "NO")
    process.exit();
});