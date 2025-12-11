from model.product import ProductModel

class MenuHandler:
    def __init__(self):
        self.model = ProductModel()

    def print_products(self):
        data = self.model.get_all()

        if not data:
            print("\nTidak ada data produk.\n")
            return

        print("\n=== DAFTAR PRODUK ===")
        print("-" * 65)
        print(f"{'ID':<5} {'Nama':<20} {'Kategori':<15} {'Harga':<10} {'Stok':<5}")
        print("-" * 65)

        for row in data:
            print(f"{row[0]:<5} {row[1]:<20} {row[2]:<15} {row[3]:<10} {row[4]:<5}")

        print("-" * 65)

    def add_product(self):
        print("\n=== TAMBAH PRODUK ===")
        name = input("Nama: ")
        category = input("Kategori: ")
        price = float(input("Harga: "))
        stock = int(input("Stok: "))

        self.model.add_product(name, category, price, stock)
        print("Produk berhasil ditambahkan!\n")

    def update_product(self):
        self.print_products()
        product_id = int(input("Masukkan ID produk yang akan diupdate: "))

        product = self.model.get_by_id(product_id)
        if not product:
            print("ID tidak ditemukan.\n")
            return

        print("\nTekan Enter untuk mempertahankan data lama:")
        name = input(f"Nama [{product[1]}]: ") or product[1]
        category = input(f"Kategori [{product[2]}]: ") or product[2]

        price_in = input(f"Harga [{product[3]}]: ")
        price = float(price_in) if price_in else product[3]

        stock_in = input(f"Stok [{product[4]}]: ")
        stock = int(stock_in) if stock_in else product[4]

        self.model.update_product(product_id, name, category, price, stock)
        print("Produk berhasil diperbarui!\n")

    def delete_product(self):
        self.print_products()
        product_id = int(input("Masukkan ID produk yang ingin dihapus: "))

        product = self.model.get_by_id(product_id)
        if not product:
            print("ID tidak ditemukan.\n")
            return

        confirm = input("Apakah yakin ingin menghapus? (y/n): ").lower()
        if confirm == "y":
            self.model.delete_product(product_id)
            print("Produk berhasil dihapus!\n")
        else:
            print("Penghapusan dibatalkan.\n")

    def show_menu(self):
        while True:
            print("""
==== FOOD & BEVERAGE ====
1. Tambah Produk
2. Lihat Produk
3. Update Produk
4. Hapus Produk
5. Keluar
""")

            choice = input("Pilih menu: ")

            if choice == "1":
                self.add_product()
            elif choice == "2":
                self.print_products()
            elif choice == "3":
                self.update_product()
            elif choice == "4":
                self.delete_product()
            elif choice == "5":
                print("Program selesai.")
                break
            else:
                print("Pilihan tidak valid!\n")
