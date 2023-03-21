/* https://school.programmers.co.kr/learn/courses/30/lessons/12931?language=javascript */
function solution(n) {
  var answer = 0;
  for (let i = 1; i <= 9; ++i) {
    let curDigit = (n % 10 ** i) / 10 ** (i - 1);
    answer += curDigit;

    n -= curDigit * 10 ** (i - 1);
    if (n === 0) {
      break;
    }
  }
  return answer;
}

