def delete_nth(order,max_e):
    res_lst = []
    for elem in order:
        if res_lst.count(elem)< max_e:
            res_lst.append(elem)
    return res_lst


print(delete_nth([20,37,20,21], 1)) #[20,37,21]
print(delete_nth([1,1,3,3,7,2,2,2,2], 3)) #[1, 1, 3, 3, 7, 2, 2, 2]