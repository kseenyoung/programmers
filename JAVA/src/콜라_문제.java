public class 콜라_문제 {

    class Solution {
        public int solution(int a, int b, int n) {
            int answer = 0, mod = 0;
            while(n >= a){
                answer += (n / a)*b;
                n = (n / a)*b + (n % a);
            }
            return answer;
        }
    }
}
