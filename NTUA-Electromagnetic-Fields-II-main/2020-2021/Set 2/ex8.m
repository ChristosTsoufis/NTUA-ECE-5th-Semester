clear;
a = 0.005; L = 0.99; h = 1; D = 1.5;
N = 3; V = 1; s0 = 1/160;
Font = 12; I = 500;

Dz = L/N; Dx = D/N;
x = - (0.5)*D:Dx:(0.5)*D;
z = -h-a-L:Dz:-h-a;

for i=1:N
  x(i) = (1/2)*( x(i) + x(i+1) );
  z(i) = (1/2)*( z(i) + z(i+1) );
  z_mirror(i) = -(1/2)*( z(i) + z(i+1) );
endfor

% VDF calculation
for i=1:N
  for j=1:3*N
    if i==j
      R1 = sqrt((Dz/2)^2 + a^2) + (Dz/2);
      R2 = sqrt((Dz/2)^2 + a^2) + -(Dz/2);
      R3 = abs(z(i) - z_mirror(j));
      VDF(i, j) = log(R1/R2) + (Dz/R2);
      
    else if j<N+1
      R1 = abs(z(i) - z(j));
      R2 = abs(z(i) - z_mirror(j));
      VDF(i, j) = Dz/R1 + Dz/R2;
      
    else if j<2*N+1
      R1 = sqrt((z(i) + h)^2 + (-D/2 + a - x(j-N))^2);
      R2 = sqrt((z(i) - h)^2 + (-D/2 + a - x(j-N))^2);
      VDF(i, j) = Dx/R1 + Dx/R2;
      
    else if j<3*N+1
      R1 = sqrt((z(i) - z(j-2*N))^2 + (D - 2*a)^2);
      R2 = sqrt((z(i) - z_mirror(j-2*N))^2 + (D - 2*a)^2);
      VDF(i, j) = Dz/R1 + Dz/R2;
    endif
    endif
    endif
    endif
  endfor
endfor
