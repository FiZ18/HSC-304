def HPP(p, vcu, fc) :
    hpp = fc / (p - vcu)
    return hpp

def var_cost(vc1, c):
    vcu = vc1/c
    return vcu

def main():
    p = float(input("enter the price :"))
    vc1 = float(input("enter the variable cost :"))
    c = float(input("enter the items number:"))

    vcu = var_cost(vc1, c)
    hpp = HPP(p, vcu, c)
    print(f"hppnya adalah {hpp}")
main()
