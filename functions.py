# fungsi yang menambahkan arr + element (element di indeks terakhir)
def konso(arr, element):

    len = arr_len(arr)

    temp = ["" for i in range(len+1)]

    for i in range(len):
        temp[i] = arr[i]
    
    temp[len] = element

    return temp

# fungsi yang menambahkan element + arr (element di indeks pertama)
def konsDot(element, arr):

    len = arr_len(arr)

    temp = ["" for i in range(len+1)]

    for i in range(1, len+1):
        temp[i] = arr[i-1]
    
    temp[0] = element

    return temp  

# fungsi yang menggabungkan 2 arr
def konkat(arr1, arr2):
    
    len1 = arr_len(arr1) 
    len2 = arr_len(arr2)

    temp = ["" for i in range(len1+len2)]

    for i in range(len1):
        temp[i] = arr1[i]

    for j in range(len1, len1+len2):
        temp[j] = arr2[j-len1]
        print(temp)

    return temp

# fungsi yang menentukan panjang string
def str_len(string):

    len = 0
    temp = ""

    while temp != string:

        temp += string[len]
        len += 1
    
    return len

# fungsi yang menentukan panjang array
def arr_len(arr):

    tempArr = []
    length =  0

    while tempArr != arr:

        length += 1
        tempArr = [arr[i] for i in range(length)]

    return length

# mengubah format file .csv menjadi array
def convertToArr(file, delimiter):

    data = file.readlines()
    row = arr_len(data)

    if row == 0:
        return []

    column = 1
    for i in range(str_len(data[0])):
        if data[0][i] == delimiter:
            column += 1

    tempArr = [[0 for i in range(column)] for i in range(row)]

    for i in range(row):

        temp = ""
        insert_column = 0

        for j in range(str_len(data[i])):

            if ((data[i][j] != "\n") and (data[i][j] != delimiter)):

                temp += data[i][j]
            
            else:

                tempArr[i][insert_column] = temp

                temp = ""
                insert_column += 1

    tempArr[row-1][column-1] = temp

    return tempArr

# mengubah array menjadi string sesuai format file .csv
def convertToCSV(arr):

    string = ""

    baris = arr_len(arr)
    if baris == 0:
        return string
    
    kolom = arr_len(arr[0])

    for i in range(baris):
        for j in range(kolom):

            string += str(arr[i][j])

            if j != kolom-1:

                string += ";"

        if i != baris-1:
            string += "\n"

    return string

# fungsi isMember
def isMember(element, arr):
    
    for i in range(arr_len(arr)):

        if arr[i] == element:
            return True
        
    return False

def sorting_arr_leks(arr):
    n = arr_len(arr)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr