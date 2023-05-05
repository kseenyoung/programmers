public class 최소_직사각형 {

    class Solution {
        public int solution(int[][] sizes) {
            int answer = 0;
            int maxC=0, maxR=0;
            for(int i=0; i<sizes.length; i++){
                if(sizes[i][1] < sizes[i][0]){
                    int temp = sizes[i][0];
                    sizes[i][0] = sizes[i][1];
                    sizes[i][1] = temp;
                }
                maxC = maxC < sizes[i][0] ? sizes[i][0] : maxC;
                maxR = maxR < sizes[i][1] ? sizes[i][1] : maxR;
            }
            System.out.printf("%d %d", maxC, maxR);
            return maxC*maxR;
        }
    }
}
