    import java.util.*;
public class 문자열_내_마음대로_정렬하기 {

    class Solution {
        public String[] solution(String[] strings, int n) {
            ArrayList<String> answer = new ArrayList<>();
            for(int i=0; i<strings.length; i++){
                answer.add("" + strings[i].charAt(n) + strings[i]);
            }
            Collections.sort(answer);
            String[] result = new String[strings.length];
            for(int i=0; i<strings.length; i++){
                result[i] = answer.get(i).substring(1, answer.get(i).length());
            }
            return result;
        }
    }
}
