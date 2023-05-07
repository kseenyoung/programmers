public class 공원_산책 {

    class Solution {
        public int[] solution(String[] park, String[] routes) {
            int[] answer = {};
            int[] pos = {0,0};
            String s = "S";
            String[][] map = new String[park.length][park[0].length()];

            int[] dr = {-1, 1, 0, 0}; // N, S, W, E
            int[] dc = {0, 0, -1, 1};

            for(int i=0; i<park.length; i++){
                String[] subMap = park[i].split("");
                for(int j=0; j<park[0].length(); j++){
                    if (park[i].charAt(j) == 'S'){
                        pos[0] = i;
                        pos[1] = j;
                    }
                    map[i][j] = subMap[j];
                }
            }
            for(String route: routes){
                String[] r = route.split(" ");
                String dir = r[0];
                int mov = Integer.parseInt(r[1]);
                int idx = dir.equals("E") ? 3 : dir.equals("S") ? 1 : dir.equals("W") ? 2 : 0;
                boolean flag = false;
                int row=pos[0], col=pos[1];

                for(int i=1; i<=mov; i++){
                    row += dr[idx];
                    col += dc[idx];
                    // System.out.println(row + " " + col);
                    if (0 > row | row >= park.length | 0 > col & col >= park[0].length() | map[row][col].equals("X")){
                        // System.out.println(row + " " + col);
                        flag = true;
                        break;
                    }
                }
                if(!flag){
                    pos[0] = row;
                    pos[1] = col;
                }

            }

            return pos;
        }
    }
}
