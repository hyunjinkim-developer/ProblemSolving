/* https://school.programmers.co.kr/learn/courses/30/lessons/12922?language=javascript */
function solution(n) {
  var answer = "";
  let answerArr = [];
  for (let i = 0; i < n; ++i) {
    if (i % 2 == 0) {
      answerArr.push("수");
    } else {
      answerArr.push("박");
    }
  }
  answer = answerArr.join("");

  return answer;
}

