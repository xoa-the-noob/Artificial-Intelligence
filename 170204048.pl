%%%Goal state
gtp(1,1,1). gtp(2,2,1). gtp(3,3,1). gtp(4,1,2).
gtp(5,2,2). gtp(6,3,2). gtp(7,2,3). gtp(8,3,3). gblnk(1,3).
%%%Current state
tp(1,1,3). tp(2,2,3). tp(3,3,3). tp(4,3,2).
tp(5,2,2). tp(6,1,2). tp(7,2,1). tp(8,1,1). blnk(3,1).

go:-
    calcH(1,0,H),write('Heuristics:'),write(H).

calcH(9,X,X):-
    !.
calcH(T,X,Y):-
    check(T,V), X1 is X+V, T1 is T+1, calcH(T1,X1,Y).
check(T,V):-
    tp(T,A,B),gtp(T,C,D), A=C, B=D, V is 0,!.
check(_,1):-
    !.
