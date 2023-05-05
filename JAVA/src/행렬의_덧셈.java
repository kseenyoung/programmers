public class 행렬의_덧셈 {
    class Solution { // 내 풀이
        public int[][] solution(int[][] arr1, int[][] arr2) {
            int[][] answer = new int[arr1.length][arr1[0].length];
            for(int i=0; i<arr1.length; i++)
                for(int j=0; j<arr1[0].length; j++)
                    answer[i][j] = arr1[i][j] + arr2[i][j];

            return answer;
        }
    }

    class Solution1 {  // 참고(arr1을 정답 배열로 대치)
        public int[][] solution(int[][] arr1, int[][] arr2) {
            int[][] answer = arr1;
            for(int i=0; i<arr1.length; i++)
                for(int j=0; j<arr1[0].length; j++)
                    answer[i][j] += arr2[i][j];

            return answer;
        }
    }
}
