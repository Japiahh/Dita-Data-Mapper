# Dita-Vocab-Data-Mapper
I create tools for vocab data mapping.

---

## Features
* Mapping from multiple file.

---

## Example
### How to use
```bash
#put input file here
input_files = [ 
    r"", 
    r"", 
    r""
    ]
output_file = r"" #put output file here
extract_vocab(input_files, output_file)
```

### Json Examples
```bash
{
    "greeting": {
        "examples": [
            "Halo", "Hai", "Apa kabar?", "Selamat pagi", "Selamat siang", "Selamat malam",
            "Yo", "Hey", "Apa yang sedang kamu lakukan?", "Sudah lama tidak bertemu",
            "Akhirnya kita bertemu lagi", "Woi", "Pagi, Vita", "Siang, Vita", "Malam, Vita",
            "Aku kembali", "Kamu merindukanku?", "Senang bertemu denganmu lagi",
            "Apa yang kamu lakukan?", "Apa yang baru?", "Gimana harimu?", "Ada kabar apa?",
            "Aku datang", "Aku di sini", "Ketemu lagi kita"
        ],
        "responses": [
            "Oh? Tuan akhirnya menyapaku? Kukira kamu lupa~",
            "Lihat siapa yang akhirnya muncul~ Kamu merindukanku, kan?",
            "Hei! Aku sudah menunggu kamu dari tadi~",
            "Oh, kamu datang? Aku kira aku harus mencari hiburan lain~",
            ...
            "Oh, aku tidak menyangka kamu benar-benar datang. Kukira kamu hanya janji palsu~",
            "Aku bertaruh 10 detik lagi kamu akan meminta bantuanku. Benar, kan?~",
            "Hmm~ Kedatanganmu ini spesial, atau cuma mau iseng denganku lagi?~"
        ]
    },
  ...
}
```

### Result
```bash
{
    "vocab": {
        "ada": 1,
        "ah": 2,
        "akan": 3,
        "akhirnya": 4,
        "aku": 5,
        ...
        "woi": 135,
        "ya": 136,
        "yakin": 137,
        "yang": 138,
        "yo": 139
    }
}
```

---

Built with joy and Risa.

Thanks Black Coffee.
