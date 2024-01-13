def mul(x,y,arrin,arrout,arrs,s,z):
    """
        x,y : inputs
        arrin : name of array
        arrout : name of output array
        z : pin number
        arrs : select pin array
        s : select pin number
    """
    return f"{arrout}[{z}] = ({arrin}[{x}] & ~{arrs}[{s}])|({arrin}[{y}] & {arrs}[{s}]);"

for i in range(1,5):
    l = 16//(2**(i-1))
    for j in range(0,l,2):
        print(mul(j,j+1,f'p{i-1}',f'p{i}','P',i-1,j//2))
    print()