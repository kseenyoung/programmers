public class 크기가_직은_부분_문자열 {

    class Solution {
        public int solution(String t, String p) {
            int answer = 0;
            long parseP = Long.parseLong(p);  //Long 주의

            for(int i=0; i<t.length()-p.length()+1; i++){
                long parseSub = Long.parseLong(t.substring(i,i+p.length()));
                if(parseSub <= parseP)
                    answer++;
            }
            return answer;
        }
    }
}
