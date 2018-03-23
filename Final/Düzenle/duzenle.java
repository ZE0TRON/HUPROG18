import java.io.BufferedReader;
import java.io.PrintWriter;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;
 
public class Main {
 
	private static void debug(Object... args) {
		System.out.println(Arrays.deepToString(args));
	}
 
	public static void main(String[] rags) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		PrintWriter pw = new PrintWriter(System.out, true);
		String text = br.readLine();
		int N = Integer.parseInt(br.readLine());
		int K = cntUnqPalins(text);
		pw.println(bracelets(N, K));
	}
 
	private static Set<Integer> pFacs(int N) {
		Set<Integer> f = new HashSet<>();
		while (N > 1) {
			for(int i=2;i<=N;i++) {
				if(N%i==0) {
					f.add(i);
					while(N%i==0) N/=i;
				}
			}
		}
		return f;
	}
	
	private static int eulerTotient(int N) {
		Set<Integer> pf = pFacs(N);
		int res = N;
		int mm = 1;
		for(int p : pf) {
			res /= p;
			mm *= (p-1);
		}
		return res * mm;
	}
	                                                                                                                      
	private static BigInteger necklaces(int n, int k) {
		BigInteger res = BigInteger.ZERO;
		BigInteger K = BigInteger.valueOf(k);
		for(int d=1;d<=n;d++) {
			if(n%d==0) {
				BigInteger expd = K.pow(n/d);
				res = res.add(expd.multiply(BigInteger.valueOf(eulerTotient(d))));
			}
		}
		return res.divide(BigInteger.valueOf(n));
	}
 
	private static BigInteger bracelets(int n, int k) {
		if(n%2==0) {
			BigInteger K = BigInteger.valueOf(k);
			BigInteger TWO = BigInteger.valueOf(2);
			BigInteger K1 = K.add(BigInteger.ONE);
			BigInteger expd = K.pow(n/2).multiply(K1);
			expd = expd.divide(TWO);
			return expd.add(necklaces(n,k)).divide(TWO);
		}
		else {
			BigInteger K = BigInteger.valueOf(k);
			BigInteger TWO = BigInteger.valueOf(2);
			BigInteger expd = K.pow((n+1)/2);
			return expd.add(necklaces(n,k)).divide(TWO);
		}
	}
         
	private static final int PRM = 13;
	private static long[]pws;
	private static int cntUnqPalins(String text) {
		
		Set<Long> hs = new HashSet<>();
		StringBuilder et = new StringBuilder("#");
		for(int i=0;i<text.length();i++) {
			hs.add((long)text.charAt(i));
			et.append(text.charAt(i)).append("#");
		}
		String etext = et.toString();
		int[]p=new int[etext.length()];
		long[]rh=new long[etext.length()];
		rh[0]=etext.charAt(0);
		pws=new long[etext.length()];
		pws[0]=1;
		for(int i=1;i<etext.length();i++) {
			rh[i]=rh[i-1]*PRM + etext.charAt(i);
			pws[i]=pws[i-1]*PRM;
		}
		int C = 0, R = 0;
		for(int i=0;i<etext.length();i++) {
			int ip = 2*C - i;
			boolean inPalin = ip >= 0 && i <= R && ip < i;
			if(inPalin && p[ip] < R - i) {
				p[i] = p[ip];
			}
			else {
				int cnt=inPalin ? R-i : 0;
				for(int j=cnt+1;i+j<etext.length() && i-j >= 0;j++) {
					if(etext.charAt(i+j) == etext.charAt(i-j)) {
						if (etext.charAt(i + j) != '#') {
							long hash = rh[i + j] - low(rh, i - j - 1, 2*j+1);
							hs.add(hash);
						}
						cnt++;
					}
					else {
						break;
					}
				}
				p[i]=cnt;
				C=i;
				R=Math.min(etext.length()-1, i+cnt);
			}
		}
		return hs.size();
	}
 
	
	private static long low(long[] rh, int i, int j) {
		if(i < 0) return 0;
		return rh[i]*pws[j];
	}
}

