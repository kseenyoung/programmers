public class _1차_비밀지도 {

    class Solution {  //내 풀이
        public String[] solution(int n, int[] arr1, int[] arr2) {
            String[] answer = new String[n];
            for(int i=0; i<arr1.length; i++){
                String temp = "";
                StringBuilder sb1 = new StringBuilder();
                while(arr1[i] > 0)
                {
                    sb1.append(arr1[i] % 2);
                    arr1[i] /= 2;
                }
                String[] s1 = (count0(n-sb1.length()) + sb1.reverse()).split("");
                StringBuilder sb2 = new StringBuilder();
                while(arr2[i] > 0)
                {
                    sb2.append(arr2[i] % 2);
                    arr2[i] /= 2;
                }
                String[] s2 = (count0(n-sb2.length()) + sb2.reverse()).split("");

                for(int j=0; j<n; j++){
                    // System.out.println(s1[j] + " " + s2[j]);
                    if(s1[j].equals("1") | s2[j].equals("1"))
                        temp += "#";
                    else
                        temp += " ";
                }
                answer[i] = temp;
            }
            return answer;
        }
        public String count0(int cnt){
            String answer = "";
            for(int i=0; i<cnt; i++)
                answer += "0";
            return answer;
        }
    }

    class Solution1 { // 참고
        public String[] solution(int n, int[] arr1, int[] arr2) {
            String[] answer = new String[n];
            for(int i=0; i<arr1.length; i++){
                answer[i] = Integer.toBinaryString(arr1[i] | arr2[i]); // 큰 값을
            }
            for(int i=0; i<arr1.length; i++){
                answer[i] = String.format("%" + n + "s", answer[i]);
                answer[i] = answer[i].replaceAll("1", "#");
                answer[i] = answer[i].replaceAll("0", " ");
            }
            return answer;
        }
    }
}
