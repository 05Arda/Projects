import math

def __main__():
    # I know that numpy has a quantile function init, 
    # but I wanted to make the problem a little more challenging.
    def quantile(data: list, q: float) -> float:
        data = sorted(data)
        n = len(data)

        index = q * (n-1)

        if index.is_integer():
            return data[int(index)]
        
        #Interpolation
        lowerIndex = math.floor(index)
        lowerVal, upperVal = data[lowerIndex], data[math.ceil(index)]
        fraction = index - lowerIndex
        
        return (1-fraction) * lowerVal + fraction * upperVal
    

    def quartileDeviation(a: float, b: float) -> float:
        return abs(a-b)/2


    data = list(range(20, 100, 5))
    q1 = quantile(data, 0.25)
    q3 = quantile(data, 0.75)

    print(quartileDeviation(q1, q3))
    

if __name__ == "__main__":
    __main__()