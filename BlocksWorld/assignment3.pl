/*  AI PRINCIPLES AND APPLICATIONS - ASSIGNMENT 3: Blocks World
    Group 14
    Program to implement the Blocks' World Problem in Prolog.   

solve_and_display.                                              */

% define blocks in world
blocks([a, b, c, d]).


/*  =========== Define Start and Goal ===========  */

/*
start([[on,a,b],[on,b,table],[on,c,d],[clear,a],[clear,c],[on,d,table]]).
goal([[on,d,a], [on,a,c], [on,c,b], [on,b,table], [clear,d]]).
*/
start([[on,a,c],[on,b,table],[on,c,b],[clear,d],[on,d,a]]).
goal([[on,b,c],[on,a,table],[on,c,table],[on,d,table],[clear,b],[clear,a],[clear,d]]).


/*  ---------- Helpers ---------- */

% block X as member of blocks
block(X) :-
    blocks(BLOCKS),
    member(X, BLOCKS).

% --- not equal
notequal(X, X) :- !, fail.
notequal(_, _).

% --- substitute an element in a list
substitute(X, Y, [X|T], [Y|T]).
substitute(X, Y, [H|T], [H|T1]) :-
    substitute(X, Y, T, T1).


/*  ---------- Move ---------- */

% --- move
% move X from Y to Z (X, Y, Z are blocks. S1, S2 are states)
move(X, Y, Z, S1, S2):-
    member([clear, X], S1),                 % find a clear block X in S1
    member([on, X, Y], S1), block(Y),       % find a block on which X sits
    member([clear, Z], S1), notequal(X, Z), % find another clear block, Z
    write('Move '), write(X), write(' from '), write(Y), write(' to '), write(Z), nl,
    substitute([on, X, Y], [on, X, Z], S1, INT),    % remove X from Y, place it on Z
    substitute([clear, Z], [clear, Y], INT, S2).    % Z is no longer clear; Y is now clear

% --- move: from block to table
move(X, Y, table, S1, S2) :-
    member([clear, X], S1),
    member([on, X, Y], S1), block(Y),
    write('Move '), write(X), write(' from '), write(Y), write(' to table'), nl,
    substitute([on, X, Y], [on, X, table], S1, INT),    % remove X from Y, place X on table
    append([[clear, Y]], INT, S2).                      % Y is now clear

% --- move: from table to block
move(X, table, Y, S1, S2) :-
    member([clear, X], S1),
    member([on, X, table], S1), block(Y),
    member([clear, Y], S1), notequal(X, Y), % find another clear block, Y
    write('Move '), write(X), write(' from table to '), write(Y), nl,
    substitute([on, X, table], [on, X, Y], S1, INT),
    select([clear, Y], INT, S2).            % Y is no longer clear


/*  ---------- Search ---------- */

% goal permutations to compare
goalCheck(State) :-
    goal(GoalState),
    permutation(State, GoalState).

% connectivity between states
path(S1, S2) :- move(_, _, _, S1, S2).
connect(S1, S2) :- path(S1, S2).
%connect(S1, S2) :- path(S2, S1).   

% --- ensure state has not been visited
% checks permutations to treat list as set
notYetVisited(State, PathSoFar) :-
    \+ (member(VisitedState, PathSoFar), permutation(State, VisitedState)).

% --- depth-first search
depthFirst(X, [X], _, 1):- goalCheck(X), !.         % base case: goal check
depthFirst(X, [X|Ypath], VISITED, PathLength):-     % recursive case
    connect(X, Y),
    notYetVisited(Y, VISITED),
    depthFirst(Y, Ypath, [Y|VISITED], SubPathLength),
    PathLength is SubPathLength + 1.


/*  ---------- Solve and Print ---------- */

% --- solve with visit count and path length
solve(Path, PathLength) :-
    start(S),
    depthFirst(S, Path, [S], PathLength).

% --- show path with newlines for each state
printPath([]).
printPath([H|T]) :-
    write(H), write(','), nl,
    printPath(T).

% --- solve and display results
solve_and_display :-
    solve(Path, PathLength),
    write('Path:'), nl,
    printPath(Path),
    write('Path Length: '), write(PathLength), nl.

