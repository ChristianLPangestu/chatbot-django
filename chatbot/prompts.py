PROMPTS = {
    "emphatize": [
        {
            "prompt": "Sebagai peneliti UX, bantu saya membuat 5 pertanyaan wawancara untuk memahami kebutuhan pengguna aplikasi [topik].",
            "label": "Membuat pertanyaan wawancara",
            "tooltip": "Membantu pengguna untuk mengidentifikasi dan memahami kebutuhan eksplisit dan implisit dari target user terhadap aplikasi tertentu."
        },
        {
            "prompt": "Sebagai ahli riset pengguna, buatkan saya daftar pertanyaan yang menggali frustrasi pengguna saat menggunakan [jenis aplikasi].",
            "label": "Menggali frustrasi pengguna",
            "tooltip": "Fokus menggali pain point atau hambatan emosional yang dialami pengguna selama menggunakan produk serupa."
        },
        {
            "prompt": "Sebagai fasilitator design thinking, berikan 5 pertanyaan untuk memahami rutinitas dan harapan pengguna [target user].",
            "label": "Memahami rutinitas dan harapan user",
            "tooltip": "Mengarahkan user agar dapat memahami konteks kehidupan pengguna (daily life, goals) yang relevan dengan penggunaan produk."
        },
        {
            "prompt": "Saya ingin memahami pola pikir pengguna. Sebagai pakar behavioral research, bantu saya membuat panduan wawancara pendek.",
            "label": "Panduan wawancara pendek",
            "tooltip": "Meningkatkan pemahaman terhadap sikap, nilai, dan pola berpikir target pengguna dengan pendekatan psikologis atau perilaku."
        },
        {
            "prompt": "Sebagai coach design sprint, buat template wawancara 5W1H untuk mengeksplorasi pengalaman pengguna saat [aktivitas tertentu].",
            "label": "Template 5W1H wawancara",
            "tooltip": "Menyusun kerangka pertanyaan terstruktur dan menyeluruh (apa, siapa, kapan, di mana, mengapa, dan bagaimana) untuk eksplorasi konteks penggunaan."
        }
    ],
    "define": [
        {
            "prompt": "Sebagai pakar design thinking, bantu saya menyusun problem statement dengan format “User membutuhkan … karena …” dari data ini: “[kutipan wawancara]”.",
            "label": "Susun problem statement",
            "tooltip": "Membantu pengguna menyusun problem statement terstruktur dengan format standar untuk mempermudah tahap ideasi."
        },
        {
            "prompt": "Sebagai mentor inovasi produk, ubah insight berikut menjadi kebutuhan pengguna: “[insight]”.",
            "label": "Konversi insight jadi kebutuhan",
            "tooltip": "Membantu pengguna mengubah hasil observasi atau wawancara (insight) menjadi pernyataan kebutuhan eksplisit."
        },
        {
            "prompt": "Saya ingin mengklarifikasi pain point. Sebagai analis user journey, bantu saya menguraikan masalah utama dari kutipan ini.",
            "label": "Klarifikasi pain point",
            "tooltip": "Membantu pengguna menafsirkan kutipan agar dapat mengisolasi titik masalah paling menyakitkan dari pengalaman pengguna."
        },
        {
            "prompt": "Sebagai fasilitator workshop design, identifikasi kebutuhan implisit dalam kutipan pengguna berikut.",
            "label": "Identifikasi kebutuhan implisit",
            "tooltip": "Membantu menemukan kebutuhan tersirat yang belum dikatakan secara langsung oleh pengguna, berdasarkan kutipan atau cerita."
        },
        {
            "prompt": "Sebagai UX strategist, ringkas hasil wawancara menjadi 1 kalimat masalah inti.",
            "label": "Ringkas insight jadi masalah inti",
            "tooltip": "Membantu pengguna menyaring informasi menjadi kalimat yang singkat, padat, dan merepresentasikan masalah utama."
        }
    ],
    "ideate": [
        {
            "prompt": "Sebagai fasilitator kreatif, berikan saya 5 ide menggunakan metode How Might We dari problem ini: “[problem]”.",
            "label": "Ide dengan HMW",
            "tooltip": "Membantu pengguna mengubah pernyataan masalah menjadi bentuk pertanyaan terbuka (How Might We) dan menghasilkan solusi kreatif dari setiap pertanyaan tersebut."
        },
        {
            "prompt": "Sebagai mentor startup, bantu saya menggunakan SCAMPER untuk mengeksplorasi solusi dari masalah berikut.",
            "label": "Eksplorasi SCAMPER",
            "tooltip": "Membantu pengguna mengeksplorasi solusi dengan pendekatan SCAMPER (Substitute, Combine, Adapt, Modify, Put to other use, Eliminate, Reverse)."
        },
        {
            "prompt": "Sebagai inovator produk digital, beri saya 5 solusi dengan pendekatan minimal viable feature untuk [problem].",
            "label": "Solusi berbasis MVF",
            "tooltip": "Mengarahkan pengguna menghasilkan solusi sederhana yang tetap bernilai (MVP), guna mempercepat pengujian ide ke tahap prototipe."
        },
        {
            "prompt": "Saya butuh ide yang unik dan menyenangkan. Sebagai creative consultant, bantu saya eksplorasi gamifikasi untuk masalah berikut.",
            "label": "Eksplorasi gamifikasi",
            "tooltip": "Mendorong pengguna menghasilkan solusi dengan pendekatan gamifikasi agar ide menjadi lebih menarik, interaktif, dan menyenangkan bagi pengguna akhir."
        },
        {
            "prompt": "Sebagai pengajar design thinking, bantu saya membuat brainstorming canvas digital berisi 5 ide untuk tantangan ini.",
            "label": "Brainstorming canvas digital",
            "tooltip": "Membantu pengguna merancang kerangka brainstorming visual yang terstruktur untuk menyusun dan mengelompokkan ide dengan lebih sistematis."
        }
    ],
    "prototype": [
        {
            "prompt": "Sebagai desainer UI/UX profesional, bantu saya menjelaskan prototipe awal dari ide ini dalam bentuk layout dan alur interaksi.",
            "label": "Jelaskan prototipe awal",
            "tooltip": "Membantu pengguna memvisualisasikan ide menjadi struktur antarmuka awal yang mencakup tata letak elemen dan alur navigasi."
        },
        {
            "prompt": "Saya ingin tahu struktur UI untuk fitur berikut: “[fitur]”. Sebagai developer UX, bantu saya merancang wireframe deskriptifnya.",
            "label": "Struktur UI fitur",
            "tooltip": "Membimbing pengguna membuat deskripsi wireframe atau sketsa logis dari UI untuk fitur spesifik, sebagai dasar pengembangan visual."
        },
        {
            "prompt": "Sebagai mentor UI design, tolong buat sketsa verbal dari halaman utama aplikasi [topik].",
            "label": "Sketsa verbal halaman utama",
            "tooltip": "Membantu pengguna menyusun narasi deskriptif tentang tampilan halaman utama secara urut dan intuitif."
        },
        {
            "prompt": "Sebagai ahli produk digital, bantu saya menjelaskan elemen utama dari prototipe [ide pilihan].",
            "label": "Jelaskan elemen utama",
            "tooltip": "Mengarahkan pengguna untuk mengidentifikasi komponen penting (button, input, visual cue) dalam prototipe agar sesuai kebutuhan user."
        },
        {
            "prompt": "Sebagai reviewer UX prototyping, bantu saya menyusun spesifikasi antarmuka awal untuk fitur ini.",
            "label": "Spesifikasi antarmuka awal",
            "tooltip": "Membantu pengguna merinci aspek fungsional dan visual dari sebuah fitur dalam bentuk spesifikasi awal untuk pengujian."
        }
    ],
    "test": [
        {
            "prompt": "Sebagai fasilitator usability testing, bantu saya menyusun 3 pertanyaan untuk menguji prototipe berikut: “[deskripsi prototipe]”.",
            "label": "Pertanyaan usability testing",
            "tooltip": "Membantu pengguna merancang pertanyaan yang mengevaluasi kemudahan penggunaan, pemahaman fitur, dan kenyamanan saat berinteraksi dengan prototipe."
        },
        {
            "prompt": "Sebagai evaluator UX, bantu saya buat checklist validasi awal sebelum tes prototipe [nama fitur].",
            "label": "Checklist validasi awal",
            "tooltip": "Menyediakan daftar pemeriksaan (pre-test checklist) agar prototipe siap diuji dan seluruh komponen penting sudah tersedia."
        },
        {
            "prompt": "Saya ingin mengumpulkan masukan. Sebagai expert design researcher, buat 1 pertanyaan feedback terbuka yang tepat.",
            "label": "Pertanyaan feedback terbuka",
            "tooltip": "Membantu pengguna mendapatkan umpan balik reflektif dari user yang bersifat luas, mendalam, dan tidak mengarahkan."
        },
        {
            "prompt": "Sebagai coach pengujian produk, bantu saya menyusun skenario testing untuk alur login aplikasi ini.",
            "label": "Skenario testing login",
            "tooltip": "Membantu menyusun langkah-langkah realistis yang akan dilalui pengguna saat menguji sebuah fungsi secara end-to-end."
        },
        {
            "prompt": "Sebagai penguji UX profesional, beri saya format penilaian yang bisa digunakan dalam pengujian terbimbing.",
            "label": "Format penilaian UX",
            "tooltip": "Menyediakan template atau format evaluasi yang dapat digunakan untuk mencatat observasi dan skor selama sesi usability testing."
        }
    ]
}
