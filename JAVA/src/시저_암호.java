public class 시저_암호 {

    class Solution {
        public String solution(String s, int n) {
            char[] chs = s.toCharArray();
            String answer = "";

            for(int i=0; i<chs.length; i++){
                if(Character.isAlphabetic(chs[i])){
                    int temp = Character.isLowerCase(chs[i]) ? (chs[i] - 'a' + n) % 26 + 'a' : (chs[i] - 'A' + n) % 26 + 'A';
                    answer += (char)temp;
                }
                else
                    answer += chs[i];
            }

            return answer;
        }
    }
}
