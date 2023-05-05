public class 푸드파이트_대회 {

    class Solution {  // 내 풀이
        public String solution(int[] food) {
            StringBuilder answer = new StringBuilder();
            for(int i=1; i<food.length; i++){
                for(int j=0; j<food[i]/2; j++){
                    answer.append(Integer.toString(i));
                }
            }

            String result = answer + "0";
            result += answer.reverse().toString();
            return result;
        }
    }


}
