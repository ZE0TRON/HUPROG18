#include <bits/stdc++.h>
#include <dirent.h>
#include <string>
#include <vector>
#include <fstream>
#include <iostream>
#include <sstream>

#define SSTR( x ) static_cast< std::ostringstream & >( \( std::ostringstream() << std::dec << x ) ).str()

using namespace std;
typedef long long ll;
ll sol(vector<ll>v)
{
    ll n = v.size();
    cout<<"nn "<<n<<endl;
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
            dp[i][j] = (max(v[i] + min(x, y), v[j] + min(y, z)))%1000000007;
            ++i;
            ++j;
        }
    }
    return dp[0][n-1];
}




vector<string> GetDirectoryFiles(const string& dir) {
    vector<string> files;
    shared_ptr<DIR> directory_ptr(opendir(dir.c_str()), [](DIR* dir){ dir && closedir(dir); });
    struct dirent *dirent_ptr;
    if (!directory_ptr) {
        cout << "Error opening : " << strerror(errno) << dir << endl;
        return files;
    }
    int i=0;
    while ((dirent_ptr = readdir(directory_ptr.get())) != nullptr) {
        if(i++>1)
            files.push_back(string(dirent_ptr->d_name));
    }
    return files;
}


int main()
{
    string n;
    string path;
    const auto& directory_path = string("..\\input");
    const auto& files = GetDirectoryFiles(directory_path);
    ifstream inputfile;
    ofstream outputfile;
    int k=0;
    for (const auto& file : files) {
        //cout << file << endl;
        path="..\\input\\";
        path.append(file.data());
        inputfile.open(path);
        inputfile>>n;
        int temp=atoi(n.c_str());
        //cout<<"nn "<<temp <<endl;
        ll* arr = new ll[temp];
        for(int i=0;i<temp;i++){
            inputfile>>*(arr+i);
            //cout<<i<<"  "<<arr[i]<<endl;
        }
        path="..\\output\\output";
        if(k<10) path.append("0");
        char buf[100];
        itoa(k++,buf,10);
        path.append(buf);
        path.append(".txt");
        outputfile.open(path);
        vector<ll> v (arr,arr + 8*temp / sizeof(ll));
        ll ans=sol(v);
        cout<<ans<<endl;
        ll sum = accumulate(v.begin(),v.end(),0);
        if(ans > sum - ans) outputfile << ans << " Pro";
        else if(ans < sum - ans) outputfile<< ans << " Zone";
        else outputfile <<ans << " ProZone";
        inputfile.close();
        outputfile.close();
    }
    return 0;
}
