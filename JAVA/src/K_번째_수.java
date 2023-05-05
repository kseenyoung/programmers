    import java.util.*;
public class K_번째_수 {

    class Solution {  // 71.4%
        public int[] solution(int[] array, int[][] commands) {
            String[] arr = new String[array.length];
            int[] answer = new int[commands.length];
            for(int i=0; i<array.length; i++){
                arr[i] = Integer.toString(array[i]);
            }
            String str = String.join("", arr);
            for(int a=0; a<commands.length; a++){
                int i=commands[a][0], j=commands[a][1], k=commands[a][2];
                String[] arr2 = str.substring(i-1, j).split("");
                Arrays.sort(arr2);
                answer[a] = Integer.parseInt(arr2[k-1]);
            }
            return answer;
        }
    }

    class Solution1 { // 참고
        public int[] solution(int[] array, int[][] commands) {
            int[] answer = new int[commands.length];
            int a=0;
            for(int[] com: commands){
                int i = com[0], j = com[1], k = com[2];
                int[] strs = Arrays.copyOfRange(array, i-1, j);
                Arrays.sort(strs);
                answer[a++] = strs[k-1];
            }
            return answer;
        }
    }
}
