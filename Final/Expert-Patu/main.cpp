#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<ctime>
#include<cmath>
#include<iostream>
#include<sstream>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<bitset>
#include<string>
#include<queue>
#include<iomanip>
#include<limits>
#include<typeinfo>
#include<functional>
#include<numeric>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef double ld;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef pair<ld,ld> pdd;

#define X first
#define Y second

const int MaxN=300010;

int n;

struct point
{
    int x,y;
    point () {}
    point (int a,int b)
    {
        x=a;
        y=b;
    }
    bool operator < (point A) const
    {
        return x<A.x||x==A.x&&y<A.y;
    }
    point operator - (point A)
    {
        return point(x-A.x,y-A.y);
    }
};

map<point,int> s;
map<int,map<point,int> > g;

int m;

struct line
{
    point a,b,v;
    int from,id;
    line () {}
    line (point x,point y,int k=-1,int r=-1)
    {
        a=x;
        b=y;
        if (b<a) swap(a,b);
        v=b-a;
        from=k;
        id=r;
    }
    ld get(ld X0)
    {
        return a.y+(X0-a.x)*v.y/v.x;
    }
};

vector<line> w;

set<int> event;
map<int,vector<int> > inp,oup;

ld X0;

inline bool cmp(int i,int j)
{
    return w[i].get(X0)<w[j].get(X0);
}

inline int random(int x)
{
    return (rand()<<15|rand())%x;
}

struct node
{
    node *Lc,*Rc;
    int id;
    int size;
    node ();
    node (int);
    node (int,node*,node*);
    node (node*);
};

typedef pair<node*,node*> pnn;

node *nil;

inline node::node()
{
    Lc=Rc=nil;
    id=-1;
    size=1;
}

inline node::node (int p)
{
    Lc=Rc=nil;
    id=p;
    size=1;
}

inline node::node (int p,node *L,node *R)
{
    Lc=L;
    Rc=R;
    id=p;
    size=L->size+R->size+1;
}

inline node::node (node *p)
{
    *this=*p;
}

node *merge(node *a,node *b)
{
    if (a==nil&&b==nil) return nil;
    if (a==nil) return new node(b);
    if (b==nil) return new node(a);
    if (random(a->size+b->size)<a->size)
        return new node(a->id,a->Lc,merge(a->Rc,b));
    else
        return new node(b->id,merge(a,b->Lc),b->Rc);
}

pnn split(node *a,int n)
{
    if (a==nil) return pnn(nil,nil);
    if (!n) return pnn(nil,new node(a));
    int cnt=a->Lc->size;
    if (cnt>=n)
    {
        pnn p=split(a->Lc,n);
        return pnn(p.X,new node(a->id,p.Y,a->Rc));
    }
    else
    {
        pnn p=split(a->Rc,n-cnt-1);
        return pnn(new node(a->id,a->Lc,p.X),p.Y);
    }
}

node *ins(node *r,int p)
{
    node *x=r;
    int cnt=0;
    while (x!=nil)
    {
        if (cmp(x->id,p))
        {
            cnt+=x->Lc->size+1;
            if (x->Rc==nil) break;
            x=x->Rc;
        }
        else
        {
            if (x->Lc==nil) break;
            x=x->Lc;
        }
    }
    pnn d=split(r,cnt);
    x=new node(p);
    return merge(merge(d.X,x),d.Y);
}

node *del(node *r,int p)
{
    node *x=r;
    int cnt=0;
    while (x!=nil)
    {
        if (x->id==p)
        {
            cnt+=x->Lc->size;
            break;
        }
        if (cmp(x->id,p))
        {
            cnt+=x->Lc->size+1;
            if (x->Rc==nil) break;
            x=x->Rc;
        }
        else
        {
            if (x->Lc==nil) break;
            x=x->Lc;
        }
    }
    pnn a=split(r,cnt);
    pnn b=split(a.Y,1);
    return merge(a.X,b.Y);
}

int solve(node *r,int x,int y)
{
    int cnt=0;
    node *p=nil;
    while (r!=nil)
    {
        if (w[r->id].get(x)<=y)
        {
            p=r;
            cnt+=r->Lc->size+1;
            if (r->Rc==nil) break;
            r=r->Rc;
        }
        else
        {
            if (r->Lc==nil) break;
            r=r->Lc;
        }
    }
    if (p==nil)
        return -1;
    if (w[p->id].get(x)==y||cnt%2)
        return w[p->id].from;
    return -1;
}

map<int,node*> root;

int MINX,MAXX;

void init()
{
    cin>>n;
    for (int i=1;i<=n;++i)
    {
        int k;
        scanf("%d",&k);
        vector<point> v;
        for (int j=0;j<k;++j)
        {
            int x,y;
            scanf("%d%d",&x,&y);
            point p(x,y);
            v.push_back(p);
            s[p]=i;
        }
        for (int j=0;j<k;++j)
            w.push_back(line(v[j],v[(j+1)%k],i,m++));
    }
    for (auto p : w)
        if (p.a.x<p.b.x)
        {
            event.insert(p.a.x);
            inp[p.a.x].push_back(p.id);
            event.insert(p.b.x);
            oup[p.b.x].push_back(p.id);
        }
        else
            g[p.a.x][point(p.a.y,p.b.y)]=p.from;
    MINX=*event.begin();
    MAXX=*event.rbegin();
    nil=new node;
    nil->Lc=nil->Rc=nil;
    nil->size=0;
    node *tmp=nil;
    for (auto x : event)
    {
        for (auto p : oup[x])
            tmp=del(tmp,p);
        auto pp=event.find(x);
        auto xx=pp;
        ++xx;
        X0=(x+*xx)/2.;
        for (auto p : inp[x])
            tmp=ins(tmp,p);
        root[x]=tmp;
    }
}

const int INF=1000000010;

int check(int x,int y)
{
    point p(x,y);
    if (s.count(p)) return s[p];
    auto it=g[x].upper_bound(point(y,INF));
    if (it!=g[x].begin())
    {
        --it;
        if (it->X.x<=y&&y<=it->X.y) return it->Y;
    }
    if (MINX<=x&&x<=MAXX)
    {
        auto it=root.upper_bound(x);
        --it;
        return solve(it->Y,x,y);
    }
    return -1;
}

void work()
{
    int T;
    cin>>T;
    while (T--)
    {
        int x,y;
        scanf("%d%d",&x,&y);
        printf("%d\n",check(x,y));
        fflush(stdout);
    }
}

int main()
{
    init();
    work();
    return 0;
}