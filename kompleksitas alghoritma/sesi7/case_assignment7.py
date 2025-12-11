# ==============================
# CASE ASSIGNMENT 7 – GREEDY STRATEGY
# Mata Kuliah : Complexity Algorithm
# ==============================

# ---------------------------------------
# 1️⃣ PROGRAM UANG KEMBALIAN (GREEDY)
# ---------------------------------------

def greedy_coin_change(amount, coins):
    coins.sort(reverse=True)
    result = []
    total_coins = 0

    for coin in coins:
        count = amount // coin
        if count > 0:
            result.append((coin, count))
            total_coins += count
            amount -= coin * count

    print("\n=== HASIL PROGRAM KEMBALIAN (GREEDY) ===")
    for coin, count in result:
        print(f"{count} koin x {coin}")
    print(f"Total koin digunakan: {total_coins}\n")


# ---------------------------------------
# 2️⃣ ACTIVITY SELECTION PROBLEM
# ---------------------------------------

activities = [
    {"name": "A1", "start": 1, "finish": 3},
    {"name": "A2", "start": 2, "finish": 5},
    {"name": "A3", "start": 4, "finish": 6},
    {"name": "A4", "start": 6, "finish": 8},
    {"name": "A5", "start": 5, "finish": 7},
]

def activity_selection_by_finish(acts):
    acts = sorted(acts, key=lambda x: x["finish"])
    selected = []
    last_finish = 0
    for a in acts:
        if a["start"] >= last_finish:
            selected.append(a)
            last_finish = a["finish"]
    return selected

def activity_selection_by_duration(acts):
    acts = sorted(acts, key=lambda x: x["finish"] - x["start"])
    selected = []
    last_finish = 0
    for a in acts:
        if a["start"] >= last_finish:
            selected.append(a)
            last_finish = a["finish"]
    return selected

# Jalankan kedua versi
ver1 = activity_selection_by_finish(activities)
ver2 = activity_selection_by_duration(activities)

print("=== HASIL ACTIVITY SELECTION ===")
print("Versi 1 (berdasarkan waktu selesai):", [a["name"] for a in ver1])
print("Versi 2 (berdasarkan durasi):", [a["name"] for a in ver2])
print("Apakah jumlah aktivitas sama?", len(ver1) == len(ver2), "\n")


# ---------------------------------------
# 3️⃣ SHORT JOB FIRST (SJF) SCHEDULING
# ---------------------------------------

def sjf_schedule(jobs):
    jobs.sort()
    total_time = 0
    waiting_time = 0
    completion_times = []

    for j in jobs:
        waiting_time += total_time
        total_time += j
        completion_times.append(total_time)

    avg_time = sum(completion_times) / len(jobs)

    print("=== HASIL PENJADWALAN (SJF) ===")
    print("Urutan layanan (dari tercepat):", jobs)
    print("Waktu selesai tiap pelanggan:", completion_times)
    print("Total waktu di sistem:", sum(completion_times))
    print("Rata-rata waktu di sistem:", round(avg_time, 2))

# Data dari soal
schedule = [5, 10, 3, 8, 2]
sjf_schedule(schedule)


# ---------------------------------------
# 🔹 Menjalankan Program Coin Change Secara Interaktif
# ---------------------------------------
if __name__ == "__main__":
    try:
        amount = int(input("\nMasukkan jumlah uang: "))
        coins = list(map(int, input("Masukkan nilai koin (pisahkan dengan spasi): ").split()))
        greedy_coin_change(amount, coins)
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")
