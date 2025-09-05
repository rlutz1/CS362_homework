% CS362
% HW 1
% Roxanne Lutz
% 8/28/25

clc, clearvars

% the objective function to minimize
f = [8, 6, 1, 3, 5, 1, 4, 3];

% exact equivalencies to constrain
Aeq = [
    1, 1, 0, 0, 0, 0, 0, 0;
    0, 0, 0, 0, 0, 1, 1, 1;
    -1, 0, 1, 1, 0, 0, 0, 0;
    0, 0, -1, 0, 0, 1, 0, 0;
    0, 0, 0, -1, 1, 0, 0, 1;
    0, -1, 0, 0, -1, 0, 1, 0
];

beq = [
    1; 
    1; 
    0; 
    0; 
    0; 
    0
    ];

% less than or equal to amounts to constrain
A = [];
b = []; 

% our bounds, and in this case, we are only sending through 1 unit, so the
% upperbound is just a one vector, the lower is zeros.
lb = zeros(8, 1);
ub = ones(8, 1);

% feed matrices & vectors to lin prog and print solution
sol = linprog(f, A, b, Aeq, beq, lb, ub)

% printing for readability
counter = 1;

disp("Ideal path found:");

for i = transpose(sol);
    
    if (i == 1);
        disp("X_" + counter);
    end;

    counter = counter + 1;

end;
