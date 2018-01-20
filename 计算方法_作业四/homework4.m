function  y=homework4(e)
C=[1 2 3 4 5 6 7 8 9 10];
P=poly(C);
for i=1:10
    a(i)=P(11-i+1);%求出a0到a9的值
end
a %打印a0到a9的值
e=1e-2;
P1=P+e;
disp('当e=1e-2时：') 
e=roots(P1)%打印扰动方程的根
e=1e-4;
P1=P+e;
disp('当e=1e-4时：')
e=roots(P1)%打印扰动方程的根
e=1e-6;
P1=P+e;
disp('当e=1e-6时：') 
e=roots(P1) %打印扰动方程的根