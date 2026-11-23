import os
import zipfile
import html

def escape_xml(s):
    return html.escape(s, quote=True)

class DocxBuilder:
    def __init__(self, title, subtitle):
        self.title = title
        self.subtitle = subtitle
        self.body_elements = []
        
        # Add Title Banner
        self.add_title_banner()

    def add_title_banner(self):
        # Subtitle / Eyebrow
        self.body_elements.append(f"""
        <w:p>
          <w:pPr>
            <w:spacing w:before="0" w:after="60"/>
          </w:pPr>
          <w:r>
            <w:rPr>
              <w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/>
              <w:b/>
              <w:sz w:val="20"/>
              <w:color w:val="0284C7"/>
            </w:rPr>
            <w:t>{escape_xml(self.subtitle.upper())}</w:t>
          </w:r>
        </w:p>""")
        
        # Main Title
        self.body_elements.append(f"""
        <w:p>
          <w:pPr>
            <w:pBdr>
              <w:bottom w:val="single" w:sz="18" w:space="8" w:color="0284C7"/>
            </w:pBdr>
            <w:spacing w:before="0" w:after="240"/>
          </w:pPr>
          <w:r>
            <w:rPr>
              <w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/>
              <w:b/>
              <w:sz w:val="38"/>
              <w:color w:val="082F49"/>
            </w:rPr>
            <w:t>{escape_xml(self.title)}</w:t>
          </w:r>
        </w:p>""")

    def add_h1(self, text):
        self.body_elements.append(f"""
        <w:p>
          <w:pPr>
            <w:spacing w:before="280" w:after="120"/>
            <w:pBdr>
              <w:bottom w:val="single" w:sz="6" w:space="4" w:color="BAE6FD"/>
            </w:pBdr>
          </w:pPr>
          <w:r>
            <w:rPr>
              <w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/>
              <w:b/>
              <w:sz w:val="28"/>
              <w:color w:val="082F49"/>
            </w:rPr>
            <w:t>{escape_xml(text)}</w:t>
          </w:r>
        </w:p>""")

    def add_h2(self, text):
        self.body_elements.append(f"""
        <w:p>
          <w:pPr>
            <w:spacing w:before="200" w:after="80"/>
          </w:pPr>
          <w:r>
            <w:rPr>
              <w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/>
              <w:b/>
              <w:sz w:val="24"/>
              <w:color w:val="0C4A6E"/>
            </w:rPr>
            <w:t>{escape_xml(text)}</w:t>
          </w:r>
        </w:p>""")

    def add_h3(self, text):
        self.body_elements.append(f"""
        <w:p>
          <w:pPr>
            <w:spacing w:before="160" w:after="60"/>
          </w:pPr>
          <w:r>
            <w:rPr>
              <w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/>
              <w:b/>
              <w:sz w:val="22"/>
              <w:color w:val="0369A1"/>
            </w:rPr>
            <w:t>{escape_xml(text)}</w:t>
          </w:r>
        </w:p>""")

    def add_paragraph(self, runs, spacing_after=120):
        # runs is list of (text, is_bold, is_italic, is_code, color)
        r_xml = []
        for run in runs:
            text = run[0]
            bold = run[1] if len(run) > 1 else False
            italic = run[2] if len(run) > 2 else False
            code = run[3] if len(run) > 3 else False
            color = run[4] if len(run) > 4 and run[4] else ("0F172A" if not code else "0369A1")
            
            rpr = ['<w:rFonts w:ascii="Consolas" w:hAnsi="Consolas"/>' if code else '<w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/>']
            rpr.append(f'<w:sz w:val="{"20" if code else "22"}"/>')
            rpr.append(f'<w:color w:val="{color}"/>')
            if bold:
                rpr.append('<w:b/>')
            if italic:
                rpr.append('<w:i/>')
            if code:
                rpr.append('<w:shd w:val="clear" w:color="auto" w:fill="F1F5F9"/>')

            r_xml.append(f"""
            <w:r>
              <w:rPr>{"".join(rpr)}</w:rPr>
              <w:t xml:space="preserve">{escape_xml(text)}</w:t>
            </w:r>""")

        self.body_elements.append(f"""
        <w:p>
          <w:pPr>
            <w:spacing w:before="0" w:after="{spacing_after}" w:line="276" w:lineRule="auto"/>
          </w:pPr>
          {"".join(r_xml)}
        </w:p>""")

    def add_callout(self, title, text):
        self.body_elements.append(f"""
        <w:p>
          <w:pPr>
            <w:pBdr>
              <w:left w:val="single" w:sz="24" w:space="12" w:color="0284C7"/>
            </w:pBdr>
            <w:shd w:val="clear" w:color="auto" w:fill="F0F9FF"/>
            <w:spacing w:before="120" w:after="160" w:line="260" w:lineRule="auto"/>
            <w:ind w:left="180" w:right="120"/>
          </w:pPr>
          <w:r>
            <w:rPr>
              <w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/>
              <w:b/>
              <w:sz w:val="21"/>
              <w:color w:val="0369A1"/>
            </w:rPr>
            <w:t>{escape_xml(title)}: </w:t>
          </w:r>
          <w:r>
            <w:rPr>
              <w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/>
              <w:sz w:val="21"/>
              <w:color w:val="0F172A"/>
            </w:rPr>
            <w:t>{escape_xml(text)}</w:t>
          </w:r>
        </w:p>""")

    def add_list_item(self, prefix, runs, level=0):
        r_xml = []
        # Prefix run
        r_xml.append(f"""
        <w:r>
          <w:rPr>
            <w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/>
            <w:b/>
            <w:sz w:val="22"/>
            <w:color w:val="0284C7"/>
          </w:rPr>
          <w:t xml:space="preserve">{escape_xml(prefix)} </w:t>
        </w:r>""")
        
        for run in runs:
            text = run[0]
            bold = run[1] if len(run) > 1 else False
            italic = run[2] if len(run) > 2 else False
            code = run[3] if len(run) > 3 else False
            color = run[4] if len(run) > 4 and run[4] else ("0F172A" if not code else "0369A1")
            
            rpr = ['<w:rFonts w:ascii="Consolas" w:hAnsi="Consolas"/>' if code else '<w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/>']
            rpr.append(f'<w:sz w:val="{"20" if code else "22"}"/>')
            rpr.append(f'<w:color w:val="{color}"/>')
            if bold:
                rpr.append('<w:b/>')
            if italic:
                rpr.append('<w:i/>')
            if code:
                rpr.append('<w:shd w:val="clear" w:color="auto" w:fill="F1F5F9"/>')

            r_xml.append(f"""
            <w:r>
              <w:rPr>{"".join(rpr)}</w:rPr>
              <w:t xml:space="preserve">{escape_xml(text)}</w:t>
            </w:r>""")

        left_ind = 480 + (level * 360)
        hang_ind = 280
        self.body_elements.append(f"""
        <w:p>
          <w:pPr>
            <w:spacing w:before="0" w:after="80" w:line="260" w:lineRule="auto"/>
            <w:ind w:left="{left_ind}" w:hanging="{hang_ind}"/>
          </w:pPr>
          {"".join(r_xml)}
        </w:p>""")

    def add_table(self, headers, rows, col_widths=None):
        total_width = 9026
        if col_widths is None:
            w = total_width // len(headers)
            col_widths = [w] * len(headers)
            col_widths[-1] = total_width - sum(col_widths[:-1])

        tbl_xml = []
        tbl_xml.append(f"""
        <w:tbl>
          <w:tblPr>
            <w:tblW w:w="{total_width}" w:type="dxa"/>
            <w:tblBorders>
              <w:top w:val="single" w:sz="6" w:space="0" w:color="CBD5E1"/>
              <w:left w:val="single" w:sz="6" w:space="0" w:color="CBD5E1"/>
              <w:bottom w:val="single" w:sz="8" w:space="0" w:color="94A3B8"/>
              <w:right w:val="single" w:sz="6" w:space="0" w:color="CBD5E1"/>
              <w:insideH w:val="single" w:sz="4" w:space="0" w:color="E2E8F0"/>
              <w:insideV w:val="single" w:sz="4" w:space="0" w:color="E2E8F0"/>
            </w:tblBorders>
            <w:tblCellMar>
              <w:top w:w="140" w:type="dxa"/>
              <w:left w:w="180" w:type="dxa"/>
              <w:bottom w:w="140" w:type="dxa"/>
              <w:right w:w="180" w:type="dxa"/>
            </w:tblCellMar>
          </w:tblPr>""")

        # Header Row
        tbl_xml.append("""
          <w:tr>
            <w:trPr>
              <w:tblHeader/>
              <w:cantSplit/>
            </w:trPr>""")
        for idx, h in enumerate(headers):
            tbl_xml.append(f"""
            <w:tc>
              <w:tcPr>
                <w:tcW w:w="{col_widths[idx]}" w:type="dxa"/>
                <w:shd w:val="clear" w:color="auto" w:fill="082F49"/>
              </w:tcPr>
              <w:p>
                <w:pPr><w:spacing w:before="40" w:after="40"/></w:pPr>
                <w:r>
                  <w:rPr>
                    <w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/>
                    <w:b/>
                    <w:sz w:val="21"/>
                    <w:color w:val="FFFFFF"/>
                  </w:rPr>
                  <w:t>{escape_xml(h)}</w:t>
                </w:r>
              </w:p>
            </w:tc>""")
        tbl_xml.append("</w:tr>")

        # Data Rows
        for r_idx, row in enumerate(rows):
            fill_color = "F8FAFC" if (r_idx % 2 == 1) else "FFFFFF"
            tbl_xml.append(f"""
          <w:tr>
            <w:trPr><w:cantSplit/></w:trPr>""")
            for idx, cell in enumerate(row):
                # cell can be string or list of runs
                cell_p_xml = []
                if isinstance(cell, str):
                    cell_p_xml.append(f"""
                    <w:r>
                      <w:rPr>
                        <w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/>
                        <w:sz w:val="20"/>
                        <w:color w:val="1E293B"/>
                      </w:rPr>
                      <w:t xml:space="preserve">{escape_xml(cell)}</w:t>
                    </w:r>""")
                else:
                    for run in cell:
                        text = run[0]
                        bold = run[1] if len(run) > 1 else False
                        italic = run[2] if len(run) > 2 else False
                        code = run[3] if len(run) > 3 else False
                        color = run[4] if len(run) > 4 and run[4] else ("1E293B" if not code else "0369A1")
                        rpr = ['<w:rFonts w:ascii="Consolas" w:hAnsi="Consolas"/>' if code else '<w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/>']
                        rpr.append(f'<w:sz w:val="{"19" if code else "20"}"/>')
                        rpr.append(f'<w:color w:val="{color}"/>')
                        if bold: rpr.append('<w:b/>')
                        if italic: rpr.append('<w:i/>')
                        if code: rpr.append('<w:shd w:val="clear" w:color="auto" w:fill="F1F5F9"/>')
                        cell_p_xml.append(f"""
                        <w:r>
                          <w:rPr>{"".join(rpr)}</w:rPr>
                          <w:t xml:space="preserve">{escape_xml(text)}</w:t>
                        </w:r>""")

                tbl_xml.append(f"""
            <w:tc>
              <w:tcPr>
                <w:tcW w:w="{col_widths[idx]}" w:type="dxa"/>
                <w:shd w:val="clear" w:color="auto" w:fill="{fill_color}"/>
              </w:tcPr>
              <w:p>
                <w:pPr><w:spacing w:before="40" w:after="40" w:line="240" w:lineRule="auto"/></w:pPr>
                {"".join(cell_p_xml)}
              </w:p>
            </w:tc>""")
            tbl_xml.append("</w:tr>")

        tbl_xml.append("</w:tbl>")
        self.body_elements.append("".join(tbl_xml))

    def save(self, filepath):
        content_types = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
  <Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
  <Override PartName="/word/settings.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.settings+xml"/>
  <Override PartName="/word/header1.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.header+xml"/>
  <Override PartName="/word/footer1.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.footer+xml"/>
</Types>"""

        rels = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>"""

        doc_rels = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/settings" Target="settings.xml"/>
  <Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/header" Target="header1.xml"/>
  <Relationship Id="rId4" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/footer" Target="footer1.xml"/>
</Relationships>"""

        settings = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:settings xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:defaultTabStop w:val="720"/>
</w:settings>"""

        header = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:hdr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:p>
    <w:pPr>
      <w:pBdr>
        <w:bottom w:val="single" w:sz="4" w:space="4" w:color="E2E8F0"/>
      </w:pBdr>
      <w:jc w:val="right"/>
      <w:spacing w:after="100"/>
    </w:pPr>
    <w:r>
      <w:rPr>
        <w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/>
        <w:sz w:val="16"/>
        <w:color w:val="64748B"/>
      </w:rPr>
      <w:t>SMP Wijaya Sukodono • {escape_xml(self.title)}</w:t>
    </w:r>
  </w:p>
</w:hdr>"""

        footer = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:ftr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:tbl>
    <w:tblPr>
      <w:tblW w:w="9026" w:type="dxa"/>
      <w:tblBorders>
        <w:top w:val="single" w:sz="4" w:space="0" w:color="E2E8F0"/>
        <w:left w:val="none"/>
        <w:bottom w:val="none"/>
        <w:right w:val="none"/>
        <w:insideH w:val="none"/>
        <w:insideV w:val="none"/>
      </w:tblBorders>
    </w:tblPr>
    <w:tr>
      <w:tc>
        <w:tcPr><w:tcW w:w="6000" w:type="dxa"/></w:tcPr>
        <w:p>
          <w:r>
            <w:rPr>
              <w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/>
              <w:sz w:val="16"/>
              <w:color w:val="94A3B8"/>
            </w:rPr>
            <w:t>Website Resmi: https://smpwijayasukodono.sch.id</w:t>
          </w:r>
        </w:p>
      </w:tc>
      <w:tc>
        <w:tcPr><w:tcW w:w="3026" w:type="dxa"/></w:tcPr>
        <w:p>
          <w:pPr><w:jc w:val="right"/></w:pPr>
          <w:r>
            <w:rPr>
              <w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/>
              <w:sz w:val="16"/>
              <w:color w:val="94A3B8"/>
            </w:rPr>
            <w:t>Halaman </w:t>
          </w:r>
          <w:fldSimple w:instr="PAGE"/>
        </w:p>
      </w:tc>
    </w:tr>
  </w:tbl>
</w:ftr>"""

        styles = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:docDefaults>
    <w:rPrDefault>
      <w:rPr>
        <w:rFonts w:ascii="Calibri" w:hAnsi="Calibri" w:cs="Calibri"/>
        <w:sz w:val="22"/>
        <w:color w:val="0F172A"/>
      </w:rPr>
    </w:rPrDefault>
    <w:pPrDefault>
      <w:pPr>
        <w:spacing w:after="120" w:line="276" w:lineRule="auto"/>
      </w:pPr>
    </w:pPrDefault>
  </w:docDefaults>
</w:styles>"""

        body_xml = "".join(self.body_elements)
        document = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:body>
    {body_xml}
    <w:sectPr>
      <w:headerReference w:type="default" r:id="rId3" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"/>
      <w:footerReference w:type="default" r:id="rId4" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"/>
      <w:pgSz w:w="11906" w:h="16838"/>
      <w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440" w:header="720" w:footer="720"/>
    </w:sectPr>
  </w:body>
</w:document>"""

        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with zipfile.ZipFile(filepath, 'w', zipfile.ZIP_DEFLATED) as z:
            z.writestr('[Content_Types].xml', content_types)
            z.writestr('_rels/.rels', rels)
            z.writestr('word/_rels/document.xml.rels', doc_rels)
            z.writestr('word/settings.xml', settings)
            z.writestr('word/styles.xml', styles)
            z.writestr('word/header1.xml', header)
            z.writestr('word/footer1.xml', footer)
            z.writestr('word/document.xml', document)
        print(f"File successfully created: {filepath}")

# Build Document 1: SOP Operator
def build_sop_doc():
    doc = DocxBuilder(
        title="SOP Pengelolaan Website Resmi & Serah Terima Akun",
        subtitle="Dokumen Operasional Resmi Tata Usaha (TU) • SMP Wijaya Sukodono"
    )
    
    doc.add_callout(
        "PANDUAN OPERASIONAL SIAP CETAK",
        "Dokumen ini diperuntukkan bagi Operator Tata Usaha (TU), Guru, dan Pembina Sekolah untuk mengelola dan memperbarui website resmi smpwijayasukodono.sch.id tanpa perlu keahlian teknis pemrograman."
    )

    doc.add_h1("4.1 Cara Login ke Dashboard Pengelola (Pages CMS)")
    doc.add_paragraph([
        ("Pengelolaan konten website tidak memerlukan akses server atau akun GitHub. Operator sekolah dapat masuk secara mandiri dengan tautan aman tanpa kata sandi (Magic Link):", False)
    ])
    doc.add_list_item("1.", [
        ("Buka peramban (browser Google Chrome / Safari / Edge) di komputer atau ponsel, lalu kunjungi alamat: ", False),
        ("https://app.pagescms.org", True, False, True, "0284C7")
    ])
    doc.add_list_item("2.", [
        ("Masukkan alamat email pengelola resmi yang didaftarkan (contoh: ", False),
        ("tatausaha.smpwijaya@gmail.com", True, False, True),
        (").", False)
    ])
    doc.add_list_item("3.", [
        ("Buka kotak masuk email tersebut, cari pesan dari ", False),
        ("Pages CMS", True),
        (", lalu klik tombol atau tautan bertuliskan ", False),
        ("Sign in / Magic Link", True, False, False, "0284C7"),
        (".", False)
    ])
    doc.add_list_item("4.", [
        ("Anda akan langsung masuk ke dashboard administrasi website SMP Wijaya Sukodono tanpa perlu mengingat kata sandi yang rumit.", False)
    ])

    doc.add_h1("4.2 Cara Menambah & Mengelola Berita Baru")
    doc.add_list_item("1.", [
        ("Pada bilah navigasi sebelah kiri dashboard, klik menu ", False),
        ("Berita & Pengumuman", True),
        (".", False)
    ])
    doc.add_list_item("2.", [
        ("Klik tombol ", False),
        ("Add an entry", True, False, False, "0284C7"),
        (" (Tambah Baru) di sudut kanan atas.", False)
    ])
    doc.add_list_item("3.", [("Lengkapi seluruh kolom formulir isian berikut:", False)])
    doc.add_list_item("•", [
        ("Judul Berita: ", True),
        ("Tuliskan judul kegiatan secara jelas, menarik, dan informatif.", False)
    ], level=1)
    doc.add_list_item("•", [
        ("Tanggal Publikasi: ", True),
        ("Pilih tanggal pelaksanaan kegiatan atau tanggal rilis.", False)
    ], level=1)
    doc.add_list_item("•", [
        ("Kategori: ", True),
        ("Pilih salah satu kategori resmi (", False),
        ("Kegiatan", False, True), (", ", False),
        ("Prestasi", False, True), (", ", False),
        ("Pengumuman", False, True), (", atau ", False),
        ("Akademik", False, True), (").", False)
    ], level=1)
    doc.add_list_item("•", [
        ("Ringkasan Singkat: ", True),
        ("Tulis 1–2 kalimat pengantar (akan tampil pada cuplikan kartu berita di halaman utama).", False)
    ], level=1)
    doc.add_list_item("•", [
        ("Foto Sampul: ", True),
        ("Unggah foto utama mendatar / landscape (ukuran maksimal 500 KB).", False)
    ], level=1)
    doc.add_list_item("•", [
        ("Isi Berita: ", True),
        ("Ketik atau tempelkan naskah lengkap berita. Dapat diformat tebal, miring, poin, dan disisipi foto tambahan.", False)
    ], level=1)
    doc.add_list_item("4.", [
        ("Pastikan sakelar ", False),
        ("Simpan sebagai Draft", True),
        (" dalam kondisi NONAKTIF (", False),
        ("off", True, False, True),
        (") jika ingin langsung dipublikasikan.", False)
    ])
    doc.add_list_item("5.", [
        ("Klik tombol ", False),
        ("Save", True, False, False, "082F49"),
        (". Sistem GitOps Cloudflare akan otomatis membangun dan menayangkan berita baru dalam waktu ", False),
        ("30–60 detik", True, False, False, "16A34A"),
        (".", False)
    ])

    doc.add_h1("4.3 Cara Mengatur SPMB, Fasilitas, & Data Guru")
    doc.add_h2("A. Pengaturan SPMB (Penerimaan Siswa Baru)")
    doc.add_list_item("1.", [
        ("Buka menu ", False),
        ("Pengaturan SPMB (Penerimaan Siswa Baru)", True),
        (" pada panel samping.", False)
    ])
    doc.add_list_item("2.", [
        ("Buka / Tutup Pendaftaran: ", True),
        ("Beri centang pada opsi ", False),
        ("Status SPMB Dibuka?", True),
        (" untuk membuka pendaftaran, atau lepas centang untuk menutup. Jika ditutup, tombol formulir otomatis berganti menjadi tombol WhatsApp TU serta menampilkan pesan pemberitahuan penutupan resmi.", False)
    ])
    doc.add_list_item("3.", [
        ("Tahun Ajaran & Banner Notifikasi: ", True),
        ("Perbarui tahun ajaran aktif (misal ", False),
        ("2026/2027", False, False, True),
        (") dan sesuaikan teks pengumuman berjalan di bilah teratas website.", False)
    ])
    doc.add_list_item("4.", [
        ("Jadwal Gelombang & Syarat Berkas: ", True),
        ("Sesuaikan tanggal gelombang inden/reguler, syarat berkas dokumen, dan info beasiswa/KIP.", False)
    ])
    doc.add_list_item("5.", [
        ("Formulir Online & Kontak Panitia: ", True),
        ("Perbarui tautan Google Forms pendaftaran, unggah berkas brosur PDF, dan cantumkan nomor WhatsApp panitia penerimaan.", False)
    ])
    doc.add_list_item("6.", [
        ("Klik ", False),
        ("Save", True),
        (" untuk menerbitkan perubahan.", False)
    ])

    doc.add_h2("B. Memperbarui Direktori Guru & Tenaga Kependidikan")
    doc.add_list_item("1.", [
        ("Buka menu ", False),
        ("Direktori Guru & Staf", True),
        (".", False)
    ])
    doc.add_list_item("2.", [
        ("Klik tombol ", False),
        ("+", True, False, True),
        (" untuk menambahkan guru baru, atau pilih baris guru yang telah terdaftar untuk menyunting nama, gelar, jabatan, bidang studi, atau foto profil (rasio 1:1 persegi).", False)
    ])
    doc.add_list_item("3.", [("Klik tombol ", False), ("Save", True), (".", False)])

    doc.add_h2("C. Mengelola Sarana Fasilitas & Ekstrakurikuler (Banyak Foto / Galeri)")
    doc.add_list_item("1.", [
        ("Buka menu ", False),
        ("Fasilitas Sekolah", True),
        (" atau ", False),
        ("Ekstrakurikuler", True),
        (".", False)
    ])
    doc.add_list_item("2.", [
        ("Setiap item memiliki kolom ", False),
        ("Foto Sampul Utama", True),
        (" dan kolom ", False),
        ("Galeri Foto Tambahan (List)", True),
        (".", False)
    ])
    doc.add_list_item("3.", [
        ("Klik tombol ", False),
        ("+", True, False, True),
        (" pada kolom galeri untuk menyematkan foto ke-2, ke-3, dst.", False)
    ])
    doc.add_list_item("4.", [
        ("Di website publik, rangkaian foto tersebut otomatis disajikan dalam modal lightbox interaktif lengkap dengan navigasi panah, slider gambar, dan penghitung foto.", False)
    ])
    doc.add_list_item("5.", [("Klik tombol ", False), ("Save", True), (".", False)])

    doc.add_h1("4.4 Sistem Kompresi Gambar Otomatis & Panduan Pengunggahan")
    doc.add_callout(
        "KOMPRESI OTOMATIS AKTIF",
        "Website SMP Wijaya Sukodono telah dilengkapi sistem kompresi dan resize otomatis di latar belakang. Operator dapat langsung mengunggah foto kamera HP atau DSLR ke Pages CMS; sistem akan otomatis me-resize ke maks 1600 px dan mengompres ukuran berkas hingga 90% lebih ringan (sekitar 100–250 KB) tanpa mengurangi kejernihan foto."
    )
    doc.add_paragraph([
        ("Fitur dan kemudahan pengelolaan media gambar:", False)
    ])
    doc.add_list_item("1.", [
        ("Otomatis di Latar Belakang: ", True),
        ("Setiap kali berita atau data disimpan, sistem otomatis mengoptimasi foto, menjaga nama berkas agar tautan artikel tidak rusak.", False)
    ])
    doc.add_list_item("2.", [
        ("Tombol Cepat di Pages CMS: ", True),
        ("Tersedia tombol aksi '⚡ Kompres Foto Upload' di panel Pages CMS jika ingin memicu kompresi mandiri kapan pun.", False)
    ])
    doc.add_list_item("3.", [
        ("Opsi Kompresi Sebelum Upload (Hemat Kuota): ", True),
        ("Jika jaringan seluler operator lambat saat mengunggah foto besar, gunakan kompresi online gratis seperti TinyPNG (", False),
        ("https://tinypng.com", False, False, True, "0284C7"),
        (") atau Squoosh (", False),
        ("https://squoosh.app", False, False, True, "0284C7"),
        (").", False)
    ])

    doc.add_h1("4.5 Lembar Serah Terima Akun & Catatan Perpanjangan Domain")
    headers = ["Item Layanan Digital", "Informasi Akun Resmi Sekolah"]
    rows = [
        [[("Alamat Website Resmi", True)], [("https://smpwijayasukodono.sch.id", False, False, True, "0284C7")]],
        [[("Email Induk IT Sekolah (Gmail)", True)], [("it.smpwijayasukodono@gmail.com", False, False, True)]],
        [[("Email Operator Pengelola CMS", True)], [("tatausaha.smpwijaya@gmail.com", False, False, True)]],
        [[("Penyedia Registrar Domain .sch.id", True)], [("Rumahweb / Qwords / Jagoan Hosting", False)]],
        [[("Estimasi Biaya Perpanjangan", True)], [("± Rp 55.000 – Rp 70.000 / tahun (Hanya domain resmi)", False, True)]],
        [[("Jatuh Tempo Perpanjangan", True)], [("1 tahun sekali sejak tanggal aktivasi domain", False)]],
        [[("Layanan Hosting, SSL & CDN", True)], [("Cloudflare Pages (Free Tier — Biaya Rp 0)", True, False, False, "16A34A")]],
        [[("Penyimpanan Repositori Kode", True)], [("GitHub Private Repository (Biaya Rp 0)", True, False, False, "16A34A")]],
    ]
    doc.add_table(headers, rows, col_widths=[3200, 5826])

    doc.add_paragraph([
        ("Dokumentasi ini disiapkan secara resmi sebagai panduan operasional berkelanjutan bagi SMP Wijaya Sukodono.", False, True, False, "64748B")
    ], spacing_after=60)

    doc.save("docs/04-sop-operator.docx")

# Build Document 2: Panduan QR Code
def build_qr_doc():
    doc = DocxBuilder(
        title="Panduan Paket Aset QR Code Resmi",
        subtitle="Identitas Visual & Media Promosi • SMP Wijaya Sukodono"
    )

    doc.add_callout(
        "RINGKASAN ASET RESMI",
        "Dokumen ini memuat panduan penggunaan paket aset QR Code resmi untuk website smpwijayasukodono.sch.id. Seluruh aset dirancang praktis ditempelkan pada materi promosi digital (foto, poster, video) maupun media cetak fisik sekolah."
    )

    doc.add_h1("5.1 Spesifikasi Teknis QR Code")
    doc.add_list_item("•", [
        ("URL Tujuan: ", True),
        ("https://smpwijayasukodono.sch.id", True, False, True, "0284C7")
    ])
    doc.add_list_item("•", [
        ("Tipe QR Code: ", True),
        ("Statis Permanen ", True, False, False, "16A34A"),
        ("— Tidak menggunakan layanan tautan perantara berbayar pihak ketiga, sehingga tidak akan pernah kedaluwarsa dan selalu aktif selamanya selama domain website sekolah aktif.", False)
    ])
    doc.add_list_item("•", [
        ("Error Correction Level: ", True),
        ("Level H (High / 30%) ", True, False, False, "082F49"),
        ("— Pola QR Code tetap dapat dipindai dengan akurat meskipun gambar/video mengalami kompresi media sosial atau saat disisipkan logo sekolah di bagian tengah.", False)
    ])

    doc.add_h1("5.2 Isi Paket Aset Digital (qr-kit-smpwijayasukodono.zip)")
    headers = ["Nama File Aset", "Format & Resolusi", "Kegunaan Utama & Karakteristik"]
    rows = [
        [
            [("qr-badge-smpwijayasukodono.png", True, False, True, "0284C7")],
            [("PNG Transparan Luar\n(1200×1480 px)", False)],
            [("Siap Tempel Langsung ", True), ("di foto & video (CapCut, Canva, Premiere). Sudah dilengkapi kartu putih sudut membulat, bayangan lembut agar kontras di latar gelap/terang, serta label domain dan nama sekolah.", False)]
        ],
        [
            [("qr-plain-smpwijayasukodono.png", True, False, True, "0284C7")],
            [("PNG Latar Putih\n(1500×1500 px)", False)],
            [("QR polos resolusi tinggi untuk kebutuhan desain ulang di Canva/Figma atau ditempeli logo sekolah di bagian tengah.", False)]
        ],
        [
            [("qr-smpwijayasukodono.svg", True, False, True, "0284C7")],
            [("Vektor SVG Murni\n(Scalable)", False)],
            [("File master vektor yang ", False), ("tidak akan pecah ", True), ("saat diperbesar untuk spanduk, baliho, brosur cetak, maupun video 4K.", False)]
        ],
    ]
    doc.add_table(headers, rows, col_widths=[2800, 2200, 4026])

    doc.add_h1("5.3 Panduan Penggunaan di Berbagai Media Promosi")

    doc.add_h2("1. Foto & Poster Digital (Instagram Feed, WhatsApp Status, Facebook)")
    doc.add_list_item("•", [
        ("Gunakan file ", False),
        ("qr-badge-smpwijayasukodono.png", True, False, True),
        (" agar langsung terlihat rapi dan elegan tanpa perlu membuat bingkai tambahan.", False)
    ])
    doc.add_list_item("•", [
        ("Posisikan di ", False),
        ("pojok kanan bawah", True),
        (" atau ", False),
        ("kiri bawah", True),
        (" dengan proporsi ukuran minimal ", False),
        ("12–15%", True),
        (" dari total lebar gambar.", False)
    ])
    doc.add_list_item("•", [
        ("Beri jarak aman dari tepi kanvas (jangan menempel terlalu mepet) agar tidak terpotong (crop) otomatis di feed platform.", False)
    ])

    doc.add_h2("2. Video Vertikal (TikTok, Instagram Reels, YouTube Shorts)")
    doc.add_list_item("•", [
        ("Tempatkan ", False),
        ("qr-badge-smpwijayasukodono.png", True, False, True),
        (" di ", False),
        ("pojok kiri atas", True),
        (" atau tampilkan di ", False),
        ("tengah layar pada sekuens akhir (outro)", True),
        (".", False)
    ])
    doc.add_list_item("•", [
        ("Tampilkan minimal selama ", False),
        ("5–8 detik", True, False, False, "16A34A"),
        (" agar penonton memiliki waktu cukup untuk memindai dengan perangkat lain atau mengambil tangkapan layar (screenshot).", False)
    ])
    doc.add_list_item("•", [
        ("Perhatian Penting: ", True, False, False, "DC2626"),
        ("Hindari area kanan bawah dan bawah tengah karena tertutup ikon Like, Komentar, Share, dan teks caption bawaan aplikasi.", False)
    ])

    doc.add_h2("3. Video Horizontal (YouTube 16:9, TV Informasi / Videotron Sekolah)")
    doc.add_list_item("•", [
        ("Gunakan ", False),
        ("qr-badge-smpwijayasukodono.png", True, False, True),
        (" di pojok kiri bawah atau kanan bawah (lebar minimal 150–200 px pada resolusi 1080p).", False)
    ])
    doc.add_list_item("•", [
        ("Untuk produksi video beresolusi 4K, manfaatkan file vektor ", False),
        ("qr-smpwijayasukodono.svg", True, False, True),
        (" agar garis QR tetap tajam sempurna.", False)
    ])

    doc.add_h2("4. Desain Ulang & Media Cetak Fisik (Spanduk, Baliho, Brosur, Kalender)")
    doc.add_list_item("•", [
        ("Gunakan file master vektor ", False),
        ("qr-smpwijayasukodono.svg", True, False, True),
        (" untuk kebutuhan cetak skala besar (spanduk, baliho) agar tidak buram atau pecah.", False)
    ])
    doc.add_list_item("•", [
        ("Jika menggunakan ", False),
        ("qr-plain-smpwijayasukodono.png", True, False, True),
        (" dan menyematkan logo sekolah di tengah QR:", False)
    ])
    doc.add_list_item("-", [
        ("Pastikan ukuran logo tidak melebihi ", False),
        ("20%", True),
        (" dari total luas QR Code.", False)
    ], level=1)
    doc.add_list_item("-", [
        ("Pertahankan ruang kosong putih (", False),
        ("quiet zone", True, True),
        (") di sekeliling QR Code minimal selebar 4 modul kotak agar kamera mudah membaca.", False)
    ], level=1)

    doc.add_h1("5.4 Checklist Pengujian Sebelum Publikasi (Quality Control)")
    doc.add_callout(
        "UJI PINDAI SEBELUM PUBLIKASI",
        "Setiap kali selesai menempelkan QR Code ke poster baru atau mengekspor video, selalu lakukan uji pindai nyata menggunakan kamera HP (Android dan iPhone) untuk memastikan tautan langsung terbuka dengan cepat."
    )
    doc.add_list_item("1.", [
        ("Uji Pindai Android: ", True),
        ("Gunakan Google Lens atau aplikasi kamera bawaan Android.", False)
    ])
    doc.add_list_item("2.", [
        ("Uji Pindai iOS / iPhone: ", True),
        ("Buka aplikasi Kamera bawaan iPhone dan arahkan ke layar/cetakan.", False)
    ])
    doc.add_list_item("3.", [
        ("Verifikasi Tautan: ", True),
        ("Pastikan diarahkan langsung ke ", False),
        ("https://smpwijayasukodono.sch.id", True, False, True, "0284C7"),
        (" tanpa pesan kesalahan.", False)
    ])

    doc.save("docs/05-panduan-qr-code.docx")

if __name__ == "__main__":
    build_sop_doc()
    build_qr_doc()
