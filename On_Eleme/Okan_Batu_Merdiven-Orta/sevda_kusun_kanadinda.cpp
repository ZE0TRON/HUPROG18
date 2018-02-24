#include <bits/stdc++.h>

typedef long long ll;

using namespace std;


ll sol(vector<ll>v)
{
	ll n = v.size();
    ll dp[n][n], gap, i, j, x, y, z;
 
 
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
            dp[i][j] = max(v[i] + min(x, y), v[j] + min(y, z));
            ++i;
            ++j;
        }
    }
 
    return dp[0][n-1];
}
 
int main()
{
    ll arr[] = {5,6,47,1,3,2};
    vector<ll> v (arr,arr + sizeof(arr) / sizeof(ll));
    ll ans = sol(v);
    ll sum = accumulate(v.begin(),v.end(),0);
 	if(ans > sum - ans) cout << "Pro";
 	else if(ans < sum - ans) cout << "Zone";
 	else cout << "GG";
    return 0;
}
