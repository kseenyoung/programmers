    import java.lang.Math;
public class 부족한_금액_계산하기 {
    class Solution {
        public long solution(int price, int money, int count) {
            long p=0;
            for (int i=1; i<=count; i++){
                p += i*price;
            }
            return money >= p ? 0 : p - money;  // 돈이 부족하지 않은 경우 money - p가 아닌 0
        }
    }
}
