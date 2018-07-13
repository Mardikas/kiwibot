import sys
sys.path.append('math')

import number

number.subtract(8, 2)

def add(a=0, b=0):
    print(a+b)
    return(a+b)

if __name__ == "__main__":
    import sys
    if len(sys.argv)==3:
        add(float(sys.argv[1]), float(sys.argv[2]))
    else:
        print("nothing given!")
