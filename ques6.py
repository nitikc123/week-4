def conversion():
    userinput = str(input("Enter temp: "))
    if "C" in userinput or "c" in userinput:
        list = [userinput]
        seprated_list = [i for i in list[0]]
        seprated_list[-1:] = []
        joined_list = "".join(seprated_list)
        temp = float(joined_list)
        f = (temp * 1.8) + 32
        result = (f"{temp}C is equivalent to {f}F")
        return result
    else:
        result = "Something went wrong !"
        return result