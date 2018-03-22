import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;
import java.io.BufferedReader;
import java.io.InputStream;

public class Main {
    public static void main(String[] args) {
        InputStream input = System.in;
        OutputStream output = System.out;
        InputReader in = new InputReader(input);
        PrintWriter out = new PrintWriter(output);
        Solve solver = new Solve();
        solver.solve(1, in, out);
        out.close();
    }

    static class Solve {
        public void solve(int testNumber, InputReader in, PrintWriter out) {
            int n = in.nextInt();
            Semt[] semtler = new Semt[n];
            for(int i = 0; i<n;i++){
                semtler[i]=new Semt(i+1);
            }
            for (int i = 0; i < n - 1; ++i) {
                Semt a = semtler[in.nextInt() - 1];
                Semt b = semtler[in.nextInt() - 1];
                a.komsu.add(b);
                b.komsu.add(a);
            }
            Semt baslangicSemt = null;
            for (int i = 0; i < n; ++i) {
                semtler[i].baslangic = in.nextInt();
                if (semtler[i].baslangic == 0) baslangicSemt = semtler[i];
            }
            Semt sonSemt = null;
            for (int i = 0; i < n; ++i) {
                semtler[i].son = in.nextInt();
                if (semtler[i].son == 0) sonSemt = semtler[i];
            }
            int kontrol = 0;
            for (Semt smt : semtler) if (smt.baslangic == smt.son) ++kontrol;
            int tasimaSayisi = 0;
            baslangicSemt.tasinirMi = true;
            if (!baslangicSemt.neredenGeldim(sonSemt, null)) throw new RuntimeException();
            while (baslangicSemt != sonSemt) {
                Semt smtt = baslangicSemt.sonrakiSemtTahmini;
                if (smtt.baslangic == smtt.son) --kontrol;
                baslangicSemt.baslangic = smtt.baslangic;
                smtt.baslangic = 0;
                if (baslangicSemt.baslangic == baslangicSemt.son) ++kontrol;
                if (smtt.baslangic == smtt.son) ++kontrol;
                baslangicSemt = smtt;
                baslangicSemt.tasinirMi = true;
                ++tasimaSayisi;
            }
            if (kontrol == n) {
                out.println(tasimaSayisi);
                return;
            }

            Semt imk = null;
            baslangicSemt.baslangicTasima(null);
            outer:
            for (Semt smtt : semtler) {
                if (smtt.baslangic != smtt.son) {
                    for (Semt kms : smtt.komsu) {
                        if (kms.tasinmaDurumu >= 0) {
                            imk = kms;
                            tasimaSayisi += 2 * kms.tasinmaDurumu;
                            break outer;
                        }
                    }
                }
            }
            if (imk == null) {
                out.println("i");
                return;
            }
            if (!baslangicSemt.neredenGeldim(imk, null)) throw new RuntimeException();
            while (baslangicSemt != imk) {
                Semt smtt = baslangicSemt.sonrakiSemtTahmini;
                baslangicSemt.baslangic = smtt.baslangic;
                baslangicSemt.son = smtt.son;
                smtt.baslangic = 0;
                smtt.son = 0;
                baslangicSemt = smtt;
            }

            int yolOl = 0;
            Semt yolBS = imk;
            Semt yolFS = imk;
            List<Semt> dino1 = new ArrayList<>();
            List<Semt> dino2 = new ArrayList<>();
            int tTasi = 0;
            for (Semt dinozor : imk.komsu) {
                if (dinozor.baslangic != dinozor.son) {
                    ++yolOl;
                    if (yolOl > 2) {
                        out.println("i");
                        return;
                    }
                    List<Semt> yolcu;
                    if (yolOl == 1) {
                        yolcu = dino1;
                    } else {
                        yolcu = dino2;
                    }
                    yolcu.add(dinozor);
                    Semt dinoSon = dinozor;
                    Semt dinoNerden = baslangicSemt;
                    ++tTasi;
                    outer3:
                    while (true) {
                        for (Semt smtt : dinoSon.komsu) {
                            if (smtt != dinoNerden) {
                                if (smtt.baslangic != smtt.son) {
                                    yolcu.add(smtt);
                                    dinoNerden = dinoSon;
                                    dinoSon = smtt;
                                    ++tTasi;
                                    continue outer3;
                                }
                            }
                        }
                        break;
                    }
                    if (yolOl == 1) yolBS = dinoSon;
                    else yolFS = dinoSon;
                }
            }
            if (kontrol + tTasi != n) {
                out.println("i");
                return;
            }

            baslangicSemt.yeniYolKonum = 0;
            for (int i = 0; i < dino2.size(); ++i) {
                dino2.get(i).yeniYolKonum = 1 + dino1.size() + dino2.size() - i;
            }
            int[] yeniYolBaslangic = new int[dino1.size() + dino2.size()];
            int[] yeniYolSonu = new int[dino1.size() + dino2.size()];
            for (int i = 0; i < dino1.size(); ++i) {
                yeniYolBaslangic[i] = dino1.get(i).baslangic;
                yeniYolSonu[i] = dino1.get(i).son;
            }
            for (int i = 0; i < dino2.size(); ++i) {
                yeniYolBaslangic[yeniYolBaslangic.length - 1 - i] = dino2.get(i).baslangic;
                yeniYolSonu[yeniYolSonu.length - 1 - i] = dino2.get(i).son;
            }
            int snDrm;
            for (snDrm = 0; snDrm < yeniYolSonu.length; ++snDrm) {
                if (yeniYolSonu[snDrm] == yeniYolBaslangic[0]) break;
            }
            if (snDrm >= yeniYolSonu.length) {
                throw new RuntimeException();
            }
            for (int i = 0; i < yeniYolSonu.length; ++i) {
                if (yeniYolSonu[(i + snDrm) % yeniYolSonu.length] != yeniYolBaslangic[i]) {
                    out.println("i");
                    return;
                }
            }
            int tt = 0;
            int ttt = 0;
            for (Semt smtt : dino1)
                if (smtt.tasinirMi) ++ttt;
                else break;
            for (Semt smtt : dino2)
                if (smtt.tasinirMi) ++tt;
                else break;
            long tastas = Math.min(Math.abs((1 + yeniYolBaslangic.length) * (long) snDrm - tt) - tt, Math.abs((1 + yeniYolBaslangic.length) * (long) (yeniYolBaslangic.length - snDrm) - ttt) - ttt) + tasimaSayisi;
            out.println(Math.min(yolBS.kacinci, yolFS.kacinci) + " " + Math.max(yolBS.kacinci, yolFS.kacinci) + " " + (tastas));

        }

        static class Semt {
            int kacinci;
            int baslangic;
            int son;
            boolean tasinirMi = false;
            int tasinmaDurumu = -1;
            List<Semt> komsu = new ArrayList<>(1);
            int yeniYolKonum;
            Semt sonrakiSemtTahmini = null;

            public Semt(int kacinci) {
                this.kacinci = kacinci;
            }

            public boolean neredenGeldim(Semt baslangicSemt, Semt parent) {
                if (this == baslangicSemt) return true;
                for (Semt smtt : komsu) {
                    if (smtt != parent) {
                        if (smtt.neredenGeldim(baslangicSemt, this)) {
                            sonrakiSemtTahmini = smtt;
                            return true;
                        }
                    }
                }
                return false;
            }

            public void baslangicTasima(Semt parent) {
                if (baslangic != son) return;
                if (tasinirMi) {
                    tasinmaDurumu = 0;
                } else {
                    tasinmaDurumu = parent.tasinmaDurumu + 1;
                }
                for (Semt smtt : komsu) {
                    if (smtt != parent) {
                        smtt.baslangicTasima(this);
                    }
                }
            }

        }

    }

    static class InputReader {
        public BufferedReader reader;
        public StringTokenizer tokenizer;

        public InputReader(InputStream stream) {
            reader = new BufferedReader(new InputStreamReader(stream), 32768);
            tokenizer = null;
        }

        public String next() {
            while (tokenizer == null || !tokenizer.hasMoreTokens()) {
                try {
                    tokenizer = new StringTokenizer(reader.readLine());
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }
            return tokenizer.nextToken();
        }

        public int nextInt() {
            return Integer.parseInt(next());
        }

    }
}

/*

5
1 2
2 3
2 5
5 4
0 1 2 4 3
3 2 1 4 0
-->> i


6
1 2
2 3
2 5
5 4
2 6
0 4 3 2 1 5
4 3 0 2 1 5

--->> 2


6
1 2
2 3
2 5
5 4
2 6
0 4 2 1 3 5
4 0 2 5 1 3
--->> 4 6 5

 */