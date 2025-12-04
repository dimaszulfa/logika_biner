import streamlit as st

# Atur judul tab browser
st.set_page_config(page_title="Edukasi Logika & Bilangan Biner", layout="wide")

# -- Fungsi materi logika --
def materi_logika():
    st.header("Materi Logika Dasar")
    st.write("""
    Logika digital adalah sistem yang menggunakan nilai 0 dan 1 untuk merepresentasikan kondisi False dan True.
    
    Gerbang logika dasar meliputi:
    - AND
    - OR
    - NOT
    - NAND
    - NOR
    - XOR
    - XNOR

    Contoh Tabel Kebenaran Gerbang AND:
    """)
    st.image("images/and_truth_table.png", caption="Tabel Kebenaran Gerbang AND")

# -- Fungsi materi bilangan biner --
def materi_biner():
    st.header("Materi Bilangan Biner")
    st.write("""
    Bilangan biner adalah sistem bilangan yang menggunakan basis 2, hanya terdiri dari angka 0 dan 1.
    
    Contoh bilangan biner: 0, 1, 10, 11, 100, ...
    
    Bilangan biner digunakan dalam komputer untuk merepresentasikan data digital.
    """)

# -- Fungsi kuis interaktif --
def kuis():
    st.header("Kuis Interaktif")
    soal = "Apa output gerbang AND jika input A=1 dan B=0?"
    pilihan = ["0", "1", "Tidak ada jawaban"]
    jawaban = st.radio(soal, pilihan)
    if st.button("Submit"):
        if jawaban == "0":
            st.success("Benar! Output gerbang AND dengan input A=1 dan B=0 adalah 0.")
        else:
            st.error("Salah, coba lagi.")

# -- Fungsi model 3D placeholder --
def model_3d():
    st.header("Model Gerbang Logika 3D")
    st.write("Model 3D akan tampil di sini (placeholder).")

# -- Fungsi chatbot sederhana (tanpa API OpenAI) --
def chatbot():
    st.header("Chatbot AI (Simulasi)")
    user_input = st.text_input("Tanyakan sesuatu tentang logika atau bilangan biner:")
    if user_input:
        st.write("Jawaban AI: Maaf, fitur chatbot belum diaktifkan.")

# -- Fungsi tentang --
def tentang():
    st.header("Tentang Proyek")
    st.write("""
    Proyek Edukasi Logika & Bilangan Biner berbasis AI dan interaktif.
    
    Dibuat oleh [Nama Kamu].
    """)

# -- Main app --
def main():
    st.title("Edukasi Logika & Bilangan Biner")

    menu = st.sidebar.selectbox("Menu", ["Materi Logika", "Materi Bilangan Biner", "Kuis", "Model 3D", "Chatbot", "Tentang"])

    if menu == "Materi Logika":
        materi_logika()
    elif menu == "Materi Bilangan Biner":
        materi_biner()
    elif menu == "Kuis":
        kuis()
    elif menu == "Model 3D":
        model_3d()
    elif menu == "Chatbot":
        chatbot()
    elif menu == "Tentang":
        tentang()

if __name__ == "__main__":
    main()