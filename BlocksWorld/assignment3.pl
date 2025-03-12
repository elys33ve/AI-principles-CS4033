/*  AI PRINCIPLES AND APPLICATIONS - ASSIGNMENT 3: Blocks World
    Group 14
    Program to implement the Blocks' World Problem in Prolog.   */

% define blocks in world
blocks([a, b, c, d]).

% block X as member of blocks
block(X) :-
    blocks(BLOCKS),
    member(X, BLOCKS).


/*  =========== Start and Goal ===========  */

% goal permutations to compare
goal(State) :-
    actual_goal(GoalState),
    permutation(State, GoalState).


start([[on,a,b],[on,b,table],[on,c,d],[clear,a],[clear,c],[on,d,table]]).
actual_goal([[on,d,a], [on,a,c], [on,c,b], [on,b,table], [clear,d]]).


/*  ---------- Helpers ---------- */

% --- not equal
notequal(X, X) :- !, fail.
notequal(_, _).

% --- substitute an element in a list
substitute(X, Y, [X|T], [Y|T]).
substitute(X, Y, [H|T], [H|T1]) :-
    substitute(X, Y, T, T1).


/*  ---------- move ---------- */

% --- move
% move X from Y to Z (X, Y, Z are blocks. S1, S2 are states)
move(X, Y, Z, S1, S2):-
    member([clear, X], S1),                 % find a clear block X in S1
    member([on, X, Y], S1), block(Y),       % find a block on which X sits
    member([clear, Z], S1), notequal(X, Z), % find another clear block, Z
    %write('Move '), write(X), write(' from '), write(Y), write(' to '), write(Z), nl,
    substitute([on, X, Y], [on, X, Z], S1, INT),    % remove X from Y, place it on Z
    substitute([clear, Z], [clear, Y], INT, S2).    % Z is no longer clear; Y is now clear

% --- move: from block to table
move(X, Y, table, S1, S2) :-
    member([clear, X], S1),
    member([on, X, Y], S1), block(Y),
    %write('Move '), write(X), write(' from '), write(Y), write(' to table'), nl,
    substitute([on, X, Y], [on, X, table], S1, INT),    % remove X from Y, place X on table
    append([[clear, Y]], INT, S2).                      % Y is now clear

% --- move: from table to block
move(X, table, Y, S1, S2) :-
    member([clear, X], S1),
    member([on, X, table], S1), block(Y),
    member([clear, Y], S1), notequal(X, Y), % find another clear block, Y
    %write('Move '), write(X), write(' from table to '), write(Y), nl,
    substitute([on, X, table], [on, X, Y], S1, INT),
    select([clear, Y], INT, S2).            % Y is no longer clear


/*  ---------- search ---------- */

% connectivity between states
path(S1, S2) :- move(_, _, _, S1, S2).
connect(S1, S2) :- path(S1, S2).
%connect(S1, S2) :- path(S2, S1).

% --- ensure state has not been visited
% checks permutations to treat list as set
notYetVisited(State, PathSoFar) :-
    \+ (member(VisitedState, PathSoFar), permutation(State, VisitedState)).

% --- depth-first search with visit count and path length
depthFirst(X, [X], _, 0, 1):- goal(X), !.                       % base case: goal check
depthFirst(X, [X|Ypath], VISITED, PathLength, VisitCount):-     % recursive case
    connect(X, Y),
    notYetVisited(Y, VISITED),
    depthFirst(Y, Ypath, [Y|VISITED], SubPathLength, SubVisitCount),
    PathLength is SubPathLength + 1,
    VisitCount is SubVisitCount + 1.


/*  ---------- solve and print ---------- */

% --- solve with visit count and path length
solve(Path, PathLength, VisitCount) :-
    start(S),
    depthFirst(S, Path, [S], PathLength, VisitCount).

% --- show path (newlines for each state)
print_path([]).
print_path([H|T]) :-
    write(H), write(','),
    nl,
    print_path(T).

% --- solve and display results
solve_and_display :-
    solve(Path, PathLength, VisitCount),
    write('Path:'), nl,
    print_path(Path),
    write('Path Length: '), write(PathLength), nl,
    write('Visit Count: '), write(VisitCount), nl.