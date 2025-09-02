% CS362
% HW 1
% Roxanne Lutz
% 8/28/25

clc, clearvars

% the objective function to minimize
f = [2300, 600]

% our constaint matrix
Aeq = [1 1]

% our solution b vector
beq = [10]

% unclear fully as to what these are, so leaving empty for now
A = [
    1, -2;
    -2, 1;
    2300, 600 % this constraint makes it so there are no solutions at all
    ]
b = [
    0; 
    0; 
    10000 % this constraint makes it so there are no solutions at all
    ] 

% our bounds, and in this case, we are only sending through 1 unit, so the
% upperbound is just a one vector, the lower is zeros.
lb = zeros(2, 1)
ub = ones (2, 1) .* 10

% and, well, let her rip?
sol = linprog(f, A, b, Aeq, beq, lb, ub)
