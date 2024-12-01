syms z;
c = -0.7 + 0.3i; 
f = z^2 + c; 

n = 1; % Desired period
f_n = f; % Start with f(z)
for k = 2:n
    f_n = subs(f, z, f_n); % Substitute f(z) into itself iteratively
end

F_n = f_n - z;

roots = vpa(solve(F_n, z));

disp('Roots (Periodic Points):');
disp(roots);

