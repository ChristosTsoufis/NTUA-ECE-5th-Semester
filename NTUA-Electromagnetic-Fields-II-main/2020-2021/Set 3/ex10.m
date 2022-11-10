clear;

a = 1;
M0 = 1;
nfig = 1;
Npoints = 250;
xmin = -3*a;
ymin = -3*a;
xmax = 3*a;
ymax = 3*a;

xx = xmin: (xmax-xmin) / Npoints:xmax;
yy = ymin: (ymax-ymin) / Npoints:ymax;
[X, Y] = meshgrid(xx, yy);
cont = [-0.9:0.1:0.9];

for ix = 1:length(xx)
    for iy = 1:length(yy)
        x0 = X(ix,iy);
        y0 = Y(ix,iy);
       rt = sqrt(x0^2+y0^2);
       if x0 > 0 & y0 >= 0 
       f = atan(y0/x0);
       else if x0 <= 0 
        f = pi + atan(y0/x0);
           else if x0 > 0 & y0 < 0
         f = 2*pi+atan(y0/x0);
               end
           end
       end
       if ix == (Npoints/2+1) & iy == (Npoints/2+1)
           Az(ix,iy) = 0;
       else if rt < 3*a
       A1 = @(f1) cos(f1)*log(a/sqrt([rt^2+a^2-2*rt*a*cos(f-f1)]));
       %Hx= @(f1) [(y0-a*sin(f1))*cos(f1)]/[rt^2+a^2-2*rt*a*cos(f-f1)];
       %Hy= @(f1) [(x0-a*cos(f1))*cos(f1)]/[rt^2+a^2-2*rt*a*cos(f-f1)];
       Az(ix,iy) = -a*integral(@(f1)A1(f1), 0, 2*pi, 'Arrayvalued', 1);
          else
         Az(ix,iy) = nan;
           end
       end
       if ix == (Npoints/2+1) & iy == (Npoints/2+1)
           Hxx(ix,iy) = 0;
           Hyy(ix,iy) = 0;
       else 
       Hx = @(f1) [(y0-a*sin(f1))*cos(f1)]/[rt^2+a^2-2*rt*a*cos(f-f1)];
       Hy = @(f1) [(x0-a*cos(f1))*cos(f1)]/[rt^2+a^2-2*rt*a*cos(f-f1)];
       Hxx(ix,iy) = a*integral(@(f1)Hx(f1), 0, 2*pi, 'Arrayvalued', 1);
       Hyy(ix,iy) = -a*integral(@(f1)Hy(f1), 0, 2*pi, 'Arrayvalued', 1);
       if rt <= a
        Bxx(ix,iy) = Hxx(ix,iy);
        Byy(ix,iy) = Hyy(ix,iy)-M0;
       else if rt > a
        Bxx(ix,iy) = Hxx(ix,iy);
        Byy(ix,iy) = Hyy(ix,iy);
           end
       end
       end
    end
end

t = Npoints/2+1;
Az(t,t) = 0;
figure(nfig);
surface(X,Y,Az) , shading interp
hold on
colorbar
xlabel('x(m)','Fontsize',12,'FontWeight','bold')
ylabel('y(m)','Fontsize',12,'FontWeight','bold')
title(['Vector Potential Az(x,y)'],'Fontsize',10,'FontWeight','bold','Color','c')
hold off

nfig = nfig + 1;
figure(nfig);
[CS,H] = contour(X,Y,Az,cont,'Linewidth',1,'Color','c');
clabel(CS,H,cont);
xlabel('x(m)','Fontsize',12,'FontWeight','bold')
ylabel('y(m)','Fontsize',12,'FontWeight','bold')
title(['Vector Potential Az(x,y)'],'Fontsize',10,'FontWeight','bold','Color','c')

nfig = nfig + 1;
figure(nfig);
streamslice(X,Y,Bxx,Byy)
hold on 
xlabel('x','Fontsize',12,'FontWeight','bold')
ylabel('y','Fontsize',12,'FontWeight','bold')
title('Magnetic Induction B(x,y) a=1 M0=1', 'Fontsize',10,'FontWeight','bold')
quiver(X,Y,Bxx,Byy);
hold off

nfig = nfig + 1;
figure(nfig);
streamslice(X,Y,Hxx,Hyy)
hold on 
xlabel('x','Fontsize',12,'FontWeight','bold')
ylabel('y','Fontsize',12,'FontWeight','bold')
title('Magnetic Field H(x,y) a=1 M0=1', 'Fontsize',10,'FontWeight','bold')
quiver(X,Y,Hxx,Hyy);
hold off