    import java.util.*;
public class 두_개_뽑아서_더하기 {

    class Solution {  // 55.6% -> 100%
        public int[] solution(int[] numbers) {
            HashSet<Integer> hash = new HashSet<>();
            for(int i=0; i<numbers.length-1; i++){
                for(int j=i+1; j<numbers.length; j++){
                    hash.add(numbers[i]+numbers[j]);
                }
            }

            int[] answer = new int[hash.size()];
            Iterator iter = hash.iterator();
            int i = 0;
            while(iter.hasNext())
                answer[i++] = (int)iter.next();
            Arrays.sort(answer);  // add
            return answer;

//            return hash.stream().sorted().mapToInt(i -> i).toArray();  // Stream 사용
        }
    }


}
