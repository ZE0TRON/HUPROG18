#include <iostream>
#include <vector>
#include <stdio.h>
#include <ctime>
#include <algorithm>
using namespace std;

#define maxn 220000 // maximal number of nodes

struct node{ // node of the first persistent tree
    int add2; // add2 is the sum of all Bs, added to this node, according to the statement, B<=1000, M<=100000, so int is ok
    long long add1,sum; // sum of all As for the node, sum in the subtree
    node*l,*r; // left and right sons
};

node*init(int l,int r){ // creates the progressions persistent tree like an ordinary segtree
    node*ret=new node;
    ret->add1=ret->add2=ret->sum=0;
    if(l<r){
        ret->l=init(l,(l+r)/2);
        ret->r=init((l+r)/2+1,r);
    }
    return ret;
}

inline long long calc(long long a,long long b,long long c){ // calculate the sum a+(a+b)+(a+2*b)...+(a+(c-1)*b)
    return a*c+((c*(c-1))/2)*b;
}

long long query(node*me,int cL,int cR,int l,int r,long long sa1,long long sa2){ // query on the progressions persistent tree, quite standard
    if(cL==l&&cR==r)return me->sum+calc(sa1,sa2,cR-cL+1);
    long long ret=0;
    int mid=(cL+cR)>>1;
    if(l<=min(mid,r))ret+=query(me->l,cL,mid,l,min(mid,r),sa1+me->l->add1,sa2+me->l->add2);
    if(max(mid+1,l)<=r)ret+=query(me->r,mid+1,cR,max(mid+1,l),r,sa1+me->r->add1+sa2*(mid-cL+1),sa2+me->r->add2);
    return ret;
}

inline long long get(node*me,int cL,int cR){ // calculates the sum of the subtree for some node
    return me->sum+calc(me->add1,me->add2,cR-cL+1);
}

node*modify(node*me,int cL,int cR,int l,int r,long long a,long long b){ // progressions persistent tree modify
    node*ret=new node; // clone the current vertice
    ret->l=me->l,ret->r=me->r; // clone the current vertice
    ret->sum=me->sum,ret->add1=me->add1,ret->add2=me->add2; //clone the current vertice
    if(cL==l&&cR==r){ // then, usual segment tree modifying follow
        ret->add1+=a,ret->add2+=b;
        return ret;
    }
    int mid=(cL+cR)>>1;
    if(l<=min(r,mid))ret->l=modify(ret->l,cL,mid,l,min(r,mid),a,b);
    if(max(l,mid+1)<=r)ret->r=modify(ret->r,mid+1,cR,max(l,mid+1),r,a+max(0,mid-l+1)*b,b);
    ret->sum=get(ret->l,cL,mid)+get(ret->r,mid+1,cR);
    return ret; // clonned node should be returned
}

struct infNode{ // persistent array
    int l,r,x;
    infNode*le,*ri;
};

infNode*changeRoot[maxn];

infNode*initInfNode(int l,int r){ // create the persistent array like an ordinary segtree
    infNode*ret=new infNode;
    ret->l=l,ret->r=r,ret->x=0;
    if(l!=r){
        ret->le=initInfNode(l,(l+r)/2);
        ret->ri=initInfNode((l+r)/2+1,r);
    }
    return ret;
}

int infnodeGet(infNode*me,int j){ // query on a persistent array, doesn't differ from a query on a segtree
    if(me->l==me->r)return me->x;
    if(me->le->r>=j)return infnodeGet(me->le,j);else return infnodeGet(me->ri,j);
}

infNode*infnodeUpdate(infNode*me,int j,int x){ // updates some value in the persistent array and returns the new version
    infNode*ret=new infNode;  // clone the current vertice
    ret->l=me->l,ret->r=me->r; // clone the current vertice
    ret->le=me->le,ret->ri=me->ri; // clone the current vertice
    ret->x=me->x; // clone the current vertice
    if(ret->l==ret->r){ // then, ordinary modifying follows
        ret->x=x;
        return ret;
    }
    if(ret->le->r>=j)ret->le=infnodeUpdate(ret->le,j,x);else ret->ri=infnodeUpdate(ret->ri,j,x);
    return ret; // the return clonned vertice
}

vector<node*>root[maxn];
vector<int>version[maxn],refreshed[maxn],chg;
vector<pair<int,int> >queries[maxn],precalc[maxn];
int n,m,i,j,x,y,f[maxn*2],t[maxn*2],p[maxn*2],ii,up[maxn][20],subtree[maxn],chain[maxn],chains,chainSize[maxn],go_back=-1,lnk[maxn],modifies;
int tin[maxn],tout[maxn],timer,place[maxn],aa,bb,L,depth[maxn],pred[maxn],ver,changes,old_ver,pr[maxn],X[maxn],Y[maxn],AA[maxn],BB[maxn];
pair<int,int>a[maxn];
bool changing;
long long lastans;
char ch[maxn];

void addedge(int x,int y){ // add an edge to the tree
    t[++ii]=y;
    p[ii]=f[x];
    f[x]=ii;
}

int ex[maxn],ey[maxn],o[maxn];

void readIn(){
    scanf("%d%d",&n,&m); // amount of vertices and queries
    for(i=1;i<n;i++)scanf("%d%d",&ex[i],&ey[i]);
    for(i=1;i<n;i++)o[i]=i;
    for(i=1;i<n;i++){
        j=rand()%(n-1)+1;
        swap(o[i],o[j]);
    }
    for(i=1;i<n;i++){
        addedge(ex[o[i]],ey[o[i]]);
        addedge(ey[o[i]],ex[o[i]]);
    }
}

void dfs(int k){ // DFS, used to build LCA, and calculate sizes of subtrees.
    subtree[k]=1;
    tin[k]=++timer; // important for LCA calculation
    int q=f[k];
    while(q){
        if(!subtree[t[q]]){
            depth[t[q]]=1+depth[k];
            up[t[q]][0]=k; // important for LCA calculation
            for(int j=1;j<20;j++)up[t[q]][j]=up[up[t[q]][j-1]][j-1]; // important for LCA calculation
            dfs(t[q]);
            subtree[k]+=subtree[t[q]]; // calculate the size of the subtree, it will be used in hldot construction
        }
        q=p[q];
    }
    a[k]=make_pair(subtree[k],k);
    tout[k]=++timer; // important for LCA calculation
}

void givechain(int k){ // greedily build the hldot. take the son with the heaviest subtree
    chain[k]=chains;
    place[k]=++chainSize[chains];
    int q=f[k],mx=0;
    while(q){
        if(subtree[t[q]]<subtree[k])mx=max(mx,subtree[t[q]]);
        q=p[q];
    }
    q=f[k];
    while(q){
        if(subtree[t[q]]==mx){
            givechain(t[q]);
            break;
        }
        q=p[q];
    }
}

void build_dot(){
    for(i=0;i<20;i++)up[1][i]=1;
    dfs(1); // at first, run the DFS
    sort(a+1,a+n+1);
    reverse(a+1,a+n+1);
    for(i=1;i<=n;i++)if(!chain[a[i].second]){ // lauch the hldot building
            pred[++chains]=up[a[i].second][0];
            givechain(a[i].second);
            root[chains].push_back(init(1,chainSize[chains]));
            version[chains].push_back(0);
        }
}

inline bool anc(int x,int y){ // checks whether X is ancestor of Y
    return (tin[x]<=tin[y]&&tout[x]>=tout[y]);
}

inline int LCA(int x,int y){ // compute the LCA for X and Y
    if(anc(x,y))return x;
    for(int i=19;i+1;i--)if(!anc(up[x][i],y))x=up[x][i];
    return up[x][0];
}

node*getCurrentRoot(int chain){ // returns actual version for the chain
    if(version[chain].back()==changes&&changing)return root[chain][version[chain].size()-1]; // if we're modifying now, and it was already changed, then take the last version
    if(version[chain].back()>go_back)return root[chain].back(); // also, if it's clear that the last version can be taken
    int now=infnodeGet(changeRoot[ver],chain); // otherwise, we use the persistent array (persistent arrays form the tree, btw) to get the current last version
    int l=0,r=version[chain].size()-1,mid; // index of the version is now known, we should find the root with this index
    while(l<r){
        mid=(l+r+1)>>1;
        if(version[chain][mid]>now)r=mid-1;else l=mid;
    }
    return root[chain][l]; // ... and return this root
}

void lift(int low,int high,long long a,long long b){ // modifying for the case when high is the ancestor of low
    if(chain[low]==chain[high]){ // case when it's necessary to modify only one chain
        long long amount=place[low]-place[high];
        node*newroot=modify(getCurrentRoot(chain[low]),1,chainSize[chain[low]],place[high],place[low],a+amount*b,-b);
        root[chain[low]].push_back(newroot); // remember the new version
        version[chain[low]].push_back(changes); // remember the new version
        chg.push_back(chain[low]); // remember the new version
    }else{ // otherwise, the whole prefix should be modified, and then lift should be called again
        long long amount=place[low]-1;
        node*newroot=modify(getCurrentRoot(chain[low]),1,chainSize[chain[low]],1,place[low],a+amount*b,-b);
        root[chain[low]].push_back(newroot); // again, remember the new version
        version[chain[low]].push_back(changes); // remember the new version
        lift(pred[chain[low]],high,a+b*place[low],b); // run lift again. generally, it will be called till the moment chain[a]=chain[b]
        chg.push_back(chain[low]); // remember the new version
    }
}

void change(int L,int x,int y,long long a,long long b){ // more general version of changing. it's not necessary for the X to be an ancestor for Y
    // split it to the two cases: [x; L], [y; L)
    long long dist=depth[x]+depth[y]-2*depth[L]+1;
    lift(x,L,a,b); // [x; L]
    if(y!=L){ // [y; L)
        int pL=y,remain=depth[y]-depth[L]-1;
        for(j=19;j+1;j--)if(remain&(1<<j))pL=up[pL][j];
        lift(y,pL,a+b*(dist-1),-b);
    }
}

long long getsum(int low,int high){ // question query for the case when high is an ancestor of low
    // same logic as in lift
    if(chain[low]==chain[high]){
        node*root=getCurrentRoot(chain[low]);
        return query(root,1,chainSize[chain[low]],place[high],place[low],root->add1,root->add2);
    }else{
        node*root=getCurrentRoot(chain[low]);
        return query(root,1,chainSize[chain[low]],1,place[low],root->add1,root->add2)+getsum(pred[chain[low]],high);
    }
    // notice, that you don't have to save any versions because you don't change anything
}

long long query(int L,int x,int y){ // more general case for quetion query
    if(L==x)return getsum(y,L); // if x is LCA
    if(L==y)return getsum(x,L); // or if y is LCA
    // otherwise, split it into two queries: [x; L] and [y; L)
    long long ret=getsum(x,L); // [x; L]
    int pL=y,remain=depth[y]-depth[L]-1;
    for(j=19;j+1;j--)if(remain&(1<<j))pL=up[pL][j];
    printf("BURA ret%lld x%d L%d y%d pL%d remai%d  gets%lld ",ret,x,L,y,pL,remain,getsum(y,pL));
    return ret+getsum(y,pL); // [y; L)
}

void upd_changed(){ // write all the updates in the persistent array
    for(j=0;j<chg.size();j++){
        infNode*tmp=infnodeUpdate(changeRoot[changes],chg[j],changes);
        changeRoot[changes]=tmp;
    }
}

int used[maxn],visited;

int main (int argc, char * const argv[]) {
    srand(time(NULL));
    readIn(); // read data
    build_dot(); // build the decomposition
    changeRoot[0]=initInfNode(1,chains); // build the version 0 of the persistent array
    for(i=1,changes=0,ver=0;i<=m;i++){
        ch[i]=getchar(); // get the type of the query
        while(ch[i]!='c'&&ch[i]!='q'&&ch[i]!='l')ch[i]=getchar(); // get the type of the query
        changing=false;
        if(ch[i]=='c'){ // changing query
            scanf("%d%d%d%d",&X[i],&Y[i],&AA[i],&BB[i]);
            X[i]=(X[i]+lastans)%n+1; // get actual X
            Y[i]=(Y[i]+lastans)%n+1; // get actual Y
            pr[++changes]=ver;
            changeRoot[changes]=new infNode; // create a new node in versions tree
            changeRoot[changes]=changeRoot[ver]; // create a new node in versions tree
            changing=true;
            x=X[i],y=Y[i],aa=AA[i],bb=BB[i];
            L=LCA(x,y); // get LCA
            chg.clear();
            change(L,x,y,aa,bb); // do the change
            upd_changed(); // update persistent array
            ver=changes; // update the current version's index
            ++modifies;
            //printf("%lld\n",query(LCA(1,5),1,5));
        }else if(ch[i]=='q'){
            scanf("%d%d",&X[i],&Y[i]);
            X[i]=(X[i]+lastans)%n+1; // get actual X
            Y[i]=(Y[i]+lastans)%n+1; // get actual Y
            x=X[i],y=Y[i];
            L=LCA(x,y); // get LCA
            lastans=query(L,x,y); // answer the query
            printf("%lld\n",lastans);
        }else if(ch[i]=='l'){
            scanf("%d",&X[i]);
            X[i]=(X[i]+lastans)%(modifies+1); // get actual version
            ver=X[i];
            go_back=changes;
        }
    }
    return 0;
}

/*

5 7
1 2
2 3
3 4
4 5
c 1 4 2 3
c 2 3 5 10
q 1 3
l 2
q 1 3
l 1
q 1 3


5 7
2 5
1 3
1 4
3 4
c 1 4 2 3
c 2 3 5 10
q 1 3
l 1
q 1 3
l 1
q 1 3




 */

