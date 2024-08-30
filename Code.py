from kandinsky import fill_rect as fr,draw_string as ds
from ion import keydown as kd
from time import sleep as sl,monotonic as mn
from random import randint as rd

clm=['a','b','c','d','e','f','g','h']
ent=lambda n:int(n)if n-int(n)<0.5 else int(n)+1
itfc,slct=(255,181,59),(48,246,49)
c1,c2=(0,85,66),(231,227,206)
n,wh=(54,21,31),(223,175,121)
re,bl=(255,0,0),(0,0,255)
s,ss=27,2
sz=8*s
tl=lambda a,b:216+(104-(len(str(a))+b)*10)//2
ww=wb=0
AIpl=[2]
fen="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
fen=fen.split(' ')
fen[4]=int(fen[4])

s1="000111000;001111100;001111100;001111100;000111000;001111100;000111000;000111000;000111000;001111100;011111110;111111111;111111111"
s2="0011011101100;0011011101100;0011111111100;0011111111100;0001111111000;0001111111000;0001111111000;0001111111000;0001111111000;0001111111000;0011111111100;0111111111110;0011111111100;0111111111110;1111111111111;1111111111111"
s3="00001111000;00011111100;00111111110;01111111110;11111111111;01100111111;00000111111;00001111111;00001111111;00011111110;00011111100;00011111100;00011111100;00111111110;00111111110;01111111111;01111111111"
s4="000010000;000111000;001111100;001111100;000111000;001111100;011111110;000111000;000111000;001111100;001111100;001111100;001111100;011111110;111111111;111111111"
s5="00000100000;00000100000;00011111000;00000100000;00000100000;00001110000;00011111000;00111111100;00111111100;00011111000;00011111000;00011111000;00001110000;00001110000;00011111000;00111111100;00111111100;01111111110;01111111110;01111111110;11111111111;11111111111"
s6="00001110000;00011111000;00011111000;00011111000;00001110000;00011111000;00111111100;00111111100;00011111000;00011111000;00011111000;00001110000;00001110000;00011111000;00111111100;00111111100;01111111110;01111111110;01111111110;11111111111;11111111111"
def d(char):
 rows=char.split(';')
 return[[int(c)for c in row]for row in rows]
p,t,k,b,r,q=d(s1),d(s2),d(s3),d(s4),d(s5),d(s6)
del d,s1,s2,s3,s4,s5,s6

lp=[p,t,k,b,r,q]
def draw(x,y): #Dessin des pièces
 p=dspl[y][x]
 if p==0:return
 c,p=n if p>6 else wh,p%6
 x,y,p=x*s,y*s,lp[p-1]
 dx,dy=(25-len(p[0]))//2+1,(25-len(p))//2+1
 for a in range(len(p)):
  for b in range(len(p[0])):
   if p[a][b]==1:fr(x+b+dx,y+a+dy,1,1,c)

def vm(px,py,vb,vh,bfr): #Enregistrement des mouvements possibles
 if 0<=px<=7 and 0<=py<=7:
  if dspl[py][px]==0:bfr[len(bfr)-1].append([px,py,1])
  elif vb<dspl[py][px]<vh:bfr[len(bfr)-1].append([px,py,2]);return 1
  else:return 1

def pm(x,y,bfr): #Possibilités de mouvements depuis une pièce
 p=dspl[y][x]
 if p==0:return
 if pl==1 and p>6:return
 elif pl==2 and p<7:return
 bfr.append([[x,y]])
 [vb,vh]=[6,13]if 0<p<=6 else[0,7]
 if p in[1,7]: #pawns
  py=y+1 if p==7 else y-1 #Avancer avec le pion
  fn=3 if[p,y]==[7,1]or[p,y]==[1,6]else 2
  for dy in range(1,fn):
   py=y+dy if p==7 else y-dy if p==1 else py
   if dspl[py][x]==0:bfr[len(bfr)-1].append([x,py,1])
   else:break
  py=y+1 if p==7 else y-1 #Manger avec le pion
  for n in[-1,1]:
   px=x+n
   if not 0<=px<=7:continue
   if vb<dspl[py][px]<vh:bfr[len(bfr)-1].append([px,py,2])
   elif clm[px]+str(py)==fen[3]:
     bfr[len(bfr)-1].append([px,py,3])
 if p in[2,8,4,10]: #bishops and rooks
  for d in range(4):
   for n in range(1,8):
    if p in [2,8]:[px,py]=[x,y-n]if d==0 else[x+n,y]if d==1 else[x,y+n]if d==2 else[x-n,y]
    elif p in [4,10]:[px,py]=[x+n,y+n]if d==0 else[x+n,y-n]if d==1 else[x-n,y-n]if d==2 else[x-n,y+n]
    if vm(px,py,vb,vh,bfr)==1:break
 elif p in[3,9]: #knights
  for dx,dy in[(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2)]:
   px,py=x+dx,y+dy
   vm(px,py,vb,vh,bfr)
 elif p in[5,11]: #kings
  for dx in range(-1,2):
   for dy in range(-1,2):
    px,py=x+dx,y+dy
    vm(px,py,vb,vh,bfr)
  if p==11 and 'k'in fen[2]and dspl[0][6]==dspl[0][5]==0:bfr[len(bfr)-1].append([6,0,4])
  if p==11 and 'q'in fen[2]and dspl[0][1]==dspl[0][2]==dspl[0][3]==0:bfr[len(bfr)-1].append([2,0,4])
  if p==5 and 'K'in fen[2]and dspl[7][6]==dspl[7][5]==0:bfr[len(bfr)-1].append([6,7,4])
  if p==5 and 'Q'in fen[2]and dspl[7][1]==dspl[7][2]==dspl[7][3]==0:bfr[len(bfr)-1].append([2,7,4])
 elif p in[6,12]: #queens
  for d in range(8):
   for n in range(1,8):
    [px,py]=[x,y-n]if d==0 else[x+n,y]if d==1 else[x,y+n]if d==2 else[x-n,y]if d==3 else[x+n,y+n]if d==4 else[x+n,y-n]if d==5 else[x-n,y-n]if d==6 else[x-n,y+n]
    if vm(px,py,vb,vh,bfr)==1:break
 if[[x,y]]in bfr:bfr.remove([[x,y]])

def prom(x,y): #Affichage et sélection de la promotion
 newp=True
 xr=0 if y==0 else 3
 def dp(x,y,p,c):
  dx,dy=(25-len(p[0]))//2+1,(25-len(p))//2+1
  for a in range(len(p)):
   for b in range(len(p[0])):
    if p[a][b]==1:fr(x+b+dx,y+a+dy,1,1,c)
 while True:
  if newp:
   newp=False
   if y==0:
    fr(x*s,0,s,4*s,(0,)*3),fr(x*s,xr*s,s,s,slct)
    for i,j in enumerate([5,2,1,3]):dp(x*s,i*s,lp[j],wh)
   else:
    fr(x*s,4*s,s,4*s,(255,)*3),fr(x*s,(xr+4)*s,s,s,slct)
    for i,j in enumerate([3,1,2,5]):dp(x*s,(i+4)*s,lp[j],n)
   sl(0.2)
  if kd(1) and xr>0:xr,newp=xr-1,True
  elif kd(2) and xr<3:xr,newp=xr+1,True
  elif kd(4)or kd(52)or pl in AIpl:
   if y==0:dspl[y][x]=6 if xr==0 else 3 if xr==1 else 2 if xr==2 else 4
   else:dspl[y][x]=12 if xr==3 else 9 if xr==2 else 8 if xr==1 else 10
   for i in range(8):
    fr(x*s,i*s,s,s,f[i][x]),draw(x,i)
   break

def ufc(n): #Update Fen for Castle
 nf,ft="",['K','Q','k','q']
 for p in fen[2]:
  if n==ft.index(p):continue
  elif n==4 and p in[ft[0],ft[1]]:continue
  elif n==5 and p in[ft[2],ft[3]]:continue
  nf+=p
 fen[2]=nf

def ok(): #Actions réalisées lorsqu'on appuie sur ok
 global new,bf,bx,by,vp,ix,pl,sh,pw,pb
 new=True
 if not vp:
  if not dspl[y][x]:return
  for i,pc in enumerate(bf):
   if [pc[0][0],pc[0][1]]==[x,y]:bx,by,vp,ix=x,y,1,i;break
 elif [bx,by]==[x,y]:vp=mp=0;sm(x,y)
 else:
  mp=0
  for mv in bf[ix]:
   if[mv[0],mv[1]]==[x,y]:mp,ch=1,mv[2];break
  if not mp:return
  tk=0
  mep,mrq=1 if ch==3 else 0,1 if ch==4 else 0
  fen[3]=clm[x]+str(y+1 if pl==1 else y-1)if[by,dspl[by][bx],y]in[[1,7,3],[6,1,4]]else'-'
  if mep:
   tk,py=1,y+1 if by==3 else y-1
   dspl[py][x]=0
   fr(x*s,py*s,s,s,f[py][x])
  for i,[a,b,c] in enumerate([[7,7,2],[0,7,2],[7,0,8],[0,0,8],[4,7,5],[4,0,11]]):
   if[bx,by,dspl[by][bx]]==[a,b,c]:ufc(i)
  if mrq:
   [x1,x2]=[5,7]if x==6 else[3,0]
   dspl[by][x1],dspl[by][x2]=dspl[by][x2],0
   fr(x2*s,by*s,s,s,f[by][x2]),draw(x1,by)
  if dspl[y][x]!=0:
   tk,te=1,[0,1,5,3,3,20,8] #table des points des pions mangés
   if dspl[y][x]>6:pw+=te[dspl[y][x]-6]
   elif dspl[y][x]<7:pb+=te[dspl[y][x]]
   for i,[a,b,c] in enumerate([[7,7,2],[0,7,2],[7,0,8],[0,0,8]]):
    if[x,y,dspl[y][x]]==[a,b,c]:ufc(i)
  dspl[y][x],dspl[by][bx],vp,mp=dspl[by][bx],0,0,0
  fr(bx*s,by*s,s,s,f[by][bx])
  if[dspl[y][x],y]in[[1,0],[7,7]]:prom(x,y)
  sh,pl=sh+1 if pl==2 else sh,2 if pl==1 else 1
  ds("Coups:"+str(sh),tl(sh,6),99,bl)
  ds("Points:"+str(pw),tl(pw,7),126,wh),ds("Points:"+str(pb),tl(pb,7),72,n)
  for mv in bf[ix]:fr(mv[0]*s,mv[1]*s,s,s,f[mv[1]][mv[0]]),draw(mv[0],mv[1])
  if cm():pv(tk)

def pv(tk): #Vérifier les positions (pour chercher une égalité)
# global hh
# #Chercher une nulle par répétition
# hh.append([[bx,by],[x,y]])
# if len(hh)==6:
#  rt=True
#  for a,b in[[0,2],[1,3]]:
#   if hh[a]!=hh[b+2]:rt=False;break
#   for c in range(2):
#    if hh[a][c]!=hh[b][1-c]:rt=False;break
#  if rt:tie(1);return
#  else:hh.pop(0)
# #Chercher une nulle si 50 coups sans actions
# if not tk and dspl[y][x]not in[1,7]:fen[4]+=1
# else:fen[4]=0
# if fen[4]==100:tie(2);return
# #Chercher une nulle par manque de matériel
# pn=[0]*13
# for a in range(8):
#  for b in range(8):
#   pn[dspl[b][a]]+=1
# if pn[1]==pn[7]==pn[2]==pn[8]==pn[6]==pn[12]==0:
#  if pn[3]==pn[9]==pn[4]==pn[10]==0:tie(3);return
#  if pn[4]==pn[10]==0 and [pn[3],pn[9]]in[[0,1],[1,0]]:tie(3);return
#  if pn[3]==pn[9]==0 and [pn[4],pn[10]]in[[0,1],[1,0]]:tie(3);return
#  if pn[3]==pn[9]==0 and pn[4]==pn[10]==1:
#   col=0
#   for a in range(8):
#    for b in range(8):
#     if dspl[b][a]in[4,10]:
#      if not col:col=f[b][a]
#      elif f[b][a]==col:tie(3);return
 return 0
def gu(): #Give Up
 fr(0,0,sz,sz,(0,)*3)
 ds("Abandon dans :",sz//2-70,72)
 ds("3",sz//2-5,102)
 ds("Appuyez sur 'clear'",sz//2-95,132)
 ds("pour annuler",sz//2-60,162)
 sl(1)
 rt=mn()+3
 while True:
  ds(str(int(rt-mn())),sz//2-5,102)
  if kd(17):sl(0.3);break
  elif rt-mn()<0:win(pl,2);break
 for a in range(8):
  for b in range(8):
   fr(a*s,b*s,s,s,f[b][a]),draw(a,b)
#def ad(): #Ask Draw
# fr(0,0,sz,sz,(0,)*3)
# ds("Egalité dans :",sz//2-70,72)
# ds("3",sz//2-5,102)
# ds("Appuyez sur 'clear'",sz//2-95,132)
# ds("pour annuler",sz//2-60,162)
# sl(1)
# rt=mn()+3
# while True:
#  ds(str(int(rt-mn())),sz//2-5,102)
#  if kd(17):sl(0.3);break
#  elif rt-mn()<0:tie();break
# for a in range(8):
#  for b in range(8):
#   fr(a*s,b*s,s,s,f[b][a]),draw(a,b)

def win(pl,wc): #Victoire
 if wc!=2:draw(x,y)
 global game,ww,wb
 sl(3),fr(0,0,320,222,(255,)*3)
 if pl==1:wb+=1;winner="noirs"
 if pl==2:ww+=1;winner="blancs"
 ds("Victoire des "+winner+" !",160-(15+len(str(winner)))*5,91)
 if wc==1:ds("(par échec et mat)",70,131)
 if wc==2:ds("(par abandon)",95,131)
 if wc==3:ds("(par hors délai)",80,131)
 sl(5)
 game=False
def tie(wc): #Egalité
 if wc!=4:draw(x,y)
 global game
 sl(3),fr(0,0,320,222,(255,)*3)
 ds("Egalité !",115,51 if wc==5 else 61)
 if wc==1:ds("(par répétition)",80,101)
 if wc==2:ds("(par 50 coups sans action)",20,101)
 if wc==3:ds("(par manque de matériel)",30,101)
 if wc==4:ds("(par accord commun)",95,101)
 if wc==5:ds("(par hors délai",85,91),ds("et manque de matériel)",30,113)
 ds("Personne ne gagne...",60,153 if wc==5 else 141)
 sl(5)
 game=False

def cm(): #Check move / Cherche tous les moves légaux
 global bf,bf2,pl
 bf=[]
 for a in range(8):
  for b in range(8):
   pm(b,a,bf)
 #Chercher une défaite par pat
 if len(bf)==0:win(pl,1);return 1
 if len(bf)==0:tie(4);return 1
 #vérifier moves illégaux
 mr=11 if pl-1 else 5
 pl=3-pl
 tr=[]
 for i,pc in enumerate(bf):
  for cp in pc:
   bf2=[]
   if len(cp)==2:dx,dy=cp[0],cp[1]
   else:
    x,y,ch=cp[0],cp[1],cp[2]
    ppc=dspl[y][x]
    dspl[y][x]=dspl[dy][dx]
    dspl[dy][dx]=0
    for a in range(8):
     for b in range(8):
      pm(b,a,bf2)
    sk=0
    for pc2 in bf2:
     for cp2 in pc2:
      if len(cp2)==2:continue
      if cp2[2]==2 and dspl[cp2[1]][cp2[0]]==mr:tr.append([i,cp]);sk=1
      if ch==4 and([cp2[0],cp2[1]]in[[4,y],[5 if x==6 else 3,y]]):tr.append([i,cp]);sk=1
      if sk:break
     if sk:break
    dspl[dy][dx],dspl[y][x]=dspl[y][x],ppc
 for i,cp in tr:bf[i].remove(cp)
 for i in reversed(range(len(bf))):
  if len(bf[i])==1:bf.remove(bf[i])
 pl=3-pl
 #Chercher une défaite par échec et mat
 if len(bf)==0:win(pl,1);return 1
 return 0

def sm(xm,ym): #Show move
 if vp:
  for pc in bf:
   for n,mv in enumerate(pc):
    px,py=mv[0],mv[1]
    if[bx,by]==[px,py]:continue
    elif n==0:break
    fr(px*s,py*s,s,s,re if mv[2]==2 else bl)
    draw(px,py)
  return
 for i in range(2):
  [x,y]=[xp,yp]if i==0 else[xm,ym]
  p=dspl[y][x]
  if p==0:continue
  if pl==1 and p>6:continue
  elif pl==2 and p<7:continue
  for pc in bf:
   for n,mv in enumerate(pc):
    px,py=mv[0],mv[1]
    if[x,y]==[px,py]:continue
    elif n==0:break
    if i==1:
     if len(mv)!=3:print(pc),print(mv)
     fr(px*s,py*s,s,s,re if mv[2]==2 else bl)
     fr(px*s+ss,py*s+ss,s-ss*2,s-ss*2,f[py][px])
    else:fr(px*s,py*s,s,s,f[py][px])
    draw(px,py)

def dt(): #Affichage du timer
 global pl,tm,tw,tb
 if mn()-tm>=1:
  if pl==1:
   tw-=mn()-tm
   m,s=str(int(tw//60)),str(int(tw%60))
   cl=re if tw<temps/10 else wh
   m,s=str("0"+m)if len(m)==1 else m,str("0"+s)if len(s)==1 else s
   ds(m+":"+s,tl(m+s,1),180,cl)
  elif pl==2:
   tb-=mn()-tm
   m,s=str(int(tb//60)),str(int(tb%60))
   cl=re if tb<temps/10 else n
   m,s=str("0"+m)if len(m)==1 else m,str("0"+s)if len(s)==1 else s
   ds(m+":"+s,tl(m+s,1),18,cl)
  if[m,s]==["00","01"]:
   #Chercher une nulle par hors délai et manque de matériel
   pn=[0]*6
   for a in range(8):
    for b in range(8):
     p=dspl[b][a]
     if p==0:continue
     elif pl==1 and p<7:continue
     elif pl==2 and p>6:continue
     pn[(p-1)%6]+=1
   if pn[0]==pn[1]==pn[5]==0 and[pn[2],pn[3]]in[[1,0],[0,0],[0,1]]:tie(5)
   else:win(pl,3)
  tm=mn()

def eg(game): #extract game (from fen)
 table=[0,'P','R','N','B','K','Q','p','r','n','b','k','q']
 dspl=[]
 rows=game.split('/')
 for i in range(8):
  dspl.append([0]*8)
  n=0
  for p in str(rows[i]):
   if p in table:dspl[i][n]=table.index(p);n+=1
   else:
    for _ in range(int(p)):dspl[i][n]=table[0];n+=1
 return dspl

def AI(): #coup ennemi
 global xp,yp,x,y
 xp,yp=x,y
 num1=rd(0,len(bf)-1)
 x,y=bf[num1][0][0],bf[num1][0][1]
 ok()
 num2=rd(1,len(bf[num1])-1)
 x,y=bf[num1][num2][0],bf[num1][num2][1]
 ok()
 if len(AIpl)!=2:x,y=xp,yp

while True:
 fr(0,0,320,222,itfc)
 f=[[c2]*8 for i in range(8)]
 for a in range(8):
  for b in range(8):
   if (16-a+b)%2==1:f[a][b]=c1
   fr(a*s,b*s,s,s,f[a][b])
 dspl=eg(fen[0])
 pt=['w','b']
 pl=pt.index(fen[1])+1
 del pt
 sh=int(fen[5])
 for a in range(8):
  for b in range(8):
   draw(a,b)
 x,y,xp,yp=0,0,0,0
 vp,mov=0,0
 hh=[]
 temps=600
 tw=tb=temps
 tm=mn()
 pw=pb=0
 ds("Coups:"+str(sh),tl(sh,6),99,bl)
 ds("Points:"+str(pw),tl(pw,7),126,wh),ds("Points:"+str(pb),tl(pw,7),72,n)
 ds("Wins:"+str(ww),tl(ww,5),153,wh),ds("Wins:"+str(wb),tl(ww,5),45,n)
 str1,str2,str3,str4=str(ent(tw//60)),str(ent(tw%60)),str(ent(tb//60)),str(ent(tb%60))
 str1=str("0"+str1)if len(str1)==1 else str1;str2=str("0"+str2)if len(str2)==1 else str2
 str3=str("0"+str3)if len(str3)==1 else str3;str4=str("0"+str4)if len(str4)==1 else str4
 ds(str1+":"+str2,tl(str1+str2,1),180,wh),ds(str3+":"+str4,tl(str3+str4,1),18,n)
 game,new=True,True
 cm()
 while game:
  if new:
   new,mov=False,0
   fr(xp*s,yp*s,s,s,f[yp][xp]),draw(xp,yp)
   sm(x,y)
   fr(x*s,y*s,s,s,slct),fr(x*s+ss,y*s+ss,s-ss*2,s-ss*2,f[y][x]),draw(x,y)
   sl(0.2)
  dt()
  if pl in AIpl:AI()
  if kd(1)and y>0:xp,yp,y,new,mov=x,y,y-1,True,1
  elif kd(2)and y<7:xp,yp,y,new,mov=x,y,y+1,True,1
  if kd(0)and x>0:xp,yp,x,new=x,y if mov==0 else yp,x-1,True
  elif kd(3)and x<7:xp,yp,x,new=x,y if mov==0 else yp,x+1,True
  elif kd(4)or kd(52):ok()
  elif kd(12):gu()
  elif kd(13):ad()
