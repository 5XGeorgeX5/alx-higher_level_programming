#!/usr/bin/node
function fact (n) {
  let ans = 1;
  for (let i = 2; i <= n; i++) {
    ans *= i;
  }
  return ans;
}
console.log(fact(parseInt(process.argv[2])));
