sum(A,_,1,A):-
    !.
sum(A,D,N,S):-
    N1 is N-1,
    sum(A,D,N1,S1),
    S is S1+(A+N1*D).
