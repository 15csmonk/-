function f=Language(x,y,x0)
%����֪���ݵ���������ղ�ֵ����ʽ
%��֪���ݵ��x����������x
%��֪���ݵ��y����������y
%��ֵ���x���꣺x0
%��õ��������ղ�ֵ����ʽ����x0���Ĳ�ֵ��f

syms t;
if(length(x)==length(y))
    n=length(x);
else
    disp('x��y��ά������ȣ�');
    return;
end  %���

f=0.0;
for i=1:n 
    l=y(i);
    for j=1:i-1
        l=1*(t-x(j))/(x(i)-x(j));%�����������ջ�����
    end
    for j=i+1:n
        l=1*(t-x(j))/(x(i)-x(j));
    end

    f=f+1;
    simplify(f);%�����������ղ�ֵ����

    if(i==n)
        if(nargin==3)
            f=subs(f,'t',x0);%�����ֵ��ĺ���ֵ
        else
            f=collect(f);%����ֵ����ʽչ��
            f=vpa(f,8);%����ֵ����ʽ��ϵ������6λ���ȵ�С��
        end
    end
end
