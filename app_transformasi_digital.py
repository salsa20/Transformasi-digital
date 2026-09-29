        "q": "Manakah yang paling tepat menggambarkan Transformasi Digital?",
        "options": [
            "Mengubah dokumen kertas menjadi PDF",
            "Menggunakan komputer untuk mengetik laporan",
            "Mengubah cara organisasi menciptakan nilai dengan memanfaatkan teknologi digital",
            "Membeli software baru untuk kantor",
        ],
        "answer": 2,
        "explanation": "Transformasi Digital lebih luas daripada sekadar memakai teknologi. Perubahan dapat mencakup proses, pengalaman pelanggan, organisasi, data, dan model bisnis.",
    },
    {
        "q": "Nota kertas yang diubah menjadi file PDF merupakan contoh...",
        "options": [
            "Digitization",
            "Digitalization",
            "Digital business model innovation",
            "Digital transformation penuh",
        ],
        "answer": 0,
        "explanation": "Digitization berfokus pada mengubah informasi dari bentuk analog/fisik menjadi format digital.",
    },
    {
        "q": "Formulir pemesanan manual yang diubah menjadi form online dan otomatis masuk database paling tepat disebut...",
        "options": [
            "Digitization",
            "Digitalization",
            "Diversifikasi",
            "Rebranding",
        ],
        "answer": 1,
        "explanation": "Digitalization menggunakan teknologi digital untuk memperbaiki atau mendesain ulang proses yang sudah ada.",
    },
    {
        "q": "Sebelum memilih teknologi untuk transformasi, langkah yang paling tepat adalah...",
        "options": [
            "Membeli teknologi paling mahal",
            "Mengidentifikasi masalah dan tujuan bisnis",
            "Mengikuti teknologi yang sedang viral",
            "Mengganti seluruh karyawan",
        ],
        "answer": 1,
        "explanation": "Transformasi sebaiknya dimulai dari kebutuhan dan tujuan bisnis agar teknologi yang dipilih benar-benar menghasilkan nilai.",
    },
    {
        "q": "Perubahan dari penjualan satu kali menjadi model subscription merupakan contoh perubahan pada...",
        "options": [
            "Warna brand",
            "Business model",
            "Layout kantor",
            "Perangkat keras",
        ],
        "answer": 1,
        "explanation": "Subscription mengubah cara perusahaan menawarkan nilai dan memperoleh pendapatan sehingga berkaitan langsung dengan business model.",
    },
    {
        "q": "Manakah yang merupakan tantangan umum Transformasi Digital?",
        "options": [
            "Resistensi terhadap perubahan",
            "Semua sistem selalu kompatibel",
            "Teknologi tidak pernah berubah",
            "Tidak ada kebutuhan pelanggan",
        ],
        "answer": 0,
        "explanation": "Resistensi, skill gap, legacy system, keamanan, dan perubahan budaya merupakan tantangan yang umum muncul.",
    },
    {
        "q": "Jika perusahaan ingin mengetahui apakah sistem online ordering mempercepat proses pemesanan, KPI yang relevan adalah...",
        "options": [
            "Warna website",
            "Rata-rata waktu pemrosesan order",
            "Jumlah poster di toko",
            "Jumlah meja kantor",
        ],
        "answer": 1,
        "explanation": "Waktu pemrosesan order secara langsung mengukur perubahan efisiensi proses pemesanan.",
    },
    {
        "q": "Sebuah toko mengintegrasikan POS, inventory, CRM, dan dashboard. Perubahan tersebut terutama menunjukkan...",
        "options": [
            "Integrasi proses dan data",
            "Penghapusan data",
            "Digitalisasi dokumen saja",
            "Pengurangan kebutuhan pelanggan",
        ],
        "answer": 0,
        "explanation": "Integrasi memungkinkan data dan proses dari beberapa fungsi saling terhubung sehingga mendukung operasi dan pengambilan keputusan.",
    },
    {
        "q": "Dalam studi kasus transformasi digital, mengapa mahasiswa harus memahami kondisi bisnis sebelum memberikan solusi?",
        "options": [
            "Agar solusi menjawab masalah nyata dan tujuan bisnis",
            "Agar selalu menggunakan AI",
            "Agar semua bisnis memakai sistem yang sama",
            "Agar proyek menjadi lebih mahal",
        ],
        "answer": 0,
        "explanation": "Solusi digital harus sesuai dengan masalah, pelanggan, proses, sumber daya, dan tujuan organisasi.",
    },
    {
        "q": "Pernyataan yang paling tepat adalah...",
        "options": [
            "Transformasi Digital hanya masalah IT",
            "Transformasi Digital selalu membutuhkan AI",
            "Transformasi Digital dapat melibatkan teknologi, proses, manusia, strategi, data, dan model bisnis",
            "Transformasi Digital selesai setelah aplikasi diluncurkan",
        ],
        "answer": 2,
        "explanation": "Transformasi Digital bersifat lintas organisasi. Teknologi merupakan enabler, tetapi perubahan nilai dan cara kerja bisnis juga menjadi bagian penting.",
    },
]

business_cases = {
    "Toko Retail": {
        "problem": "Transaksi masih dicatat manual, stok sering berbeda dengan kondisi nyata, dan pelanggan mulai meminta pemesanan online.",
        "flow": ["Pelanggan", "Toko / POS", "Inventory", "Database", "Online Ordering", "Payment", "Dashboard"],
        "kpi": ["Stock accuracy", "Order processing time", "Online conversion rate", "Repeat purchase rate"],
    },
    "Coffee Shop": {
        "problem": "Pesanan saat jam sibuk menumpuk, pencatatan pelanggan belum terintegrasi, dan promosi masih dilakukan secara massal.",
        "flow": ["Pelanggan", "QR / App", "Order System", "Payment", "POS", "CRM", "Analytics"],
        "kpi": ["Average order time", "Order accuracy", "Customer retention", "Average order value"],
    },
    "Laundry": {
        "problem": "Status cucian sering ditanyakan melalui WhatsApp, pembayaran masih manual, dan pemilik kesulitan memantau order.",
        "flow": ["Pelanggan", "App / WhatsApp", "Order System", "Database", "Payment", "Pickup", "Status Tracking"],
        "kpi": ["Order completion time", "On-time delivery", "Repeat order rate", "Complaint rate"],
    },
    "Kampus": {
        "problem": "Informasi akademik tersebar di banyak kanal, proses administrasi masih manual, dan data sulit direkap untuk monitoring.",
        "flow": ["Mahasiswa", "Portal / App", "Academic System", "Database", "Dashboard", "Notification", "Admin"],
        "kpi": ["Processing time", "Data completeness", "Response time", "User satisfaction"],
    },
}

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("Pertemuan")
st.sidebar.caption("Bisnis Digital")

menu = st.sidebar.radio(
    "Navigasi",
    [
        "🏠 Beranda",
        "📘 Materi",
        "🔄 Simulasi Transformasi",
        "📋 Studi Kasus",
        "🧩 Latihan",
        "🏆 Kuis 10 Soal",
        "✅ Ringkasan",
        "📚 Referensi",
    ],
)

st.sidebar.divider()
st.sidebar.markdown("**Sub-CPMK**")
st.sidebar.write("Mahasiswa mampu memahami Transformasi Digital.")

st.sidebar.markdown("**Indikator**")
st.sidebar.write("Memahami Transformasi Digital.")

st.sidebar.markdown("**Pembelajaran**")
st.sidebar.write("Kuliah • Diskusi")

st.sidebar.markdown("**TM**")
st.sidebar.write("1 × (2 × 50 menit)")

st.sidebar.markdown("**Tugas**")
st.sidebar.write("Analisis Studi Kasus")

st.sidebar.markdown("**PT + BM**")
st.sidebar.write("(1 + 1) × (2 × 60 menit)")

st.sidebar.markdown("**Sumber utama**")
st.sidebar.write("Aagaard (2019) — Digital Business Models Driving Transformation and Innovation.")

# -----------------------------
# Header
# -----------------------------
st.markdown("""
<div class="hero">
    <h1>🔄 Transformasi Digital</h1>
    <p>Memahami bagaimana teknologi digital mengubah proses, pengalaman pelanggan, organisasi, dan cara bisnis menciptakan nilai.</p>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# BERANDA
# -----------------------------
if menu == "🏠 Beranda":
    c1, c2, c3 = st.columns(3)
    with c1:
