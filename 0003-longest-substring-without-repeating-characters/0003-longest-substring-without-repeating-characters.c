#include<string.h>
int lengthOfLongestSubstring(char* s) {
    int count[128]={0};
    int i=0,j;
    int maxlength=0;
    int currentlength=0;
    int n=strlen(s);
    for (j=0;j<n;j++){
        while(count[s[j]]>0){
            count[s[i]]-=1;
            i+=1;
        }
        count[s[j]]+=1;
        currentlength=j-i+1;
        if (currentlength>maxlength){
            maxlength=currentlength;
        }
    }
    return maxlength;

}