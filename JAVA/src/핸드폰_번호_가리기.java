public class 핸드폰_번호_가리기 {
    class Solution {
        public String solution(String phone_number) {
            String answer = "";
            int plen = phone_number.length();
            for(int i=0; i<plen-4; i++){
                answer += "*";
            }
            return answer + phone_number.substring(plen-4, plen);
        }
    }

}
