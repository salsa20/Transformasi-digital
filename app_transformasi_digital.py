import streamlit as st

st.set_page_config(
    page_title="Pertemuan | Transformasi Digital",
    page_icon="🔄",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>
.block-container {
    max-width: 1200px;
    padding-top: 1.5rem;
    padding-bottom: 3rem;
}
.hero {
    padding: 2rem;
    border-radius: 22px;
    background: linear-gradient(135deg, #f6f8ff 0%, #eefaf7 100%);
    border: 1px solid rgba(120,120,120,.18);
    margin-bottom: 1.2rem;
}
.hero h1 {
    margin: 0 0 .4rem 0;
    font-size: 2.35rem;
}
.hero p {
    font-size: 1.05rem;
    margin: 0;
    opacity: .82;
}
.card {
    border: 1px solid rgba(120,120,120,.18);
    border-radius: 18px;
    padding: 1.2rem;
    margin-bottom: 1rem;
    background: rgba(255,255,255,.65);
}
.small-card {
    border: 1px solid rgba(120,120,120,.18);
    border-radius: 16px;
    padding: 1rem;
    min-height: 120px;
}
.flow {
    border-radius: 16px;
    padding: 1rem 1.1rem;
    background: rgba(120,120,120,.06);
    border: 1px dashed rgba(120,120,120,.35);
    font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
    line-height: 1.75;
}
.badge {
    display: inline-block;
    padding: .28rem .7rem;
    border-radius: 999px;
    border: 1px solid rgba(120,120,120,.25);
    margin: .15rem .2rem .15rem 0;
    font-size: .86rem;
}
.note {
    padding: 1rem 1.1rem;
    border-left: 5px solid #6c63ff;
    background: rgba(108,99,255,.08);
    border-radius: 12px;
}
.quiz-box {
    border: 1px solid rgba(120,120,120,.22);
    border-radius: 18px;
    padding: 1.15rem;
    margin-bottom: 1rem;
}
.case-box {
    border: 1px solid rgba(120,120,120,.18);
    border-radius: 18px;
    padding: 1.2rem;
    background: rgba(255,255,255,.55);
    margin-bottom: 1rem;
}
div[data-testid="stMetric"] {
    border: 1px solid rgba(120,120,120,.16);
    padding: .8rem;
    border-radius: 16px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Data
# -----------------------------
quiz = [
    {
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
# GLOSSARY DATA
# -----------------------------
glossary = {
    "AI (Artificial Intelligence)": "Kecerdasan buatan: teknologi yang membuat komputer dapat melakukan tugas yang biasanya membutuhkan kemampuan manusia, seperti mengenali pola, membuat prediksi, atau memahami bahasa.",
    "API (Application Programming Interface)": "Antarmuka yang memungkinkan satu aplikasi atau sistem berkomunikasi dan bertukar data dengan aplikasi lain.",
    "BI (Business Intelligence)": "Metode dan tools untuk mengubah data bisnis menjadi informasi yang membantu monitoring dan pengambilan keputusan.",
    "Business Model": "Cara perusahaan menciptakan, menyampaikan, dan memperoleh nilai atau pendapatan dari pelanggan.",
    "Business Process": "Serangkaian aktivitas yang dilakukan untuk menghasilkan produk atau layanan.",
    "CRM (Customer Relationship Management)": "Sistem atau pendekatan untuk mengelola data dan hubungan pelanggan, misalnya riwayat pembelian, komunikasi, dan segmentasi.",
    "Cloud / Cloud Computing": "Penggunaan server, penyimpanan, database, atau komputasi melalui internet tanpa harus memiliki seluruh perangkat fisiknya sendiri.",
    "Conversion Rate": "Persentase pengunjung atau calon pelanggan yang melakukan tindakan yang ditargetkan, misalnya pembelian.",
    "Customer Experience": "Pengalaman pelanggan ketika berinteraksi dengan perusahaan, produk, layanan, website, aplikasi, pembayaran, dan layanan setelah pembelian.",
    "Customer Relationship": "Cara perusahaan membangun dan mempertahankan hubungan dengan pelanggan.",
    "Data Analytics": "Proses mengolah dan menganalisis data untuk menemukan informasi, pola, atau insight yang membantu keputusan bisnis.",
    "Data Governance": "Aturan, tanggung jawab, proses, dan standar agar data dikelola secara konsisten, aman, dan tepat.",
    "Dashboard": "Tampilan visual yang merangkum data dan KPI agar kondisi bisnis dapat dipantau dengan cepat.",
    "Digital Channel": "Kanal digital yang digunakan untuk berinteraksi atau menjual kepada pelanggan, seperti website, aplikasi, atau marketplace.",
    "Digital Payment": "Pembayaran melalui media atau sistem digital, misalnya QRIS, e-wallet, atau mobile banking.",
    "Digital Opportunity": "Bagian proses atau model bisnis yang berpotensi diperbaiki atau dikembangkan dengan teknologi digital.",
    "Digital Transformation": "Perubahan yang lebih luas pada cara organisasi bekerja, melayani pelanggan, dan menciptakan nilai dengan memanfaatkan teknologi digital.",
    "Digitalization": "Pemanfaatan teknologi digital untuk memperbaiki atau mengubah proses yang sudah ada.",
    "Digitization": "Proses mengubah informasi dari bentuk analog atau fisik menjadi bentuk digital.",
    "Ecosystem": "Jaringan perusahaan, pelanggan, supplier, partner, platform, dan pihak lain yang saling berhubungan dalam menciptakan nilai.",
    "ERP (Enterprise Resource Planning)": "Sistem terintegrasi untuk membantu mengelola proses seperti keuangan, persediaan, pembelian, dan operasional.",
    "Governance": "Aturan, struktur tanggung jawab, dan mekanisme pengawasan agar teknologi dan data dikelola secara terarah.",
    "IoT (Internet of Things)": "Konsep menghubungkan perangkat fisik ke internet agar dapat mengirim, menerima, atau bertukar data.",
    "KPI (Key Performance Indicator)": "Indikator utama untuk mengukur apakah proses, program, atau tujuan bisnis mencapai hasil yang diharapkan.",
    "Legacy System": "Sistem lama yang masih digunakan dan dapat menjadi tantangan ketika perusahaan mengadopsi teknologi baru.",
    "Mobile": "Teknologi atau layanan yang digunakan melalui perangkat bergerak seperti smartphone atau tablet.",
    "Mitigation": "Tindakan untuk mengurangi kemungkinan terjadinya risiko atau mengurangi dampaknya.",
    "Omnichannel": "Pendekatan yang menghubungkan beberapa kanal penjualan dan layanan agar pengalaman pelanggan tetap terintegrasi.",
    "Online Conversion Rate": "Persentase pengunjung online yang melakukan tindakan target, biasanya pembelian atau pendaftaran.",
    "Payment Gateway": "Layanan yang menghubungkan transaksi pembayaran pelanggan dengan penyedia pembayaran seperti bank atau e-wallet.",
    "Personalization": "Penyesuaian produk, layanan, konten, atau promosi berdasarkan karakteristik atau perilaku pelanggan.",
    "Platform": "Sistem digital yang menghubungkan pengguna, penjual, penyedia layanan, atau pihak lain.",
    "POS (Point of Sale)": "Sistem kasir untuk mencatat transaksi penjualan dan biasanya terhubung dengan stok atau database.",
    "Predictive Analytics": "Analisis data yang digunakan untuk memperkirakan kemungkinan kondisi atau kejadian di masa depan.",
    "Privacy": "Perlindungan terhadap penggunaan dan pengelolaan informasi pribadi.",
    "Process Automation": "Penggunaan teknologi untuk menjalankan aktivitas proses secara otomatis sehingga mengurangi pekerjaan manual.",
    "Roadmap": "Rencana tahapan implementasi yang menunjukkan perubahan jangka pendek, menengah, dan panjang.",
    "Revenue Model": "Cara perusahaan memperoleh pendapatan dari produk, layanan, pelanggan, atau aktivitas bisnis.",
    "Scalability": "Kemampuan sistem atau proses untuk menangani peningkatan pengguna, transaksi, atau beban kerja.",
    "Self-service": "Kemampuan pelanggan menyelesaikan kebutuhannya sendiri melalui sistem digital tanpa selalu membutuhkan bantuan petugas.",
    "Single Source of Truth": "Satu sumber data utama yang disepakati sebagai acuan agar informasi antarbagian konsisten.",
    "Skill Gap": "Kesenjangan antara kemampuan yang dimiliki karyawan dan kemampuan yang dibutuhkan untuk menjalankan pekerjaan atau teknologi baru.",
    "Subscription": "Model pendapatan ketika pelanggan membayar secara berkala, misalnya bulanan atau tahunan, untuk mendapatkan akses produk atau layanan.",
    "Value Proposition": "Manfaat utama yang ditawarkan perusahaan kepada pelanggan sebagai alasan pelanggan memilih produk atau layanan.",
    "Value Capture": "Cara perusahaan memperoleh manfaat ekonomi atau pendapatan dari nilai yang telah diciptakan.",
    "Workflow": "Urutan aktivitas dan perpindahan pekerjaan dari satu tahap atau pihak ke tahap berikutnya.",
    "Cybersecurity": "Upaya melindungi sistem, jaringan, aplikasi, dan data dari akses, serangan, atau gangguan yang tidak diizinkan.",
    "Customer Retention": "Kemampuan perusahaan mempertahankan pelanggan agar tetap menggunakan atau membeli produk atau layanan.",
    "Repeat Purchase Rate": "Persentase pelanggan yang melakukan pembelian kembali dalam periode tertentu.",
    "Average Order Value": "Rata-rata nilai uang dari setiap transaksi atau pesanan.",
    "Order Accuracy": "Tingkat ketepatan pesanan dibandingkan dengan pesanan yang diminta pelanggan.",
    "Average Order Time": "Rata-rata waktu yang dibutuhkan untuk menyelesaikan proses pemesanan pada tahap yang ditentukan.",
    "Order Processing Time": "Waktu yang dibutuhkan untuk memproses pesanan sejak diterima sampai tahap berikutnya.",
    "Order Completion Rate": "Persentase pesanan yang berhasil diselesaikan dibandingkan dengan seluruh pesanan yang masuk.",
    "On-time Delivery": "Persentase pesanan yang dikirim atau diterima sesuai waktu yang dijanjikan.",
    "Complaint Rate": "Jumlah atau persentase keluhan pelanggan dibandingkan dengan transaksi atau pelanggan dalam periode tertentu.",
    "Data Completeness": "Tingkat kelengkapan data yang dibutuhkan; semakin lengkap, semakin sedikit informasi penting yang kosong.",
    "Response Time": "Waktu yang dibutuhkan sistem atau petugas untuk memberikan respons kepada pelanggan atau pengguna.",
    "User Satisfaction": "Tingkat kepuasan pengguna terhadap sistem, layanan, atau pengalaman yang diterima.",
    "Stock Accuracy": "Tingkat kesesuaian jumlah stok yang tercatat di sistem dengan stok yang benar-benar tersedia.",
    "Current Process": "Cara kerja atau alur proses bisnis yang sedang berjalan sebelum dilakukan perubahan.",
    "Customer Segment": "Kelompok pelanggan yang memiliki karakteristik atau kebutuhan yang relatif serupa.",
    "Channel": "Media atau jalur yang digunakan perusahaan untuk menjangkau pelanggan dan menyampaikan produk atau layanan.",
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
        "📖 Glosarium Istilah",
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

st.sidebar.markdown("**💡 Tips**")
st.sidebar.caption("Jika menemukan istilah yang belum familiar, buka menu 📖 Glosarium Istilah. Anda dapat mencari CRM, KPI, API, POS, AI, Cloud, Dashboard, dan istilah lainnya.")

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
        st.markdown("""
        <div class="small-card">
        <b>🎯 Fokus</b><br><br>
        Memahami konsep dan ruang lingkup Transformasi Digital.
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div class="small-card">
        <b>🧠 Metode</b><br><br>
        Kuliah, diskusi, studi kasus, latihan, dan kuis.
        </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown("""
        <div class="small-card">
        <b>📚 Hasil Akhir</b><br><br>
        Mahasiswa mampu menganalisis kebutuhan transformasi digital sederhana.
        </div>
        """, unsafe_allow_html=True)

    st.subheader("Tujuan Pembelajaran")
    st.markdown("""
    Setelah mengikuti pertemuan ini, mahasiswa diharapkan mampu:
    1. Menjelaskan pengertian Transformasi Digital.
    2. Membedakan digitization, digitalization, dan digital transformation.
    3. Mengidentifikasi pendorong dan tantangan Transformasi Digital.
    4. Menjelaskan perubahan pada customer, process, data, people, technology, dan business model.
    5. Menganalisis studi kasus bisnis dan menyusun rekomendasi transformasi.
    6. Menentukan KPI sederhana untuk mengevaluasi hasil transformasi.
    """)

    st.markdown("""
    <div class="note">
    <b>Analogi sederhana:</b> Transformasi Digital bukan sekadar memindahkan pekerjaan
    dari kertas ke komputer. Yang berubah adalah <b>cara bisnis bekerja dan menciptakan nilai</b>
    dengan bantuan teknologi digital.
    </div>
    """, unsafe_allow_html=True)


    with st.expander("📖 Istilah penting di halaman ini"):
        st.markdown("""
        - **Customer Experience:** pengalaman pelanggan saat berinteraksi dengan perusahaan.
        - **Business Process:** rangkaian aktivitas untuk menghasilkan produk atau layanan.
        - **KPI:** indikator utama untuk mengukur keberhasilan tujuan atau proses bisnis.
        - **Business Model:** cara perusahaan menciptakan, menyampaikan, dan memperoleh nilai.
        """)

    st.markdown("### Alur berpikir")
    st.markdown("""
    <div class="flow">
    Masalah Bisnis → Tujuan → Proses Saat Ini → Peluang Digital → Solusi → Implementasi → KPI → Perbaikan Berkelanjutan
    </div>
    """, unsafe_allow_html=True)

# -----------------------------
# MATERI
# -----------------------------
elif menu == "📘 Materi":
    tabs = st.tabs([
        "Konsep Dasar",
        "3 Istilah Penting",
        "Area Perubahan",
        "Pendorong & Tantangan",
        "Business Model",
        "Metode Studi Kasus",
    ])

    with tabs[0]:
        st.subheader("1. Apa itu Transformasi Digital?")
        st.write(
            "Transformasi Digital adalah perubahan organisasi yang dipicu dan dibentuk oleh "
            "teknologi digital sehingga perusahaan dapat mengubah cara bekerja, menciptakan nilai, "
            "berinteraksi dengan pelanggan, dan menjalankan bisnis."
        )
        st.markdown(
            '<span class="badge">Customer</span>'
            '<span class="badge">Process</span>'
            '<span class="badge">Data</span>'
            '<span class="badge">People</span>'
            '<span class="badge">Technology</span>'
            '<span class="badge">Business Model</span>',
            unsafe_allow_html=True,
        )
        st.markdown("### Contoh sederhana")
        st.write(
            "Toko yang awalnya hanya menerima pesanan di kasir kemudian membangun online ordering, "
            "mengintegrasikan stok, menyediakan pembayaran digital, memakai CRM, dan menggunakan "
            "dashboard untuk mengambil keputusan telah melakukan perubahan yang lebih luas daripada sekadar digitalisasi dokumen."
        )

        with st.expander("📖 Istilah pada contoh"):
            st.markdown("""
            - **Online ordering:** pemesanan melalui kanal digital.
            - **CRM:** sistem/pendekatan untuk mengelola data dan hubungan pelanggan.
            - **Digital payment:** pembayaran menggunakan media digital.
            - **Dashboard:** tampilan visual untuk memantau data dan indikator bisnis.
            """)

    with tabs[1]:
        st.subheader("2. Digitization, Digitalization, dan Digital Transformation")
        data = {
            "Konsep": ["Digitization", "Digitalization", "Digital Transformation"],
            "Fokus": [
                "Mengubah informasi analog/fisik menjadi digital",
                "Memanfaatkan teknologi untuk memperbaiki proses",
                "Mengubah cara organisasi bekerja dan menciptakan nilai",
            ],
            "Contoh": [
                "Nota kertas → PDF",
                "Form manual → form online + database",
                "Toko fisik → omnichannel + CRM + analytics",
            ],
        }
        st.dataframe(data, use_container_width=True, hide_index=True)

        st.markdown("""
        <div class="note">
        <b>Cara cepat mengingat:</b><br>
        Digitization = <b>mengubah bentuk data</b><br>
        Digitalization = <b>memperbaiki proses</b><br>
        Digital Transformation = <b>mengubah cara bisnis menciptakan nilai</b>
        </div>
        """, unsafe_allow_html=True)

    with tabs[2]:
        st.subheader("3. Area yang Dapat Berubah")
        areas = [
            ("Customer Experience", "Kanal digital, personalisasi, self-service"),
            ("Business Process", "Otomatisasi, integrasi, workflow"),
            ("Data & Analytics", "Dashboard, BI, predictive analytics, AI"),
            ("People & Culture", "Skill, kolaborasi, pola kerja"),
            ("Technology", "Cloud, API, mobile, AI, IoT"),
            ("Business Model", "Value proposition, channel, revenue model"),
            ("Ecosystem", "Partner, platform, supplier, customer"),
            ("Governance", "Risk, privacy, cybersecurity, compliance"),
        ]
        for i in range(0, len(areas), 2):
            c1, c2 = st.columns(2)
            for col, item in zip([c1, c2], areas[i:i+2]):
                with col:
                    st.markdown(f"""
                    <div class="card">
                    <b>{item[0]}</b><br>{item[1]}
                    </div>
                    """, unsafe_allow_html=True)

    with tabs[3]:
        st.subheader("4. Pendorong dan Tantangan")
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("### 🚀 Pendorong")
            st.markdown("""
            - Perubahan perilaku pelanggan
            - Persaingan digital
            - Kebutuhan efisiensi
            - Pengambilan keputusan berbasis data
            - AI, cloud, platform, dan mobile
            - Perubahan model bisnis
            """)
        with c2:
            st.markdown("### ⚠️ Tantangan")
            st.markdown("""
            - Resistensi terhadap perubahan
            - Skill gap
            - Legacy system
            - Investasi dan prioritas
            - Keamanan dan privasi
            - Perubahan budaya dan proses
            - Risiko tidak menghasilkan nilai bisnis
            """)

        st.info("Pertanyaan manager: bukan hanya 'teknologi apa yang kita gunakan?', tetapi 'masalah bisnis apa yang ingin kita selesaikan?'")

    with tabs[4]:
        st.subheader("5. Transformasi dan Business Model")
        st.write("Transformasi digital dapat mengubah cara perusahaan menawarkan nilai dan memperoleh pendapatan.")
        model = {
            "Elemen": [
                "Value Proposition",
                "Customer Segment",
                "Channel",
                "Customer Relationship",
                "Revenue Model",
                "Key Activities / Resources",
                "Partners / Ecosystem",
            ],
            "Contoh perubahan digital": [
                "Produk fisik → layanan digital",
                "Mass market → personalized segment",
                "Toko → omnichannel",
                "Tatap muka → self-service / digital support",
                "One-time sale → subscription",
                "Manual → automated & data-driven",
                "Partner lokal → platform ecosystem",
            ],
        }
        st.dataframe(model, use_container_width=True, hide_index=True)

        st.markdown("""
        <div class="flow">
        Customer Need → Value Proposition → Digital Channel → Digital Process → Data → Revenue / Value Capture
        </div>
        """, unsafe_allow_html=True)

        with st.expander("📖 Istilah pada Business Model"):
            st.markdown("""
            - **Value Proposition:** manfaat utama yang ditawarkan kepada pelanggan.
            - **Digital Channel:** kanal digital untuk menjangkau atau melayani pelanggan.
            - **Revenue Model:** cara perusahaan memperoleh pendapatan.
            - **Value Capture:** cara perusahaan memperoleh manfaat ekonomi dari nilai yang diciptakan.
            """)

    with tabs[5]:
        st.subheader("6. Metode Studi Kasus")
        st.write("Gunakan alur berikut saat menganalisis kasus Transformasi Digital:")
        steps = [
            ("1", "Understand the Business", "Pahami produk, pelanggan, proses, dan sumber pendapatan."),
            ("2", "Identify the Problem", "Temukan masalah berdasarkan fakta atau data."),
            ("3", "Map Current Process", "Gambarkan bagaimana proses berjalan saat ini."),
            ("4", "Find Digital Opportunity", "Cari bagian yang dapat diperbaiki dengan teknologi digital."),
            ("5", "Design Transformation", "Rancang perubahan proses, customer experience, data, people, dan model bisnis."),
            ("6", "Define KPI", "Tentukan indikator keberhasilan."),
            ("7", "Recommend & Justify", "Tentukan prioritas dan jelaskan alasan bisnisnya."),
        ]
        for num, title, desc in steps:
            st.markdown(f"""
            <div class="card">
            <b>{num}. {title}</b><br>{desc}
            </div>
            """, unsafe_allow_html=True)

# -----------------------------
# SIMULASI
# -----------------------------
elif menu == "🔄 Simulasi Transformasi":
    st.subheader("Simulasi Alur Transformasi Digital")
    business = st.selectbox("Pilih jenis bisnis", list(business_cases.keys()))
    case = business_cases[business]

    st.markdown("### Kondisi bisnis")
    st.info(case["problem"])

    st.markdown("### Contoh alur digital")
    st.markdown(
        '<div class="flow">' + " → ".join(case["flow"]) + "</div>",
        unsafe_allow_html=True,
    )

    st.markdown("### Pilih situasi yang terjadi")
    problem = st.selectbox(
        "Situasi",
        [
            "Pelanggan meningkat tajam",
            "Data pelanggan tersebar",
            "Proses masih banyak manual",
            "Pelanggan mengeluh karena layanan lambat",
            "Manajemen membutuhkan dashboard",
        ],
    )

    if problem == "Pelanggan meningkat tajam":
        st.success("Fokus: scalability, automation, kapasitas sistem, dan desain proses.")
    elif problem == "Data pelanggan tersebar":
        st.warning("Fokus: database terpusat, integrasi sistem, CRM, data governance.")
    elif problem == "Proses masih banyak manual":
        st.warning("Fokus: digitalization, workflow, automation, dan integrasi.")
    elif problem == "Pelanggan mengeluh karena layanan lambat":
        st.warning("Fokus: customer journey, bottleneck proses, service design, dan KPI waktu layanan.")
    else:
        st.info("Fokus: data integration, BI/dashboard, KPI, dan pengambilan keputusan berbasis data.")

    st.markdown("### KPI yang dapat digunakan")
    st.write(", ".join(case["kpi"]))
    with st.expander("📖 Apa itu KPI?"):
        st.write("KPI (Key Performance Indicator) adalah indikator utama untuk mengukur apakah suatu proses atau tujuan bisnis mencapai hasil yang diharapkan.")
        st.caption("Contoh: Stock accuracy mengukur kesesuaian stok yang tercatat di sistem dengan stok yang benar-benar tersedia.")


# -----------------------------
# STUDI KASUS
# -----------------------------
elif menu == "📋 Studi Kasus":
    st.subheader("Studi Kasus: Toko Sinar Jaya")

    st.markdown("""
    <div class="case-box">
    <b>Peran Anda: Business Transformation Supervisor</b><br><br>
    Toko Sinar Jaya adalah toko retail perlengkapan rumah tangga. Transaksi masih banyak
    dicatat menggunakan nota dan spreadsheet. Promosi dilakukan melalui WhatsApp secara manual.
    Permintaan pelanggan untuk pemesanan online mulai meningkat.
    </div>
    """, unsafe_allow_html=True)

    st.dataframe({
        "Indikator": [
            "Transaksi per bulan",
            "Transaksi terlambat dicatat",
            "Pesanan perlu konfirmasi ulang karena stok",
            "Permintaan pemesanan online",
        ],
        "Kondisi": ["2.000", "15%", "8%", "Meningkat"],
    }, use_container_width=True, hide_index=True)


    with st.expander("📖 Istilah yang mungkin muncul"):
        st.markdown("""
        - **Current Process:** cara kerja bisnis saat ini.
        - **Digital Opportunity:** bagian proses yang berpotensi diperbaiki dengan teknologi digital.
        - **Roadmap:** tahapan implementasi perubahan.
        - **KPI:** ukuran untuk menilai keberhasilan.
        - **Mitigation:** tindakan untuk mengurangi risiko.
        """)

    st.markdown("### Pertanyaan Analisis")
    questions = [
        "Identifikasi minimal 3 masalah utama.",
        "Petakan proses bisnis saat ini.",
        "Tentukan peluang transformasi digital.",
        "Usulkan solusi dan jelaskan alasan bisnisnya.",
        "Jelaskan dampaknya terhadap customer experience, proses, data, dan SDM.",
        "Apakah business model perlu berubah? Jelaskan.",
        "Tentukan minimal 3 KPI.",
        "Susun roadmap jangka pendek, menengah, dan panjang.",
        "Identifikasi risiko dan mitigasinya.",
    ]
    for q in questions:
        st.write("• " + q)

    with st.expander("Contoh arah jawaban"):
        st.markdown("""
        **Jangka pendek:** POS dan inventory terintegrasi.

        **Jangka menengah:** online ordering, payment digital, dan dashboard.

        **Lanjutan:** CRM, customer segmentation, dan analytics.

        **KPI:** stock accuracy, order processing time, online conversion rate, repeat purchase rate.

        **Catatan:** Mahasiswa tidak harus memilih solusi yang sama. Yang dinilai adalah kemampuan menghubungkan masalah → solusi → KPI → nilai bisnis.
        """)

# -----------------------------
# LATIHAN
# -----------------------------
elif menu == "🧩 Latihan":
    st.subheader("Latihan Studi Kasus")

    with st.expander("Kasus 1 — Coffee Shop", expanded=True):
        st.write(
            "Sebuah coffee shop ramai pada jam makan siang. Antrean panjang terjadi karena "
            "pemesanan dan pembayaran masih dilakukan di kasir. Pemilik ingin memperbaiki pengalaman pelanggan."
        )
        st.text_area("Sebagai supervisor, apa yang akan Anda ubah?", key="lat1", height=120)
        if st.button("Lihat panduan Kasus 1"):
            st.info(
                "Contoh arah: QR ordering / mobile ordering, digital payment, integrasi order dengan POS, "
                "dashboard waktu layanan, dan KPI seperti average order time."
            )

    with st.expander("Kasus 2 — Laundry Digital"):
        st.write(
            "Laundry menerima banyak pertanyaan WhatsApp tentang status cucian. Pemilik juga kesulitan "
            "memantau order, pembayaran, dan pengantaran."
        )
        st.text_area("Rancang solusi transformasinya.", key="lat2", height=120)
        if st.button("Lihat panduan Kasus 2"):
            st.info(
                "Contoh arah: order system, database status laundry, payment digital, pickup/delivery tracking, "
                "notifikasi otomatis, dan dashboard."
            )

    with st.expander("Kasus 3 — Kampus"):
        st.write(
            "Informasi akademik tersebar di WhatsApp, spreadsheet, dan beberapa sistem. "
            "Manajemen kesulitan memperoleh laporan yang konsisten."
        )
        st.text_area("Apa yang harus diubah dari sisi proses, data, dan teknologi?", key="lat3", height=120)
        if st.button("Lihat panduan Kasus 3"):
            st.info(
                "Contoh arah: integrasi data, single source of truth, portal akademik, workflow digital, "
                "dashboard monitoring, dan data governance."
            )

    st.divider()
    st.subheader("Tugas Individu / Kelompok")
    st.write("Pilih satu bisnis nyata di sekitar Anda.")
    st.markdown("""
    **Output analisis:**
    1. Profil singkat bisnis.
    2. Masalah utama.
    3. Current process.
    4. Peluang digital.
    5. Solusi transformasi.
    6. Dampak terhadap customer, process, data, people, dan business model.
    7. Minimal 3 KPI.
    8. Roadmap implementasi.
    9. Risiko dan mitigasi.
    """)

# -----------------------------
# QUIZ
# -----------------------------
elif menu == "🏆 Kuis 10 Soal":
    st.subheader("Kuis Transformasi Digital")
    st.caption("Pilih satu jawaban pada setiap soal, lalu klik Periksa Jawaban.")

    if "quiz_submitted" not in st.session_state:
        st.session_state.quiz_submitted = False

    for i, item in enumerate(quiz):
        st.markdown(
            f'<div class="quiz-box"><b>Soal {i+1}.</b> {item["q"]}</div>',
            unsafe_allow_html=True,
        )
        st.radio(
            "Pilih jawaban:",
            item["options"],
            key=f"q_{i}",
            index=None,
            label_visibility="collapsed",
        )

        if st.session_state.quiz_submitted:
            selected = st.session_state.get(f"q_{i}")
            if selected is None:
                st.warning("Belum dijawab.")
            else:
                idx = item["options"].index(selected)
                if idx == item["answer"]:
                    st.success("Jawaban benar.")
                else:
                    st.error(f"Jawaban yang tepat: {item['options'][item['answer']]}")
                st.caption(item["explanation"])
        st.divider()

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("✅ Periksa Jawaban", use_container_width=True):
            st.session_state.quiz_submitted = True
            st.rerun()
    with col2:
        if st.button("🔄 Ulangi Kuis", use_container_width=True):
            for i in range(len(quiz)):
                st.session_state.pop(f"q_{i}", None)
            st.session_state.quiz_submitted = False
            st.rerun()

    if st.session_state.quiz_submitted:
        score = 0
        answered = 0
        for i, item in enumerate(quiz):
            selected = st.session_state.get(f"q_{i}")
            if selected is not None:
                answered += 1
                if item["options"].index(selected) == item["answer"]:
                    score += 1

        st.subheader("Hasil Kuis")
        c1, c2, c3 = st.columns(3)
        c1.metric("Skor", f"{score}/10")
        c2.metric("Nilai", f"{score * 10}")
        c3.metric("Terjawab", f"{answered}/10")

        if score >= 8:
            st.success("Sangat baik. Pemahaman konsep sudah kuat.")
        elif score >= 6:
            st.info("Cukup baik. Review kembali bagian yang masih salah.")
        else:
            st.warning("Perlu review materi sebelum mencoba kuis kembali.")

# -----------------------------
# GLOSARIUM
# -----------------------------
elif menu == "📖 Glosarium Istilah":
    st.subheader("Glosarium Istilah Transformasi Digital")
    st.write("Setiap istilah teknis yang digunakan dalam aplikasi dijelaskan di sini dengan bahasa sederhana.")

    search_term = st.text_input(
        "🔎 Cari istilah",
        placeholder="Contoh: CRM, KPI, API, Cloud, Dashboard, POS..."
    )

    if search_term.strip():
        q = search_term.lower().strip()
        filtered = {
            term: definition
            for term, definition in glossary.items()
            if q in term.lower() or q in definition.lower()
        }
    else:
        filtered = glossary

    st.caption(f"{len(filtered)} istilah ditampilkan.")

    for term, definition in filtered.items():
        with st.expander(term):
            st.write(definition)

    st.markdown("""
    <div class="note">
    <b>Tips untuk mahasiswa:</b> Jangan hanya menghafal singkatan.
    Pahami <b>fungsi istilah tersebut dalam proses bisnis</b>.
    </div>
    """, unsafe_allow_html=True)

# -----------------------------
# RINGKASAN
# -----------------------------
elif menu == "✅ Ringkasan":
    st.subheader("Ringkasan Pertemuan")
    st.markdown("""
    **Inti materi yang perlu diingat:**

    - Transformasi Digital lebih luas daripada sekadar memakai teknologi.
    - **Digitization** = mengubah bentuk data.
    - **Digitalization** = menggunakan teknologi untuk memperbaiki proses.
    - **Digital Transformation** = perubahan lebih luas pada cara organisasi bekerja dan menciptakan nilai.
    - Area perubahan dapat mencakup **customer, process, data, people, technology, ecosystem, governance, dan business model**.
    - Analisis transformasi sebaiknya dimulai dari **masalah dan tujuan bisnis**, bukan dari teknologi.
    - KPI digunakan untuk mengetahui apakah perubahan benar-benar menghasilkan nilai.
    """)

    st.markdown("""
    <div class="flow">
    Business Problem → Digital Opportunity → Transformation Design → Implementation → KPI → Continuous Improvement
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="note">
    <b>Pesan utama:</b> Teknologi adalah enabler. Transformasi Digital berhasil jika perubahan teknologi
    menghasilkan perbaikan yang relevan terhadap proses, pelanggan, organisasi, atau penciptaan nilai bisnis.
    </div>
    """, unsafe_allow_html=True)

# -----------------------------
# REFERENSI
# -----------------------------
elif menu == "📚 Referensi":
    st.subheader("Referensi")
    st.markdown("### Sumber utama RPS")
    st.write(
        "Aagaard, A. (Ed.). (2019). *Digital Business Models Driving Transformation and Innovation*. Springer."
    )

    st.markdown("### Referensi jurnal pendukung")
    refs = [
        "Gong, C., & Ribiere, V. (2021). Developing a unified definition of digital transformation. Technovation, 102, 102217. DOI: 10.1016/j.technovation.2020.102217.",
        "Hanelt, A., Bohnsack, R., Marz, D., & Antunes Marante, C. (2021). A systematic review of the literature on digital transformation: Insights and implications for strategy and organizational change. Journal of Management Studies, 58(5), 1159–1197. DOI: 10.1111/joms.12639.",
        "Trischler, M. F. G., & Li-Ying, J. (2023). Digital business model innovation: Toward construct clarity and future research directions. Review of Managerial Science, 17, 3–32. DOI: 10.1007/s11846-021-00508-2.",
        "Plekhanov, D., Franke, H., & Netland, T. H. (2023). Digital transformation: A review and research agenda. European Management Journal, 41(6), 821–844.",
        "Kao, L.-J., Chiu, C.-C., Lin, H.-T., Hung, Y.-W., & Lu, C.-C. (2024). Unveiling the dimensions of digital transformation: A comprehensive taxonomy and assessment model for business. Journal of Business Research, 176, 114595. DOI: 10.1016/j.jbusres.2024.114595.",
        "Lin, Q. (2025). A meta-analytic investigation of digital transformation: Antecedents, consequences, and contingencies. Journal of Business Research, 200, 115643. DOI: 10.1016/j.jbusres.2025.115643.",
    ]
    for r in refs:
        st.markdown("- " + r)

    st.markdown("### Catatan penggunaan")
    st.caption(
        "Referensi digunakan untuk memperkuat materi konseptual. Studi kasus di aplikasi merupakan kasus pembelajaran/fiktif agar mahasiswa fokus pada proses analisis."
    )

st.divider()
st.caption(
    "Materi Transformasi Digital — Bisnis Digital | Sub-CPMK: Mahasiswa mampu memahami Transformasi Digital | "
    "Kuliah • Diskusi • Studi Kasus • Latihan • Kuis"
)
