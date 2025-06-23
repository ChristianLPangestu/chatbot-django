PROMPTS = {
    "emphatize": [
        {
            "prompt": "Sebagai peneliti UX, bantu saya membuat 5 pertanyaan wawancara untuk memahami kebutuhan pengguna aplikasi [topik].",
            "label": "Pertanyaan Kebutuhan Pengguna",
            "tooltip": "Menggali kebutuhan eksplisit dan implisit pengguna terhadap aplikasi tertentu.",
        },
        {
            "prompt": "Sebagai ahli riset pengguna, buatkan saya daftar pertanyaan yang menggali frustrasi pengguna saat menggunakan [jenis aplikasi].",
            "label": "Frustrasi Pengguna",
            "tooltip": "Mengungkap hambatan emosional atau pain point saat menggunakan aplikasi serupa.",
        },
        {
            "prompt": "Sebagai fasilitator design thinking, berikan 5 pertanyaan untuk memahami rutinitas dan harapan pengguna [target user].",
            "label": "Rutinitas dan Harapan",
            "tooltip": "Memahami konteks kehidupan dan ekspektasi pengguna dalam menggunakan aplikasi.",
        },
        {
            "prompt": "Saya ingin memahami pola pikir pengguna. Sebagai pakar behavioral research, bantu saya membuat panduan wawancara pendek.",
            "label": "Pola Pikir Pengguna",
            "tooltip": "Menggali sikap, nilai, dan cara berpikir pengguna dari sudut pandang psikologis.",
        },
        {
            "prompt": "Sebagai coach design sprint, buat template wawancara 5W1H untuk mengeksplorasi pengalaman pengguna saat [aktivitas tertentu].",
            "label": "Wawancara 5W1H",
            "tooltip": "Menggunakan kerangka 5W1H untuk mengeksplorasi pengalaman pengguna secara menyeluruh.",
        },
    ],
    "define": [
        {
            "prompt": "Sebagai pakar design thinking, bantu saya menyusun problem statement dengan format “User membutuhkan … karena …” dari data ini: “[kutipan wawancara]”.",
            "label": "Susun Problem Statement",
            "tooltip": "Membantu menyusun pernyataan masalah terstruktur untuk tahap ideasi.",
        },
        {
            "prompt": "Sebagai mentor inovasi produk, ubah insight berikut menjadi kebutuhan pengguna: “[insight]”.",
            "label": "Ubah Insight Jadi Kebutuhan",
            "tooltip": "Mengubah insight dari riset menjadi kebutuhan eksplisit pengguna.",
        },
        {
            "prompt": "Saya ingin mengklarifikasi pain point. Sebagai analis user journey, bantu saya menguraikan masalah utama dari kutipan ini.",
            "label": "Klarifikasi Pain Point",
            "tooltip": "Mengisolasi titik masalah utama dari pengalaman pengguna.",
        },
        {
            "prompt": "Sebagai fasilitator workshop design, identifikasi kebutuhan implisit dalam kutipan pengguna berikut.",
            "label": "Kebutuhan Implisit",
            "tooltip": "Mengungkap kebutuhan tersirat dari cerita atau kutipan pengguna.",
        },
        {
            "prompt": "Sebagai UX strategist, ringkas hasil wawancara menjadi 1 kalimat masalah inti.",
            "label": "Ringkas Masalah Inti",
            "tooltip": "Menyaring hasil wawancara menjadi satu kalimat yang merepresentasikan masalah utama.",
        },
    ],
    "ideate": [
        {
            "prompt": "Sebagai fasilitator kreatif, berikan saya 5 ide menggunakan metode How Might We dari problem ini: “[problem]”.",
            "label": "Ide How Might We",
            "tooltip": "Mengubah masalah menjadi pertanyaan terbuka dan menghasilkan ide kreatif dari pendekatan How Might We.",
        },
        {
            "prompt": "Sebagai mentor startup, bantu saya menggunakan SCAMPER untuk mengeksplorasi solusi dari masalah berikut.",
            "label": "Eksplorasi dengan SCAMPER",
            "tooltip": "Mengeksplorasi ide berdasarkan pendekatan SCAMPER (Substitute, Combine, Adapt, Modify, Put to other use, Eliminate, Reverse).",
        },
        {
            "prompt": "Sebagai inovator produk digital, beri saya 5 solusi dengan pendekatan minimal viable feature untuk [problem].",
            "label": "Solusi MVP",
            "tooltip": "Menghasilkan ide solusi minimum bernilai (MVP) agar cepat diuji melalui prototipe awal.",
        },
        {
            "prompt": "Saya butuh ide yang unik dan menyenangkan. Sebagai creative consultant, bantu saya eksplorasi gamifikasi untuk masalah berikut.",
            "label": "Ide Gamifikasi",
            "tooltip": "Menghasilkan solusi berbasis gamifikasi agar lebih interaktif dan menarik bagi pengguna.",
        },
        {
            "prompt": "Sebagai pengajar design thinking, bantu saya membuat brainstorming canvas digital berisi 5 ide untuk tantangan ini.",
            "label": "Brainstorming Canvas",
            "tooltip": "Membuat kerangka visual untuk mengelompokkan dan merancang ide secara sistematis.",
        },
    ],
    "prototype": [
        {
            "prompt": "Sebagai desainer UI/UX profesional, bantu saya menjelaskan prototipe awal dari ide ini dalam bentuk layout dan alur interaksi.",
            "label": "Deskripsi Prototipe Awal",
            "tooltip": "Memvisualisasikan ide ke dalam layout dan alur interaksi awal aplikasi.",
        },
        {
            "prompt": "Saya ingin tahu struktur UI untuk fitur berikut: “[fitur]”. Sebagai developer UX, bantu saya merancang wireframe deskriptifnya.",
            "label": "Wireframe Fitur",
            "tooltip": "Membuat wireframe deskriptif untuk struktur UI dari fitur tertentu.",
        },
        {
            "prompt": "Sebagai mentor UI design, tolong buat sketsa verbal dari halaman utama aplikasi [topik].",
            "label": "Sketsa Verbal Halaman Utama",
            "tooltip": "Menyusun deskripsi urut dan intuitif dari tampilan halaman utama aplikasi.",
        },
        {
            "prompt": "Sebagai ahli produk digital, bantu saya menjelaskan elemen utama dari prototipe [ide pilihan].",
            "label": "Elemen Utama Prototipe",
            "tooltip": "Mengidentifikasi komponen penting dari prototipe untuk mendukung kebutuhan pengguna.",
        },
        {
            "prompt": "Sebagai reviewer UX prototyping, bantu saya menyusun spesifikasi antarmuka awal untuk fitur ini.",
            "label": "Spesifikasi Antarmuka Awal",
            "tooltip": "Merinci aspek fungsional dan visual dari fitur sebagai dasar pengujian awal.",
        },
    ],
    "test": [
        {
            "prompt": "Sebagai fasilitator usability testing, bantu saya menyusun 3 pertanyaan untuk menguji prototipe berikut: “[deskripsi prototipe]”.",
            "label": "Pertanyaan Usability Testing",
            "tooltip": "Menyusun pertanyaan untuk menguji kemudahan, pemahaman, dan kenyamanan saat menggunakan prototipe.",
        },
        {
            "prompt": "Sebagai evaluator UX, bantu saya buat checklist validasi awal sebelum tes prototipe [nama fitur].",
            "label": "Checklist Pra-Uji Prototipe",
            "tooltip": "Daftar pemeriksaan komponen penting sebelum prototipe diuji.",
        },
        {
            "prompt": "Saya ingin mengumpulkan masukan. Sebagai expert design researcher, buat 1 pertanyaan feedback terbuka yang tepat.",
            "label": "Pertanyaan Feedback Terbuka",
            "tooltip": "Pertanyaan reflektif untuk mendapatkan masukan luas dan mendalam dari pengguna.",
        },
        {
            "prompt": "Sebagai coach pengujian produk, bantu saya menyusun skenario testing untuk alur login aplikasi ini.",
            "label": "Skenario Testing Alur Login",
            "tooltip": "Langkah-langkah realistis untuk menguji fungsi login dari perspektif pengguna.",
        },
        {
            "prompt": "Sebagai penguji UX profesional, beri saya format penilaian yang bisa digunakan dalam pengujian terbimbing.",
            "label": "Format Penilaian UX Testing",
            "tooltip": "Template evaluasi untuk mencatat observasi dan skor selama sesi pengujian.",
        },
    ],
}
