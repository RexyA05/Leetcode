#include<string.h>
int numberOfSubstrings(char* s) {
    int n=strlen(s);
    int i=0;
    int j=0;
    int answer=0;
    int count[3] = {0,0,0};
    for (j=0;j<n;j++){
        if (s[j]=='a'){
            count[0]+=1;
        }
        else if(s[j]=='b'){
            count[1]+=1;
        }
        else{
            count[2]+=1;
        }
        while(count[0]>0 && count[1]>0 && count[2]>0){
            answer+=(n-j);
            if (s[i]=='a'){
                count[0]-=1;
        }
            else if(s[i]=='b'){
                count[1]-=1;
        }
            else{
                count[2]-=1;
        } 
        i+=1;

        }
    }
    return answer;
}