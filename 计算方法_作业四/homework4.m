function  y=homework4(e)
C=[1 2 3 4 5 6 7 8 9 10];
P=poly(C);
for i=1:10
    a(i)=P(11-i+1);%���a0��a9��ֵ
end
a %��ӡa0��a9��ֵ
e=1e-2;
P1=P+e;
disp('��e=1e-2ʱ��') 
e=roots(P1)%��ӡ�Ŷ����̵ĸ�
e=1e-4;
P1=P+e;
disp('��e=1e-4ʱ��')
e=roots(P1)%��ӡ�Ŷ����̵ĸ�
e=1e-6;
P1=P+e;
disp('��e=1e-6ʱ��') 
e=roots(P1) %��ӡ�Ŷ����̵ĸ�