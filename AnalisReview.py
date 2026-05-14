import anthropic
import json
import pandas as pd
from config import API_KEY

# ── SETUP ──────────────────────────────
client = anthropic.Anthropic(api_key=API_KEY)

# ── FUNGSI KIRIM KE CLAUDE ─────────────────
def kirim_ke_claude(prompt):
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=8000,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.content[0].text

# ── FUNGSI BERSIHKAN OUTPUT ───────────────
def bersihkan_json(teks):
    teks = teks.strip()
    if "```" in teks:
        baris = teks.split("\n")
        baris = [b for b in baris 
                 if not b.strip().startswith("```")]
        teks = "\n".join(baris)
    return teks

# -- TARIK DATA EXCEL -------
# Baca file excel 

df = pd.read_excel("data_review_salero_minang.xlsx",
                   sheet_name="Data Review")

#lihat isinya 
print(df.head())

# ubah setiap baris jadi teks
data_review = ""
for index, row in df.iterrows():
    data_review += f"review {row['No']} | {row['Nama Pelanggan']} | {row['Isi Review']}\n"

print(data_review)


# -- PROMT 1 - KLASIFIKASI REVIEW -------

promt_1 = f"""
kamu adalah senior manager analis dibagian pelayanan yang sudah punya pengalaman
20 tahun menganalisa perilaku konsumen kuliner. 

tugas kamu saat ini adalah melakukan klasifikasi atas hasil review yang diberikan konsumen kendalam tiga klasifikasi.
kalsifikasinya antara lain : (positif/negatif/netral)

contoh pengkasifikasiannya adalah sebagai berikut :
positif : "Makanannya lezat, porsinya pas, dan pelayanan sangat cepat."
netral : "Rasanya biasa saja, harga sesuai, tempat cukup nyaman."
negatif : "Makanannya dingin, terlalu asin, dan pelayanannya sangat lambat."

jika kamu menemukan hasil review yang memuat beberapa sentimen sekaligus (misal sentimen positif dan netral) kamu ambil sentimen paling berat sebagai klasifikasi output.
jika dalam satu review terdapat beberapa sentimen dan mengandung sentimen negatif, kamu klasifikasikan review itu dalam negatif.
kamu wajib memberikan alasan penentuan klasifikasi dalam maksimal 7 kata di bagian alasan.

data review yang harus di analis :
{data_review}

⚠️ PENTING: Output HANYA JSON berikut. Tanpa teks apapun di luar JSON.

[
{{
"nama" : "",
"isiReview" : "",
"klasifikasiReview" : "Positif/Netral/Negatif",
"JenisReview" : "Layanan/Makanan",
"alasanKlasifikasi" : "" 
}}
]

"""
# -- PROMT 2 - KLASIFIKASI REVIEW -------

promt_2 = """
kamu adalah seorang senior analis yang memiliki pengalaman 25 tahun dalam mengolah data dan data sains. 

tugas kamu saat ini adalah mengelompokan data JSON ini dalam beberapa kategori :
1. total data
2. total review positif
3. total review negatif
4. total review netral
5. total review layanan
6. total review Makanan
7. layanan yang paling banyak komplain
8. layanan yang paling banyak impresi positif



⚠️ PENTING: Output HANYA JSON berikut. Tanpa teks apapun di luar JSON.

{
"totalData" : "",
"totalPositif" : "",
"totalNegatif" : "",
"totalNetral" : "",
"totalRevLayanan" : "",
"totalRevMakanan" : "",
"layananKomplain" : "",
"layananPositif" : "",
"detailReview" : [{
"nama" : "",
"isiReview" : "", 
"klasifikasiReview" : ""
}]
}

"""
# -- PROMT 3 - KLASIFIKASI REVIEW -------

promt_3 = """
kamu adalah seorang business analys senior yang memiliki pengalaman lebih dari 30 tahun
dan keahlian terbaik kamu adalah membuat laporan analis yang akan diserahkan ke direksi
dengan bahasa indonesia yang baku, tidak teralu panjang, semua konteks dan data penting tersampaikan dengan baik
karena kamu tau kalo data analis kamu akan dipakai para direksi untuk pengambilan keputusan


tugas kamu saat ini adalah melakukan analisa dari data JSON ini, dan kamu buatkan laporan dalam bentuk text yang ahirnya akan ku convert ke pdf

untuk rules bentuk formatnya adalah :
1. format memiliki struktur : pembuka, isi, penutup
2. pada bagian pembuka kamu buat laporan yang menejelaskan terkait detail data penting seperti jumlah review negatif, positif dll (maksimal 20% dari total laporan)
3. pada bagian isi kamu bahas secara komprehensi hasil temuan data yang dijelaskan json sebelumnya (maksimal 50% dari total laporan)
4. pada bagian penutup kamu jelaskan rekomendasi terbaik untuk respon review negatif dan review positif, berikan 3 rekomendasi yang 
executale ( maksimal 30% dari total laporan)
5. laporan maksimal berisi 150 kata dan jangan sampai meningalkan analisa penting ya, soalnya ini akan dipakai direksi mengambil keputusan
"""

# jalankan 3 chain promt otomatis

print("menjalankan promt chain, silahkan ditunggu ..... ")
print("=" * 60)

# chain 1

print("\n Chain 1 Berjalan : Melakukan klasifikasi Review ....")
output_p1_raw = kirim_ke_claude(promt_1)
output_p1_bersih = bersihkan_json(output_p1_raw)
data_klasifikasi = json.loads(output_p1_bersih)
print(f"chain 1 selesai dikerjakan, {len(data_klasifikasi)} review terklasifikasi")

#simpan hasil chain 1
with open("hasil_chain1.json", "w") as f:
    json.dump(data_klasifikasi, f, indent=2, ensure_ascii=False)

# chain 2
print("\n Chain 2 akan segera dijalankan ....")
promt_2_work = promt_2 + output_p1_bersih
ouput_p2_raw = kirim_ke_claude(promt_2_work)
output_p2_bersih = bersihkan_json(ouput_p2_raw)
data_rekap = json.loads(output_p2_bersih)
print("Chain 2 Selesai dikerjakan ......")

#simpan hasil chain 2
with open("hasil_chain2.json", "w") as a :
    json.dump(data_rekap, a, indent=2, ensure_ascii=False)


# chain 3

print("chain 3 berjalan : Melakukan analisa ....")
promt_3_work = promt_3 + output_p2_bersih
ouput_p3 = kirim_ke_claude(promt_3_work)
print("hasil analisa chain 3 sudah selesai ......")

#simpan hasil chain 3 

with open("hasil_laporan_direksi.txt", "w") as b :
    b.write(ouput_p3)

#selesai

print("✅ Selesai!")