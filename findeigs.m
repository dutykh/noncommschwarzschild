clear
close all
format longE

M0 = readmatrix('data/M0.mat', 'FileType', 'text');
M1 = readmatrix('data/M1.mat', 'FileType', 'text');
M2 = readmatrix('data/M2.mat', 'FileType', 'text');

e = polyeig(M0, 1i*M1, M2);

figure(1);
plot(real(e), imag(e), 'b.'), grid off
xlabel('Re $\omega$', 'interpreter', 'LaTeX', 'fontsize', 14);
ylabel('Im $\omega$', 'interpreter', 'LaTeX', 'fontsize', 14);
title('Black hole QNMs');
set(gcf, 'color', 'w');