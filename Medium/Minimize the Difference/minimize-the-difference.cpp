//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;


class Array
{
public:
    template <class T>
    static void input(vector<T> &A,int n)
    {
        for (int i = 0; i < n; i++)
        {
            scanf("%d ",&A[i]);
        }
    }

    template <class T>
    static void print(vector<T> &A)
    {
        for (int i = 0; i < A.size(); i++)
        {
            cout << A[i] << " ";
        }
        cout << endl;
    }
};


// } Driver Code Ends

#define ll long long

class Solution {
    public:
    int minimizeDifference(int n, int k, vector<int> &arr) {
       
       vector<ll> suf(n,0);
      
       // / -> min
       // % -> max
       ll MAX=1e9+3;
       
       //suffix
       suf[n-1]=(MAX*arr[n-1])+arr[n-1];
       for(int i=n-2;i>=0;i--)
       {
           ll back_min=suf[i+1]/MAX;
           ll back_max=suf[i+1]%MAX;
           
           ll mini;
           ll maxi;
           
           if(arr[i]<back_min)
           mini=arr[i];
           else
           mini=back_min;
           
           if(arr[i]>back_max)
           maxi=arr[i];
           else
           maxi=back_max;
           
           suf[i]=(MAX*mini)+maxi;
       }
       
       
      
       int pre_min=arr[0];
       int pre_max=arr[0];
       int i=0;
       int j=k-1;
       ll ans=suf[k]%MAX - suf[k]/MAX;
       while(j+2<n)
       {
           i++;
           j++;
           
           int maximum;
           int minimum;
           
           if(pre_max>(suf[j+1]%MAX))
           maximum=pre_max;
           else
           maximum=suf[j+1]%MAX;
           
           
           if(pre_min<(suf[j+1]/MAX))
           minimum=pre_min;
           else
           minimum=suf[j+1]/MAX;
           
           if((maximum-minimum)<ans)
           ans=maximum-minimum;
           
           if(arr[i]<pre_min)
           pre_min=arr[i];
           
           if(arr[i]>pre_max)
           pre_max=arr[i];
           
       }
       
       if((pre_max - pre_min)<ans)
       ans=pre_max-pre_min;
       
       return ans;
    }
};


//{ Driver Code Starts.

int main(){
    int t;
    scanf("%d ",&t);
    while(t--){
        
        int n;
        scanf("%d",&n);
        
        
        int k;
        scanf("%d",&k);
        
        
        vector<int> arr(n);
        Array::input(arr,n);
        
        Solution obj;
        int res = obj.minimizeDifference(n, k, arr);
        
        cout<<res<<endl;
        
    }
}

// } Driver Code Ends