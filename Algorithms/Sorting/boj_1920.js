const readline = require("readline");
function binarySearch(l, target) {
    let left = 0;
    let right = l.length - 1;

    let result = -1

    while (left <= right) {
        let mid = Math.floor((left + right) / 2);
        if (l[mid] > target) {
            right = mid - 1;
        } else if (l[mid] < target) {
            left = mid + 1;
        } else {
            result = mid;
            break;
        }
    }

    return result == -1 ? 0 : 1
}

const r = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];
let result = [];

r.on("line", (line) => {
    input.push(line);
}).on("close", () => {
    let n = parseInt(input[0]);
    let nNum = input[1].split(" ").map((a) => { return a * 1 }).sort((a, b) => { return a - b });

    let m = parseInt(input[2]);
    let mNum = input[3].split(" ").map((a) => { return a * 1 });

    for (let i = 0; i < m; i++) {
        result.push(binarySearch(nNum, mNum[i]));
    }

    console.log(result.join("\n"));
 
    process.exit();
});