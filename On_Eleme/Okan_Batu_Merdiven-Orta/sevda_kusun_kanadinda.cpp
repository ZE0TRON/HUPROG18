#include <bits/stdc++.h>
#include <dirent.h>
#include <string>
#include <vector>
#include <fstream>
#include <iostream>
#include <sstream>

using namespace std;
typedef long long ll;
ll sol(vector<ll>v)
{
    ll n = v.size();
    ll **dp;
    dp = new ll* [n];
    for (int i = 0; i<n;i++)
        dp[i]= new ll[n];

    ll  i, j, x, y, z;


    for (ll m = 0; m < n; ++m)
    {
        i = 0;
        j = m;
        while (j < n)
        {
            if((i+2) <= j)
                x = dp[i+2][j];
            else
                x = 0;
            if((i+1) <= (j-1))
                y = dp[i+1][j-1];
            else
                y = 0;
            if(i <= (j-2))
                z = dp[i][j-2];
            else
                z = 0;
            dp[i][j] = (max(v[i] + min(x, y), v[j] + min(y, z)));
            ++i;
            ++j;
        }
    }
    return dp[0][n-1];
}



int main()
{
    int n;
    cin>>n;
    ll* arr = new ll[n];
    for(int i=0;i<n;i++){
        cin>>*(arr+i);
    }
    vector<ll> v (arr,arr + 8*n / sizeof(ll));
    ll ans=sol(v);
    ll sum = accumulate(v.begin(),v.end(),0);
    if(ans > sum - ans) cout << ans << " Pro";
    else if(ans < sum - ans) cout<< ans << " Zone";
    else cout <<ans << " ProZone";

    return 0;
}