import pandas as pd

# Fungsi untuk membaca data dari file Excel
def read_excel(file_path):
    return pd.read_excel(file_path)

# Fungsi untuk menghitung probabilitas Naive Bayes
def naive_bayes(data, target_column):
    probabilities = {}
    total_count = len(data)
    for target in data[target_column].unique():
        probabilities[target] = len(data[data[target_column] == target]) / total_count
    return probabilities

# Fungsi untuk normalisasi Z-Score
def z_score_normalization(data):
    if not pd.api.types.is_numeric_dtype(data):
        raise ValueError("Kolom harus berisi nilai numerik.")
    mean = data.mean()
    std_dev = data.std()
    return (data - mean) / std_dev

# Fungsi untuk menampilkan menu
def display_menu():
    print("\nMenu:")
    print("1. Baca Data dari Excel")
    print("2. Hitung Probabilitas Naive Bayes")
    print("3. Normalisasi Data")
    print("4. Keluar")

# Fungsi utama
def main():
    while True:
        display_menu()
        choice = input("Pilih opsi (1-4): ").strip()

        if choice == '1':
            file_path = input("Masukkan path file Excel: ").strip()
            data = read_excel(file_path)
            print("Data berhasil dibaca:")
            print(data.head())  # Menampilkan 5 baris pertama dari data

        elif choice == '2':
            target_column = input("Masukkan nama kolom target: ")
            probabilities = naive_bayes(data, target_column)
            print("Probabilitas Naive Bayes:", probabilities)

        elif choice == '3':
            target_column = input("Masukkan nama kolom target untuk normalisasi: ")
            if target_column not in data.columns:
                print("Kolom tidak ditemukan dalam data.")
                continue  # Kembali ke menu jika kolom tidak ada
            if not pd.api.types.is_numeric_dtype(data[target_column]):
                print("Kolom harus berisi nilai numerik.")
                continue  # Kembali ke menu jika kolom tidak numerik
            normalized_data = data.copy()
            for column in data.columns:
                if column != target_column:
                    normalized_data[column] = z_score_normalization(data[column])
            output_file = input("Masukkan nama file output untuk menyimpan data normalisasi: ")
            normalized_data.to_excel(output_file, index=False)
            print(f"Hasil normalisasi telah disimpan ke {output_file}")

        elif choice == '4':
            print("Keluar dari program.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Menjalankan fungsi utama
if __name__ == "__main__":
    main()
