public class 자연수_뒤집어_배열로_만들기 {

    class Solution { // my solution
        public int[] solution(long n) {
            String s = Long.toString(n);
            int[] answer = new int[s.length()];
            for(int i=0; i<s.length(); i++){
                answer[i] = (int)(n % 10);
                n /= 10;
            }
            return answer;
        }
    }

    class Solution1 {  // 참고
        public String solution(String phone_number) {
            char[] number = phone_number.toCharArray();
            int plen = phone_number.length();
            for(int i=0; i<plen-4; i++){
                number[i] = '*';
            }
            return String.valueOf(number);
        }
    }

}
