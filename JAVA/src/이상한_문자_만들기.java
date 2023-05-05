public class 이상한_문자_만들기 {

    class Solution { // 내 풀이
        public String solution(String s) {
            s = s.toLowerCase();
            char[] ch = s.toCharArray();
            StringBuilder answer = new StringBuilder();
            Boolean flag = Character.isLowerCase(ch[0]);
            int j = 0;

            for(int i=0; i<ch.length; i++){
                if (!flag & Character.isLowerCase(ch[i])){
                    j = 1;
                    answer.append(Character.toUpperCase(ch[i]));
                    flag = true;
                }
                else{
                    if(Character.isLowerCase(ch[i]) & j % 2 == 0)
                        answer.append(Character.toUpperCase(ch[i]));
                    else
                        answer.append(ch[i]);
                    j++;
                    flag = Character.isLowerCase(ch[i]);
                }


            }
            return answer.toString();
        }
    }

    class Solution1 { // 참고
        public String solution(String s) {
            String[] str = s.split("");
            int cnt = 0;
            String answer = "";

            for(String ss : str){
                cnt = ss.contains(" ") ? 0 : cnt + 1; // 공백이면 리셋
                answer += cnt % 2 == 0 ? ss.toLowerCase() : ss.toUpperCase();  // 공백 다음부터는 대소문자 번갈아 실행
            }
            return answer;
        }
    }
}
