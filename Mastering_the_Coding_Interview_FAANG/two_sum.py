def two_sum(ls=None, sum=0) -> list:
    if ls == None:
        return None
    
    # key = sum - num
    # value = index
    sum_map = {}


    for index, num in enumerate(ls):
        if (sum - num) in sum_map.keys():
            print(f"{sum_map[num]} {index}")
        else:
            print(f"{sum} is not in sum_map" )
            sum_map[num] = index
        print(sum_map)
        print()

    return None
        



def main():
    ls = [1,2,3,4,5,6]

    num = 11

    two_sum(ls, num)

if __name__ == "__main__":
    main()