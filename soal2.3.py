def hitung_pendapatan(gaji_per_jam , jam_kerja):
    # Menghitung pendapatan sebelum pajak
    pendapatan_sebelum_pajak = gaji_per_jam * jam_kerja * 5 

    #hitung pajak
    pajak = 0.14 * pendapatan_sebelum_pajak
    pendapatan_setelah_pajak =  pendapatan_sebelum_pajak - pajak

    #pengeluaran untuk baju dan aksesoris
    pengeluaran_baju_aksesoris = 0.10 * pendapatan_setelah_pajak

    #pengeluaran untuk alat tulis
    pengeluaran_alat_tulis = 0.01 * pendapatan_setelah_pajak

    #jumlah uamg sedekah
    sisa_uang = pendapatan_setelah_pajak - pengeluaran_baju_aksesoris -  pengeluaran_alat_tulis
    sedekah_untuk_yatim = 0.30 * (sisa_uang // 1000)
    sedekah_kaum_dhuafa = (1 - 0.30) * (sisa_uang // 1000)

    return pendapatan_sebelum_pajak, pendapatan_setelah_pajak, pengeluaran_baju_aksesoris, pengeluaran_alat_tulis, sisa_uang, sedekah_untuk_yatim, sedekah_kaum_dhuafa

#input dari user
gaji_per_jam = float(input(" Masukan gaji perjam anda :"))
jam_kerja = float(input(" Masukan jam kerja anda :"))

pendapatan_sebelum_pajak,pendapatan_setelah_pajak,pengeluaran_baju_aksesoris, pengeluaran_alat_tulis,sisa_uang, sedekah_untuk_yatim, sedekah_kaum_dhuafa = hitung_pendapatan(gaji_per_jam, jam_kerja)

print(f"A. pendapatan budi sebelum pajak : Rp {pendapatan_sebelum_pajak : 2f}")
print(f"B. pendapatan budi setelah pajak : Rp {pendapatan_setelah_pajak : 2f}")
print(f"C. pengeluaran untuk baju dan aksesoris : Rp {pengeluaran_baju_aksesoris : 2f}")
print(f"D. pengeluaran alat tulis : Rp {pengeluaran_alat_tulis : 2f}")
print(f"E. jumlah uang yang disedahkan : Rp {sisa_uang : 2f}")
print(f"G. jumlah uang yang akan diterima anak yatim : Rp {sedekah_untuk_yatim : 2f}")
print(f"E. jumlah uang yang akan diterima kaum duafa : Rp {sedekah_kaum_dhuafa : 2f}")