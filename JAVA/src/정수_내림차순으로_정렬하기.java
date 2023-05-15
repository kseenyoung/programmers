import java.util.*;
public class 정수_내림차순으로_정렬하기 {
    class Solution {
        public long solution(long n) {
            String[] str = String.valueOf(n).split("");
            Arrays.sort(str);
            StringBuilder sb = new StringBuilder();
            for (String s: str) sb.append(s);
            return Long.parseLong(sb.reverse().toString());
        }
    }
}
