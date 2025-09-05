% CS362
% HW 1
% Roxanne Lutz
% 8/28/25

clc, clearvars;

% the objective function to minimize
f = [2300, 600]

% exact equivalencies to constrain
Aeq = [];
beq = [];

% less than or equal to amounts to constrainc
A = [
    2300, 600; % this constraint makes it so there are no solutions at all
    -1 -1;
    1, -2;
    -2, 1;
    ];

b = [
    9999.99; % this constraint makes it so there are no solutions at all
    -10;
    0; 
    0; 
    ];

% our bounds, and in this case, we are only sending through 1 unit, so the
% upperbound is just a one vector, the lower is zeros.

lb = zeros(2, 1);
ub = [];

% and, well, let her rip?
sol = linprog(f, A, b, Aeq, beq, lb, ub)
