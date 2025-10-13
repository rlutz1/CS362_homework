clc, clearvars

f_capacity = [5, 1, 2, 1, 1, 2, 2, 3];
f_capacity = (-1) .* f_capacity;


lb = [0, 0, 0, 0, 0, 0, 0, 0];
ub = [5, 1, 2, 1, 1, 2, 2, 3];

A = [];
b = [];

Aeq = [[-1, 0, 1, 1, 0, 0, 0, 0],
       [0, 0, -1, 0, 0, 1, 0, 1],
       [0, 1, 0, 0, 0, 1, -1, 0],
       [0, 0, 0, 1, -1, 0, 0, 0]];
beq = [0, 0, 0, 0];

sol = linprog(f_capacity, A, b, Aeq, beq, lb, ub)

disp("got " + (sol(5) + sol(7) + sol(8)) + " units through to t");

% ------------------------------------------------------------

f_cost = [2, 10, 1, 1, 3, 1, 2, 1]; % cost now, arbitrary


lb = [0, 0, 0, 0, 0, 0, 0, 0];
ub = [5, 1, 2, 1, 1, 2, 2, 3];

A = [];
b = [];

Aeq = [[-1, 0, 1, 1, 0, 0, 0, 0],
       [0, 0, -1, 0, 0, 1, 0, 1],
       [0, 1, 0, 0, 0, 1, -1, 0],
       [0, 0, 0, 1, -1, 0, 0, 0],
       [1, 1, 0, 0, 0, 0, 0, 0], % sending through units
       [0, 0, 0, 0, 1, 0, 1, 1]]; % sending through units
beq = [0, 0, 0, 0, 3, 3]; % success
% beq = [0, 0, 0, 0, 4, 4]; % success
% beq = [0, 0, 0, 0, 5, 5]; % FAIL

sol = linprog(f_cost, A, b, Aeq, beq, lb, ub)

disp("got " + (sol(5) + sol(7) + sol(8)) + " units through to t");
