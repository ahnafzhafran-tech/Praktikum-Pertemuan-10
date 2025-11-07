'''
nama    : Muhammad Ahnaf Zhafran Sultan
kelas   : 1A
NIM     : 2500551
'''


def menu_login_konfirmasi():
    # Data login yang benar sesuai soal
    username = "Ahnaf"
    password = "Kazuki"
    
    #Jumlah maksimal percobaan password
    chance = 3

    print("--- Menu Login SMAN 2 Harapan ---")
    
    #Konfirmasi Username 
    print(f"Username Anda terdeteksi: {username}")

    konfirmasi = input("Apakah username ini benar? (ya/tidak): ").lower().strip()
    
    username_valid = False
    
    if konfirmasi == "ya":
        print("Username dikonfirmasi.")
        username_valid = True
    else:
        # Jika bukan "ya", masuk ke mode input manual
        print("Baik, silakan masukkan username Anda.")
        
        # loop sampai mendapat username yang benar
        while True:
            username_input = input("Masukkan username yang benar: ")
            
            if username_input == username:
                print("Username diterima. Silakan masukkan password.")
                username_valid = True
                break 
            else:
                print("Username salah. Silakan coba lagi.")

    #Password 
    if username_valid:
        for i in range(chance):
            password_input = input(f"Masukkan password (percobaan {i+1} dari {chance}): ")
            
            #jika password benar
            if password_input == password:
                print("\nSelamat, login berhasil!")
                break 
            else:
                print("Password salah.")
                
        # Jika password salah setelah 3 percobaan kali
        else:
            print("---------------------------------")
            print("Anda telah salah memasukkan password 3 kali. Akun diblokir.")

menu_login_konfirmasi()