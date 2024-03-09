//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
//User function template for C++

class Solution{
  public:
    char nthCharacter(string s, int r, int n) {
        string st = "";
        int len = s.length();
        if(len % 2 == 0) len = len/2;
        else len = len/2 + 1;
        
        while(r != 0){
            for(int i = 0; i < len; i++){
                if(s[i] == '1'){
                    st += "10";
                }
                else{
                    st += "01";
                }
            }
            s = st;
            st = "";
            r--;
        }
        
        return s[n];
    }
};

//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int R, N;
        string S;
        cin >> S >> R >> N;
        Solution ob;
        cout << ob.nthCharacter(S, R, N) << endl;
    }
    return 0;
}
// } Driver Code Ends