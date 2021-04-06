// 스택 수열
const readline = require("readline");
const r = readline.createInterface({
    input: process.stdin,
    ouput: process.stdout
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
    let pointer = 1;

    for (let i = 0; i < n; i = i) {
        if (pointer <= nums[i]) {
            stack.push(pointer);
            result.push("+");
            pointer++;
        } else if (stack[stack.length - 1] == nums[i]) {
            stack.pop();
            result.push("-");
            i++;
        } else {
            break;
        }
    }

    console.log(stack.length == 0 ? result.join("\n") : "NO");
    process.exit();
});