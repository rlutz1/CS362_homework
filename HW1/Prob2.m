% CS362
% HW 1
% Roxanne Lutz
% 8/28/25

clc, clearvars;

% the objective function to minimize
f = [2300, 600];

% exact equivalencies to constrain
Aeq = [];
beq = [];

% less than or equal to amounts to constrain
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

% upperbound is technically nothing, the lower is zeros.
lb = ones(2, 1);
ub = [];

% feed matrices & vectors to lin prog and print solution
sol = linprog(f, A, b, Aeq, beq, lb, ub)

% printing for readability

if (isempty(sol));
    disp("No solution found within constraints");
else;
    disp("From Dell at $2300 each: " + sol(1));
    disp("From Apple at $600 each: " + sol(2));
end;
