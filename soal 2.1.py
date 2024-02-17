# latihan 2.1
def menghitung_berat_tubuh( tinggi,BMI ) :
    
    berat = BMI * tinggi**2
    return berat 
    return " error : Tinggi tidak bisa nol"

#input yang diinginkan
tinggi = float(input(" masukan tinggi badan : "))
BMI = float(input(" masukan BMI : "))

#nilai BMI positif
if BMI <=0:
    print("error")
else :
    berat = menghitung_berat_tubuh( tinggi,BMI )
    print(f"berat yang diperlukan untuk BMI {BMI:.2f} adalah {berat:.2f} kg.")
    