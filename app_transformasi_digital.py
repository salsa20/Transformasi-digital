import streamlit as st

st.set_page_config(page_title="Transformasi Digital", page_icon="💻", layout="wide")

st.title("Transformasi Digital")
st.caption("Bisnis Digital | Kuliah • Diskusi • Studi Kasus • Kuis • Latihan")

quiz_questions = [{'q': 'Mana yang paling tepat menggambarkan Transformasi Digital?', 'options': ['Mengubah dokumen kertas menjadi PDF', 'Menggunakan komputer untuk mengetik laporan', 'Mengubah proses dan cara perusahaan menciptakan nilai dengan memanfaatkan teknologi digital', 'Membeli software baru untuk kantor'], 'answer': 2}, {'q': 'Sebuah toko mengubah formulir pemesanan manual menjadi formulir online yang otomatis masuk database. Ini paling tepat disebut...', 'options': ['Digitization', 'Digitalization', 'Transformasi model bisnis', 'Diversifikasi'], 'answer': 1}, {'q': 'Sebelum memilih teknologi dalam transformasi digital, langkah yang paling tepat adalah...', 'options': ['Membeli teknologi paling mahal', 'Mengidentifikasi masalah dan tujuan bisnis', 'Mengikuti teknologi yang sedang tren', 'Mengganti seluruh karyawan'], 'answer': 1}, {'q': 'Contoh perubahan yang paling jelas pada business model adalah...', 'options': ['Mengganti printer', 'Memindahkan file Excel ke cloud', 'Mengubah sumber pendapatan dari penjualan satu kali menjadi model subscription', 'Mengganti warna logo'], 'answer': 2}, {'q': 'Mengapa kualitas data penting dalam transformasi digital?', 'options': ['Karena semua teknologi harus menggunakan data yang besar', 'Karena data mendukung pengambilan keputusan dan otomatisasi yang lebih baik', 'Karena data menggantikan seluruh keputusan manajer', 'Karena data membuat teknologi selalu berhasil'], 'answer': 1}, {'q': 'Mana yang merupakan tantangan transformasi digital?', 'options': ['Resistensi terhadap perubahan', 'Tidak adanya kebutuhan pelanggan', 'Semua proses otomatis tanpa risiko', 'Teknologi selalu murah'], 'answer': 0}, {'q': 'Toko menggunakan POS, CRM, dashboard, dan online ordering yang terhubung. Perubahan ini terutama menunjukkan...', 'options': ['Integrasi proses dan data', 'Penghapusan data', 'Digitalisasi dokumen saja', 'Pengurangan kebutuhan pelanggan'], 'answer': 0}, {'q': 'KPI yang paling relevan untuk menilai apakah online ordering memperbaiki proses pemesanan adalah...', 'options': ['Warna website', 'Order completion rate', 'Jumlah komputer kantor', 'Jumlah halaman SOP'], 'answer': 1}, {'q': 'Dalam studi kasus, mengapa mahasiswa perlu memahami kondisi bisnis sebelum memilih solusi teknologi?', 'options': ['Agar solusi menjawab masalah nyata dan menghasilkan nilai bisnis', 'Agar selalu menggunakan AI', 'Agar semua perusahaan memiliki sistem yang sama', 'Agar implementasi menjadi lebih mahal'], 'answer': 0}, {'q': 'Pernyataan yang paling tepat adalah...', 'options': ['Transformasi digital hanya masalah IT', 'Transformasi digital selalu membutuhkan AI', 'Transformasi digital dapat melibatkan teknologi, proses, manusia, strategi, data, dan model bisnis', 'Transformasi digital selesai setelah aplikasi diluncurkan'], 'answer': 2}]

with st.sidebar:
    st.header("RPS")
    st.markdown("""
**Sub-CPMK:** Mahasiswa mampu memahami Transformasi Digital.

**Indikator:** Memahami Transformasi Digital.

**Kriteria:** Mahasiswa mampu menjelaskan Transformasi Digital dan menghubungkannya dengan perubahan proses, pengalaman pelanggan, model bisnis, data, SDM/budaya, dan teknologi.

**Bentuk pembelajaran:** Kuliah; Diskusi

**TM:** 1 × (2 × 50 menit)

**Tugas:** Analisis studi kasus Transformasi Digital.

**PT + BM:** (1 + 1) × (2 × 60 menit)
""")
    page = st.radio("Menu", ["Materi", "Studi Kasus", "Kuis", "Latihan", "Referensi"])

if page == "Materi":
    st.header("Materi Transformasi Digital")
    st.subheader("1. Pengertian")
    st.write("Transformasi Digital adalah perubahan organisasi yang dipicu dan dibentuk oleh penyebaran teknologi digital sehingga perusahaan dapat mengubah cara bekerja, menciptakan nilai, berinteraksi dengan pelanggan, dan menjalankan model bisnis.")
    st.info("Cara mudah mengingat: teknologi berubah → proses berubah → pengalaman pelanggan berubah → cara bisnis menciptakan nilai ikut berubah.")

    st.subheader("2. Digitization vs Digitalization vs Digital Transformation")
    st.dataframe({
        "Konsep": ["Digitization", "Digitalization", "Digital Transformation"],
        "Fokus": [
            "Mengubah data analog menjadi digital",
            "Memanfaatkan teknologi digital untuk memperbaiki proses",
            "Mengubah proses, organisasi, pengalaman pelanggan, dan/atau model bisnis"
        ],
        "Contoh": [
            "Nota kertas → PDF",
            "Form manual → form online terintegrasi",
            "Toko fisik → omnichannel + CRM + analytics"
        ]
    }, use_container_width=True)

    st.subheader("3. Area perubahan")
    cols = st.columns(4)
    areas = [
        ("Customer", "Experience dan kanal digital"),
        ("Process", "Otomatisasi dan integrasi"),
        ("Business Model", "Value proposition dan revenue"),
        ("Data", "Dashboard, analytics, AI"),
        ("People", "Skill dan budaya"),
        ("Technology", "Cloud, API, AI, IoT"),
        ("Ecosystem", "Partner dan platform"),
        ("Governance", "Risk, privacy, cybersecurity")
    ]
    for i, (name, desc) in enumerate(areas):
        with cols[i % 4]:
            st.markdown(f"**{name}**")
            st.caption(desc)

    st.subheader("4. Pendorong")
    st.markdown("- Perubahan perilaku pelanggan\n- Persaingan digital\n- Efisiensi dan otomatisasi\n- Keputusan berbasis data\n- Perkembangan AI, cloud, dan platform\n- Perubahan model bisnis dan ekosistem")

    st.subheader("5. Tantangan")
    st.markdown("- Resistensi terhadap perubahan\n- Kesenjangan kompetensi digital\n- Legacy system\n- Investasi dan prioritas teknologi\n- Keamanan dan privasi data\n- Perubahan proses dan budaya\n- Risiko transformasi tidak menghasilkan nilai bisnis")

    st.subheader("6. Business Model")
    st.markdown("Transformasi dapat mengubah **value proposition, customer segment, channel, customer relationship, revenue model, key activities/resources, dan partner/ecosystem**.")

    st.subheader("7. Prinsip utama")
    st.success("Mulai dari masalah dan tujuan bisnis → rancang perubahan → pilih teknologi yang relevan → ukur hasil dengan KPI.")

    st.subheader("8. Metode Studi Kasus")
    st.markdown("""
1. Understand the Business — pahami bisnis, pelanggan, dan sumber pendapatan.
2. Identify the Problem — temukan masalah berdasarkan fakta/data.
3. Map the Current Process — petakan proses saat ini.
4. Identify the Digital Opportunity — tentukan peluang digital.
5. Design the Transformation — rancang perubahan proses, pelanggan, data, SDM, dan model bisnis.
6. Define KPI — tentukan indikator keberhasilan.
7. Recommend & Justify — pilih prioritas dan jelaskan alasannya.
""")

elif page == "Studi Kasus":
    st.header("Studi Kasus: Toko Sinar Jaya")
    st.write("Toko Sinar Jaya adalah toko retail fiktif yang menjual perlengkapan rumah tangga. Transaksi dicatat menggunakan nota dan spreadsheet. Promosi dilakukan melalui WhatsApp secara manual.")
    st.dataframe({
        "Indikator": ["Transaksi per bulan", "Transaksi terlambat dicatat", "Pesanan perlu konfirmasi ulang karena stok", "Permintaan pemesanan online"],
        "Kondisi": ["2.000", "15%", "8%", "Mulai meningkat"]
    }, use_container_width=True)

    st.subheader("Peran mahasiswa")
    st.write("Anda berperan sebagai **Business Transformation Supervisor**.")
    st.markdown("""
**Tugas analisis:**
1. Identifikasi 3 masalah utama.
2. Petakan proses saat ini.
3. Usulkan solusi digital.
4. Jelaskan perubahan pada customer experience, proses, data, SDM/budaya, dan model bisnis.
5. Tentukan minimal 3 KPI.
6. Susun roadmap jangka pendek, menengah, dan panjang.
7. Identifikasi risiko dan mitigasinya.
""")
    with st.expander("Contoh arah jawaban"):
        st.markdown("""
- Jangka pendek: POS + inventory terintegrasi.
- Menengah: online ordering + dashboard.
- Lanjutan: CRM/customer segmentation dan analytics.
- KPI: stock accuracy, order completion rate, waktu pembuatan laporan, conversion rate.
""")

elif page == "Kuis":
    st.header("Kuis Pemahaman")
    st.write("Pilih satu jawaban terbaik pada setiap pertanyaan.")
    selected = []
    for i, item in enumerate(quiz_questions):
        selected.append(st.radio(item["q"], item["options"], key=f"q{i}"))
    if st.button("Hitung Nilai", type="primary"):
        score = 0
        for i, item in enumerate(quiz_questions):
            if selected[i] == item["options"][item["answer"]]:
                score += 1
        pct = score / len(quiz_questions) * 100
        st.success(f"Skor: {score}/{len(quiz_questions)} ({pct:.0f}%)")
        with st.expander("Lihat kunci jawaban"):
            for i, item in enumerate(quiz_questions, 1):
                st.write(f"{i}. {item['options'][item['answer']]}")

elif page == "Latihan":
    st.header("Latihan / Tugas Studi Kasus")
    st.markdown("""
Pilih satu bisnis nyata di sekitar Anda, misalnya toko retail, UMKM kuliner, laundry, gym, kampus, atau jasa.

**Analisis:**
1. Jelaskan kondisi bisnis saat ini.
2. Identifikasi minimal 3 masalah yang dapat dibantu transformasi digital.
3. Bedakan masalah yang hanya membutuhkan digitalisasi proses dengan masalah yang membutuhkan perubahan lebih besar.
4. Usulkan solusi digital.
5. Jelaskan perubahan pada Customer Experience, Business Process, Data & Analytics, People & Culture, dan Business Model.
6. Tentukan minimal 3 KPI.
7. Buat roadmap jangka pendek, menengah, dan panjang.
8. Jelaskan risiko utama dan mitigasinya.
""")
    st.text_area("Nama bisnis", height=60)
    st.text_area("Masalah utama", height=100)
    st.text_area("Solusi transformasi digital", height=100)
    st.text_area("KPI", height=100)
    st.text_area("Roadmap", height=100)
    st.text_area("Risiko dan mitigasi", height=100)
    st.info("PT + BM: (1 + 1) × (2 × 60 menit).")

else:
    st.header("Referensi")
    refs = [
        "Aagaard, A. (Ed.). (2019). Digital Business Models Driving Transformation and Innovation. Springer.",
        "Hanelt, A., Bohnsack, R., Marz, D., & Antunes Marante, C. (2021). A Systematic Review of the Literature on Digital Transformation: Insights and Implications for Strategy and Organizational Change. Journal of Management Studies, 58(5), 1159–1197. DOI: 10.1111/joms.12639.",
        "Trischler, M. F. G., & Li-Ying, J. (2022/2023). Digital business model innovation: toward construct clarity and future research directions. Review of Managerial Science, 17, 3–32. DOI: 10.1007/s11846-021-00508-2.",
        "Alshammari, K. (2023). Investigating the Factors That Influence Digital Transformation: A Systematic Literature Review. iRASD Journal of Management, 5(2), 62–73. DOI: 10.52131/jom.2023.0502.0107.",
        "Kao, L.-J., Chiu, C.-C., Lin, H.-T., Hung, Y.-W., & Lu, C.-C. (2024). Unveiling the dimensions of digital transformation: A comprehensive taxonomy and assessment model for business. Journal of Business Research, 176, 114595. DOI: 10.1016/j.jbusres.2024.114595.",
        "Lin, Q. (2025). A meta-analytic investigation of digital transformation: Antecedents, consequences, and contingencies. Journal of Business Research, 200, 115643. DOI: 10.1016/j.jbusres.2025.115643."
    ]
    for r in refs:
        st.markdown("- " + r)

# End
