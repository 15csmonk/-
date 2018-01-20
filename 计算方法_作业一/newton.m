function f=Newton(x,y,x0)
%����֪���ݵ�ľ�����ʽ��ţ�ٲ�ֵ����ʽ
%��֪���ݵ��x����������x
%��֪���ݵ��y����������y
%��ֵ���x���꣺x0
%��õľ�����ʽ��ţ�ٲ�ֵ����ʽ����x0���Ĳ�ֵ��f

syms t;
if(length(x)==length(y))
    n=length(x);
    c(1:n)=0.0;
else
    disp('x��y��ά������ȣ�');
    return;
end  %���

f=y(1);
y1=0;
l=1;

for i=1:n-1
    for j=i+1:n
        y1(j)=(y(j)-y(i))/(x(j)-x(i);
    end
    c(i)=y1(i+1);
    l=l*(t-x(i));
    f=f+c(i)*1;
    simplify(f);
    y=y1;

    if(i==n-1)
        if(nargin==3)
            f=subs(f,'t',x0);%�����ֵ��ĺ���ֵ
        else
            f=collect(f);%����ֵ����ʽչ��
            f=vpa(f,8);%����ֵ����ʽ��ϵ������6λ���ȵ�С��
        end
    end
end
    
        

