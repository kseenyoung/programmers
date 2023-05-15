    import java.lang.Math;
public class _3진법_뒤집기 {

    class Solution { // 60%(런타임에러)
        public int solution(int n) {
            int answer = 0;
            StringBuilder sb = new StringBuilder();
            while (n>0){
                sb.append(n%3);
                n/=3;
            }

            int zin3 = Integer.parseInt(sb.toString()), j=0;
            System.out.print(zin3);
            while(zin3 > 0){
                answer += (zin3 %10)*(Math.pow(3, j));
                zin3 /= 10;
                j++;
            }
            return answer;
        }

        class Solution1 { // 참고
            public int solution(int n) {
                long answer = 0;
                StringBuilder sb = new StringBuilder();
                while (n>0){
                    sb.append(n%3);
                    n/=3;
                }

                return Integer.parseInt(sb.toString(), 3); // 문자열과 숫자 입력시 해당하는 진수로 파싱
            }
        }
    }
}
