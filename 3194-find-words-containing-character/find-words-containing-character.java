class Solution {
    public List<Integer> findWordsContaining(String[] words, char x) {
        List<Integer> result=new ArrayList<>();
        for(int i=0;i<words.length;i++){
            String word=words[i]; //spliiting into each word from array
            for(int j=0;j<word.length();j++){
                if(word.charAt(j)==x){
                    result.add(i);
                    break; //avoiding duplicate add
                }
            }
        }
        return result;
    }
}