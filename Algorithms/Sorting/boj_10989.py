# 문제: https://www.acmicpc.net/problem/10989
# 소스코드: https://www.acmicpc.net/source/24033050
import sys

n = int(sys.stdin.readline().rstrip())
l = [0] * 10001

for i in range (1, n+1):
    number = int(sys.stdin.readline().rstrip())
    l[number] += 1

for i in range(1, 10001):
    for _ in range(l[i]):
        sys.stdout.write(str(i) + "\n")

# node.js로는 위와 같이 해도 메모리 부족 에러를 뚫지 못한다.
# 코드:
#
# const readline = require("readline");
# const r = readline.createInterface({
#    input: process.stdin,
#    output: process.stdout
# });
#
# let n = 0;
# let cnt = 0;
# let numbers = new Uint32Array(10001);
# 
# r.on("line", (line) => {
#     if (cnt == 0) {
#         n = parseInt(line);
#         cnt++;
#     } else {
#         if (cnt > n) {
#             r.close();
#         }  
#         numbers[parseInt(line)]++;
#         cnt++;
#     }
# }).on("close", () => {
#     for (let i = 1; i < 10001; i++) {
#         for (let j = 0; j < numbers[i]; j++) {
#             console.log(i);
#         }
#     }
#     process.exit();
# });