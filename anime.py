from sty import fg, bg, ef, rs
from os import system
from time import sleep
from random import randint
draw = fg.black+'''                                                                                                                    
               AU           ██████████████████       AV                                                                                
   AA                 ██████Z                F████         AW     X░░░░G                                                               
            AF      ██Z                          F██    AX       X░G  X░G                                                              
    AB            ██Z                              F██          X░G         BD      BQ                                                 
                ██Z                                 F██  AY    X░G                                                                     
                ██Z          F████████████Z          F██        X░G             BR                                                     
   AC     AG  ██Z      F██████O░░░░░░░▒▒▒F██Z        F██         X░G  X░G  BC                                                          
              ██Z  F████O▒▒▒▒▒▒▒▒▒▒▒▒F██████Z         ░F██        X░░░░G               BJ                                              
              ██Z  F██O▒▒▒▒F██████████Q░░░░░░F█Z       ░F██                     BS                                                     
            ██Z    F██OF████Q░░░░░░░░░░░░░░░F█Z       ░░░F██  BA         Y░░░░G                                                        
            ██Z  F██████Q░░░░░░░░░░B▒▒▒▒▒▒Q░░░F█Z   ░░░░░F██            Y░G  Y░G         BK                                            
            ██Z  F████Q░░░░░░K   B▒▒Q░░░░░░░░░F█Z   ░░░░░F██           Y░G  YGY░G                                                      
      AD    ██Z  F████Q░░K       Q░░░F██████Q░F█Z   ░░░░░F██  BB       Y░G YG Y░G                                                      
            ██Z  F██Q░░K           F██KFPWP▓Q░F█Z  ░░░░░░░F██    BU    Y░GYG  Y░G       BL                                             
 AM         ██Z  F██QB▒▒▒▒▒▒K            PPQ░░░F█Z░░░░░░░░F██           Y░G  Y░G               BO                                      
      AL    ██Z  F██B▒Q░░░░░░K              Q░░░F█Z░░░░F█Z F██           Y░░░░G    BT   BM                                             
 AE         ██Z  F████Q ████K               Q░░░F█Z░░░░F█Z F██     BE                         BP                                       
            ██Z  F██ZF██KPW▓Q░K                F██Z░░░░F█Z ░░F██           BH  N░░░░░░░G                                               
     AH       ██ZF██ZF██KP░░K    B░░K     IIK  F██Z░░░░F████████        BG    N░G N░G N░G    BN                                        
 AT           ██████ZF██K                    F██Z ░░░░░F██K░░░░F██   BF       N░G N░G N░G                                              
         AK   ██Z░░░░░░F██K   IIK    L▒▒░K   F██Z ░░░F██K░░░░░  ░F██     BI   N░G N░G N░G                                              
 AI           ██Z░░░░░░░░F██K         L░░░K    F██Z ░░░F██K░░░     F██        N░G N░G N░G     BW                                       
              ██Z ░░░░░░░░░F████K          F████Z ░░░F██K░░░         F██      NG  NG  NG                                               
            ██Z░  ░░░░░░░░░░░░░F████████████KF██Z ░░░F██K░░░         F██                                                               
      AJ    ██Z   ░░  ░░░░░░░░░░░░░░░░░░░F██KF██Z ░░░F████K░           F██  BV   BZ          VG                                        
            ██Z   ░░  ░░░░░░░░░░░░░░░░░F██KF██Z   ░░░F████K░           F██            V░░░░░░░G                                        
      AO    ██Z ░░░░  ░░░░░░░░░░░░░F████KF████Z   ░░░F████K░░░          ░F██           VG                                              
 AN       ██Z   ░░  ░░░░░░░░░F██████K░░F██JF██Z   ░░░F██OF██K░           F██    BX     VG   VG   BY                                    
    AP    ██Z ░░░░  ░░░░░░░F██K ░░░F████J░░F██Z   ░░░F██OF██K░            ░F██         V░░░░G                                          
        ██Z   ░░  ░░░░░░░F██K ░F████J░░░░░░F██Z  F██ZF██O▒▒F██K░          ░F██         VG     VG                                       
AQ      ██Z ░░░░░░░░░░░F████████J░░░░░░░░░░F██Z  F██ZF██O▒▒F██K░            ░F██  CH   VG    V░G                                       
   AR ██Z ░░░░░░░░░F████J░░F██J░░░░░░░░░░░OF██Z  F██ZF██O▒▒▒▒F██K░          ░F██      V░░░░░░░░G  CF                                   
      ██Z ░░░░░F████J░░░░F██J░░░░░░░░░░░░░OF██ZF████Z░░F██O▒▒F██K░            ░F██                                                     
AS  ██Z ░░░F████J░▒▒░░░░░F██J░░░░░░░░░░░O▒▒F██ZF██OF██ZF██O▒▒▒▒F██K░          ░F██   CB              C█G                               
    ██Z ░F██J░░░░░░░░░░O▒F██O▒J░░░░░O▒▒▒▒▒▒▒▒F████OF██ZF██O▒▒▒▒F████K         ░░░F██     BY   C░░░░░░░G                                
    ██ZF██J░░░░░░░░░░░░O▒F██O▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒F██ZF██O▒▒▒▒F████K░          ░F██             C░G                                   
  ██Z ░F██J░░░░░░░░░░O▒▒▒▒▒F██O▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒F████O▒▒▒▒F██  ██K         ░F██      CA     C░G                                   
  ██ZF██J░░░░░░░░░░░O▒▒▒▒▒▒F██OF██████████████████O▒▒▒▒▒▒▒▒▒▒F██    ██K░        ░░░F██          C░G                                    
  ██ZF██O▒J░░░░░O▒▒▒▒▒▒▒▒▒▒▒▒F██K                F██████O▒▒▒▒F██      ██K░      ░░░F██          C░G                                    
██Z ░F██O▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒F████KF████K        F████K    F████OF██        ██K░    ░░░░░F██       C░G                                     
██Z ░F██O▒▒▒▒▒▒▒▒▒▒▒F████K   F██K  F██████████K            F██          ██K░░░  ░░░░░F██                                               
██Z ░░░F██O▒▒▒▒▒▒▒F██K     F██K                           F██            ██K░░░░░░░░░░F██ CI    CE                                     
██Z ░░░░░F██O▒▒▒▒▒F██K    F██K                          F██              ██K░░░░░░░░░░F██                                              
██Z ░░░░░░░░F███████K   F██K                            F██                ██K░░░░░░░░F██    CD                                        
  ██Z░░░░░░░░░░░░░░F█████K                            F██                    ██K░░░░░░░░F██                                            
    ██Z░░░░░░░░░░░F██K                              F██                      ██K░░░░░░░░F██'''+bg.rs+fg.rs
colors = [(255,0,0),(255,50,0),(255,100,0),(255,150,0),(255,200,0),(255,255,0),(200,255,0),(150,255,0),(100,255,0),(50,255,0),(0,255,0),(0,255,50),(0,255,100),(0,255,150),(0,255,200),(0,255,255),(0,200,255),(0,150,255),(0,100,255),(0,50,255),(0,0,255),(50,0,255),(100,0,255),(150,0,255),(200,0,255),(255,0,255),(255,0,200),(255,0,150),(255,0,100),(255,0,50),(255,0,0)]
bra = [(255,0,0),(21,255,0),(0,187,255),(51,0,255),(255,0,255),(255,0,89)]
c = 0
d = 15
e = 16

f = 0
g = 7
h = 14
i = 21
j = 28

while True:
  sleep(0.1)
  system("cls")
  if c == 31:
    c = 0
  cc = list(colors[int(c)])
  cr = int(cc[0])
  cg = int(cc[1])
  cb = int(cc[2])
  c = c + 1

  if d == 31:
    d = 0
  dd = list(colors[int(d)])
  dr = int(dd[0])
  dg = int(dd[1])
  db = int(dd[2])
  d = d + 1


  if e == 31:
    e = 0
  ee = list(colors[int(e)])
  er = int(ee[0])
  eg = int(ee[1])
  eb = int(ee[2])
  e = e + 1

  f =  randint(0,30)
  ff = list(colors[int(f)])
  zr = int(ff[0])
  zg = int(ff[1])
  zb = int(ff[2])
  f = f + 1

  g =  randint(0,30)
  rr = list(colors[int(g)])
  gr = int(rr[0])
  gg = int(rr[1])
  gb = int(rr[2])
  g = g + 1

  h =  randint(0,30)
  hh = list(colors[int(h)])
  hr = int(hh[0])
  hg = int(hh[1])
  hb = int(hh[2])
  h = h + 1

  i =  randint(0,30)
  ii = list(colors[int(i)])
  ir = int(ii[0])
  ig = int(ii[1])
  ib = int(ii[2])
  i = i + 1


  j =  randint(0,30)
  jj = list(colors[int(j)])
  jr = int(jj[0])
  jg = int(jj[1])
  jb = int(jj[2])
  j = j + 1

  a = draw
  shh = ["AA","AB","AC","AD","AE","AF","AG","AH","AI","AJ","AK","AL","AM","AN","AO","AP","AQ","AR","AS","AT","AU","AV","AW","AX","AY","AZ","BA","BB","BC","BD","BE","BF","BG","BH","BI","BJ","BK","BL","BM","BN","BO","BP","BQ","BR","BS","BT","BU","BV","BW","BX","BY","BZ","CA","CB","CC","CD","CE","CF","CG","CH","CI"]
  for seh in shh:
    checkout = randint(0,1)
    if checkout == 0:
      n = randint(0,1)
      yo = randint(0,5)
      a = a.replace(seh,fg(bra[yo][0],bra[yo][1],bra[yo][2])+" "+str(n)+fg(0,0,0)+"")
    else:
      a = a.replace(seh,"  ")

  a = a.replace("Z",bg(cr,cg,cb)+"█")
  a = a.replace("R",bg(255,0,0)+"█")
  a = a.replace("L",bg(255,0,0)+"█")
  a = a.replace("K",bg(245,190,154)+"░")
  a = a.replace("Q",bg(237, 165, 119)+"░")
  a = a.replace("F"," "+bg(0,0,0))
  a = a.replace("D",bg(0,0,0)+"░")
  a = a.replace("W",bg(255,255,255)+"░")
  a = a.replace("I",bg(245, 166, 224)+"░")
  a = a.replace("B",bg(112,100,92)+" ")
  a = a.replace("P",bg(180, 16, 235)+"░")
  a = a.replace("J",bg(dr,dg,db)+"░")
  a = a.replace("O",bg(er,eg,eb)+"▒")
  a = a.replace("X",bg(zr,zg,zb)+"░")
  a = a.replace("Y",bg(gr,gg,gb)+"░")
  a = a.replace("N",bg(hr,hg,hb)+"░")
  a = a.replace("V",bg(ir,ig,ib)+"░")
  a = a.replace("C",bg(jr,jg,jb)+"░")
  a = a.replace("G",bg(0,0,0)+" ")
  print (a)
