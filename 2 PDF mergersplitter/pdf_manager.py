import PyPDF2

def merge_pdfs(pdf_list, output_path):
    pdf_merger = PyPDF2.PdfMerger()
    for pdf in pdf_list:
        try:
            pdf_merger.append(pdf)
        except FileNotFoundError:
            print(f"Dosya bulunamadı: {pdf}")
        except Exception as e:
            print(f"Hata oluştu {pdf} için: {e}")
    pdf_merger.write(output_path)
    pdf_merger.close()
    print(f"PDF dosyaları başarıyla birleştirildi ve {output_path} olarak kaydedildi.")

def split_pdf(pdf_path, output_folder):
    try:
        pdf_reader = PyPDF2.PdfReader(pdf_path)
        for page_num in range(len(pdf_reader.pages)):
            pdf_writer = PyPDF2.PdfWriter()
            pdf_writer.add_page(pdf_reader.pages[page_num])
            output_path = f"{output_folder}/page_{page_num + 1}.pdf"
            with open(output_path, 'wb') as output_pdf:
                pdf_writer.write(output_pdf)
            print(f"Sayfa {page_num + 1} kaydedildi: {output_path}")
    except FileNotFoundError:
        print(f"Dosya bulunamadı: {pdf_path}")
    except Exception as e:
        print(f"Hata oluştu: {e}")

def main():
    print("📄 PDF Birleştirici / Bölücü")
    choice = input("1 - PDF birleştir\n2 - PDF böl\nSeçiminiz: ")
    
    if choice == '1':
        files = input("Birleştirilecek PDF dosyalarının yollarını virgülle ayırarak girin: ").split(',')
        output = input("Oluşacak dosya adı (örn: merged.pdf): ")
        merge_pdfs([f.strip() for f in files], output)
    elif choice == '2':
        pdf_path = input("Bölünecek PDF dosyasının yolunu girin: ")
        output_folder = input("Sayfaların kaydedileceği klasör yolunu girin: ")
        split_pdf(pdf_path.strip(), output_folder.strip())
    else:
        print("Geçersiz seçim.")

if __name__ == "__main__":
    main()
