from collections import deque
import time
import os

# ============================================================
#   SISTEM LAYANAN RESTORAN CEPAT SAJI
#   Menggunakan Struktur Data: DEQUE (Double-Ended Queue)
#   Mata Kuliah: Struktur Data & Algoritma
# ============================================================

class RestoranCepatSaji:
    def __init__(self, nama_restoran="FastFood Express"):
        self.nama = nama_restoran
        self.antrian = deque()          # Deque utama untuk antrian pesanan
        self.riwayat_selesai = []       # Menyimpan pesanan yang sudah diproses
        self.nomor_antrian = 0          # Counter nomor antrian

    def tampilkan_header(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=" * 60)
        print(f"   🍔  {self.nama}  🍔")
        print("   Sistem Manajemen Antrian Pesanan")
        print("=" * 60)

    # ----------------------------------------------------------
    # ENQUEUE BELAKANG: Pelanggan biasa masuk antrian normal
    # Menggunakan: deque.append() → O(1)
    # ----------------------------------------------------------
    def tambah_pelanggan_biasa(self, nama, pesanan):
        self.nomor_antrian += 1
        data_pesanan = {
            "no": self.nomor_antrian,
            "nama": nama,
            "pesanan": pesanan,
            "tipe": "Biasa",
            "waktu": time.strftime("%H:%M:%S")
        }
        self.antrian.append(data_pesanan)   # Masuk dari BELAKANG
        print(f"\n  ✅ Pelanggan '{nama}' masuk antrian normal (No. {self.nomor_antrian})")
        print(f"     Pesanan: {pesanan}")

    # ----------------------------------------------------------
    # ENQUEUE DEPAN: Pelanggan VIP diprioritaskan
    # Menggunakan: deque.appendleft() → O(1)
    # ----------------------------------------------------------
    def tambah_pelanggan_vip(self, nama, pesanan):
        self.nomor_antrian += 1
        data_pesanan = {
            "no": self.nomor_antrian,
            "nama": nama,
            "pesanan": pesanan,
            "tipe": "VIP ⭐",
            "waktu": time.strftime("%H:%M:%S")
        }
        self.antrian.appendleft(data_pesanan)   # Masuk dari DEPAN (prioritas)
        print(f"\n  ⭐ Pelanggan VIP '{nama}' diprioritaskan ke depan antrian (No. {self.nomor_antrian})")
        print(f"     Pesanan: {pesanan}")

    # ----------------------------------------------------------
    # UNDO / BATALKAN PESANAN TERAKHIR
    # Menggunakan: deque.pop() → O(1)
    # ----------------------------------------------------------
    def batalkan_pesanan(self):
        if not self.antrian:
            print("\n  ⚠️  Tidak ada pesanan dalam antrian.")
            return

        pesanan_dibatalkan = self.antrian.pop()  # Hapus dari BELAKANG
        print(f"\n  ❌ Pesanan dibatalkan!")
        print(f"     Nama  : {pesanan_dibatalkan['nama']}")
        print(f"     Pesan : {pesanan_dibatalkan['pesanan']}")
        print(f"     Tipe  : {pesanan_dibatalkan['tipe']}")

    # ----------------------------------------------------------
    # PROSES PESANAN (Dapur memasak)
    # Menggunakan: deque.popleft() → O(1)
    # ----------------------------------------------------------
    def proses_pesanan(self):
        if not self.antrian:
            print("\n  ⚠️  Antrian kosong. Tidak ada pesanan untuk diproses.")
            return

        pesanan = self.antrian.popleft()    # Ambil dari DEPAN (FIFO)
        pesanan["status"] = "Selesai ✅"
        pesanan["waktu_selesai"] = time.strftime("%H:%M:%S")
        self.riwayat_selesai.append(pesanan)

        print(f"\n  👨‍🍳 Dapur memproses pesanan...")
        print(f"     No Antrian : {pesanan['no']}")
        print(f"     Nama       : {pesanan['nama']} ({pesanan['tipe']})")
        print(f"     Pesanan    : {pesanan['pesanan']}")
        print(f"     Status     : Pesanan siap! 🍽️")

    # ----------------------------------------------------------
    # LIHAT ANTRIAN SAAT INI
    # ----------------------------------------------------------
    def tampilkan_antrian(self):
        print("\n" + "─" * 60)
        print("  📋 ANTRIAN SAAT INI:")
        if not self.antrian:
            print("     (Antrian kosong)")
        else:
            print(f"     Total: {len(self.antrian)} pesanan\n")
            print(f"     {'No.':<5} {'Nama':<15} {'Tipe':<10} {'Pesanan':<20} {'Waktu'}")
            print(f"     {'─'*65}")
            for i, p in enumerate(self.antrian):
                posisi = "← DEPAN" if i == 0 else ("← BELAKANG" if i == len(self.antrian)-1 else "")
                print(f"     {p['no']:<5} {p['nama']:<15} {p['tipe']:<10} {p['pesanan']:<20} {p['waktu']} {posisi}")
        print("─" * 60)

    # ----------------------------------------------------------
    # LIHAT RIWAYAT PESANAN SELESAI
    # ----------------------------------------------------------
    def tampilkan_riwayat(self):
        print("\n" + "─" * 60)
        print("  📜 RIWAYAT PESANAN SELESAI:")
        if not self.riwayat_selesai:
            print("     (Belum ada pesanan yang selesai)")
        else:
            for p in self.riwayat_selesai:
                print(f"     [{p['waktu_selesai']}] No.{p['no']} - {p['nama']} : {p['pesanan']} ✅")
        print("─" * 60)

    # ----------------------------------------------------------
    # CEK APAKAH ANTRIAN KOSONG
    # ----------------------------------------------------------
    def antrian_kosong(self):
        return len(self.antrian) == 0

    # ----------------------------------------------------------
    # MENU UTAMA (MAIN LOOP)
    # ----------------------------------------------------------
    def jalankan(self):
        while True:
            self.tampilkan_header()
            self.tampilkan_antrian()

            print("\n  MENU:")
            print("  1. Tambah pelanggan BIASA")
            print("  2. Tambah pelanggan VIP (prioritas)")
            print("  3. Batalkan pesanan terakhir (Undo)")
            print("  4. Proses pesanan berikutnya (Dapur)")
            print("  5. Lihat riwayat pesanan selesai")
            print("  6. Keluar")
            print()

            pilihan = input("  Pilih menu [1-6]: ").strip()

            if pilihan == "1":
                nama = input("  Nama pelanggan : ").strip()
                pesanan = input("  Pesanan        : ").strip()
                self.tambah_pelanggan_biasa(nama, pesanan)

            elif pilihan == "2":
                nama = input("  Nama pelanggan VIP : ").strip()
                pesanan = input("  Pesanan            : ").strip()
                self.tambah_pelanggan_vip(nama, pesanan)

            elif pilihan == "3":
                self.batalkan_pesanan()

            elif pilihan == "4":
                self.proses_pesanan()

            elif pilihan == "5":
                self.tampilkan_riwayat()

            elif pilihan == "6":
                print("\n  Terima kasih! Sampai jumpa! 👋\n")
                break

            else:
                print("\n  ⚠️  Pilihan tidak valid!")

            input("\n  Tekan Enter untuk melanjutkan...")


# ==============================================================
#  DEMO OTOMATIS (Simulasi Tanpa Input Manual)
# ==============================================================
def demo_simulasi():
    print("=" * 60)
    print("   DEMO SIMULASI SISTEM RESTORAN CEPAT SAJI")
    print("   Struktur Data: DEQUE")
    print("=" * 60)

    restoran = RestoranCepatSaji("Demo Restoran")

    # Skenario 1: Beberapa pelanggan biasa masuk
    print("\n🔵 Skenario 1: Pelanggan biasa masuk antrian")
    restoran.tambah_pelanggan_biasa("Andi", "Burger + Cola")
    restoran.tambah_pelanggan_biasa("Budi", "Ayam Goreng + Es Teh")
    restoran.tambah_pelanggan_biasa("Citra", "Pizza Slice + Juice")
    restoran.tampilkan_antrian()

    # Skenario 2: Pelanggan VIP masuk, langsung ke depan
    print("\n⭐ Skenario 2: Pelanggan VIP masuk diprioritaskan")
    restoran.tambah_pelanggan_vip("Dewi VIP", "Steak + Air Mineral")
    restoran.tampilkan_antrian()

    # Skenario 3: Batalkan pesanan terakhir (undo)
    print("\n❌ Skenario 3: Batalkan pesanan terakhir")
    restoran.batalkan_pesanan()
    restoran.tampilkan_antrian()

    # Skenario 4: Dapur memproses 2 pesanan
    print("\n👨‍🍳 Skenario 4: Dapur memproses pesanan")
    restoran.proses_pesanan()
    restoran.proses_pesanan()
    restoran.tampilkan_antrian()

    # Riwayat
    restoran.tampilkan_riwayat()

    print("\n✅ Demo selesai! Struktur data DEQUE bekerja dengan baik.")
    print("   - addFirst()    → Pelanggan VIP (O(1))")
    print("   - addLast()     → Pelanggan Biasa (O(1))")
    print("   - removeLast()  → Batalkan/Undo (O(1))")
    print("   - removeFirst() → Proses Dapur (O(1))")


# ==============================================================
#  ENTRY POINT
# ==============================================================
if __name__ == "__main__":
    print("Pilih mode:")
    print("1. Demo otomatis (simulasi)")
    print("2. Mode interaktif (menu)")
    mode = input("Pilihan [1/2]: ").strip()

    if mode == "2":
        app = RestoranCepatSaji()
        app.jalankan()
    else:
        demo_simulasi()