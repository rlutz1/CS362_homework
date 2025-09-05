% CS362
% HW 1
% Roxanne Lutz
% 8/28/25

clc, clearvars

% the objective function to minimize
f = [8, 6, 1, 3, 5, 1, 4, 3]

% our constaint matrix
Aeq = [
    1, 1, 0, 0, 0, 0, 0, 0;
    0, 0, 0, 0, 0, 1, 1, 1;
    -1, 0, 1, 1, 0, 0, 0, 0;
    0, 0, -1, 0, 0, 1, 0, 0;
    0, 0, 0, -1, 1, 0, 0, 1;
    0, -1, 0, 0, -1, 0, 1, 0
]

% our solution b vector
beq = [1; 1; 0; 0; 0; 0]

% unclear fully as to what these are, so leaving empty for now
A = []
b = [] 

% our bounds, and in this case, we are only sending through 1 unit, so the
% upperbound is just a one vector, the lower is zeros.
lb = zeros(8, 1)
ub = ones (8, 1)

% and, well, let her rip?
sol = linprog(f, A, b, Aeq, beq, lb, ub)
