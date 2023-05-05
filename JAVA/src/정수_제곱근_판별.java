public class 정수_제곱근_판별 {

    class Solution { // 82%
        public long solution(long n) {
            double sqrt = Math.sqrt(n);
            if( Math.pow(sqrt, 2) == n)
                return (long)Math.pow(sqrt + 1, 2);
            else return -1;
        }
    }

    class Solution1 { // 100%(참고)
        public long solution(long n) {
            double sqrt = Math.ceil(Math.sqrt(n));
            if( Math.pow(sqrt, 2) == n)
                return (long)Math.pow(sqrt + 1, 2);
            else return -1;
        }
    }


}
