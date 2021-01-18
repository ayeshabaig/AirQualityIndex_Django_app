def ultimate_analysis(analyze_list):
    sum = analyze_list[0]
    min = analyze_list[0]
    max = analyze_list[0]
    for i in range(1, len(analyze_list), 1):
        sum += analyze_list[i]
        if analyze_list[i]<min:
            min=analyze_list[i]
        if analyze_list[i]>max:
            max=analyze_list[i]
    return{
        'sumTotal': sum,
        'average': sum/len(analyze_list),
        'min': min,
        'max': max,
        'length' : len(analyze_list)




    }
print(ultimate_analysis([37,2,1,-9]))
