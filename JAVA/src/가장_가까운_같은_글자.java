public class 가장_가까운_같은_글자 {

    class Solution {
        public int[] solution(String s) {

            String[] arr = s.split("");
            int[] answer = new int[s.length()];
            for(int i=0; i<s.length(); i++){
                for(int j=i-1; j>-1; j--){
                    if(arr[i].equals(arr[j])){
                        answer[i] = i - j;
                        break;
                    }
                }
                answer[i] = answer[i] == 0 ? -1 : answer[i];
            }
            return answer;
        }
    }
}
