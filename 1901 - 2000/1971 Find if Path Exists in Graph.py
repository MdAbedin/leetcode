class Solution:
 def validPath(q,n,E,s,d):return[P:=list(range(n)),S:=P.__setitem__,F:=lambda x:[S(x,F(P[x])),P[x]][1]if P[x]!=x else P[x],U:=lambda x,y:S(F(x),F(y)),list(starmap(U,E)),F(s)==F(d)][-1]
