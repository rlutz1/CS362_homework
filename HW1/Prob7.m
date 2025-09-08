% CS362
% HW 1
% Roxanne Lutz
% 8/28/25

clc, clearvars;

numFams = 3;
famMems1 = 4;
famMems2 = 4;
famMems3 = 6;

% the objective function to minimize
    
f = [-1, -1, -1, ... % P_n
    -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, ... e_k
    -1, -1, -1, -1 ... Q_m
    ];


Aeq = [
    ];
beq = [
    ];

% exact equivalencies to constrain
Aeq = [
    0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, -1, 0, 0, 0;
    0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, -1, 0, 0;
    0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, -1, 0;
    0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, -1;
    ]; 

beq = [
    0;
    0;
    0;
    0;
    ];

% less than or equal to amounts to constrain
A = [
    -1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0;
    0, -1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0;
    0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0;
    ]; 

b = [
    0;
    0;
    0;
    ];

% upperbound is technically nothing, the lower is zeros.
lb = [
    famMems1; famMems2; famMems3; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0;
];
ub = [
    famMems1; famMems2; famMems3; 1; 1; 1; 1; 1; 1; 1; 1; 1; 1; 1; 1; numFams; numFams; numFams; numFams;
    ];

% feed matrices & vectors to lin prog and print solution
sol = linprog(f, A, b, Aeq, beq, lb, ub)

% printing for readability

if (isempty(sol));
    disp("No solution found within constraints");
else;
   
end;
