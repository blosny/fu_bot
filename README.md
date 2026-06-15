# OBS Anket Botu

Fırat Üniversitesi Öğrenci Bilgi Sistemi (OBS) için otomatik anket doldurma botu.

## Kurulum ve Kullanım

### Windows İçin:
1. Terminali (Komut İstemi veya PowerShell) açın.
2. Gerekli kütüphaneleri yükleyin:
   ```bash
   pip install -r requirements.txt
   ```
   *(Hata alırsanız: `pip install selenium` ve `pip install webdriver-manager` yazın)*
3. `main.py` dosyasını bir metin editörüyle açıp `OGRENCI_NO` ve `SIFRE` kısımlarına kendi bilgilerinizi yazın.
4. Botu çalıştırın:
   ```bash
   python main.py
   ```

### macOS (Mac) İçin:
1. Terminal uygulamasını açın.
2. Mac'lerde genellikle `pip` yerine `pip3`, `python` yerine `python3` kullanılır. Kütüphaneleri yükleyin:
   ```bash
   pip3 install -r requirements.txt
   ```
   *(Hata alırsanız: `pip3 install selenium` ve `pip3 install webdriver-manager` yazın)*
   
   **Önemli Notlar:**
   * **Not 1:** Python sürümünüz eskiyse (Python 3.7 altı), lütfen python.org adresinden güncel Python sürümünü indirin.
   * **Not 2:** Mac'te "SSL: CERTIFICATE_VERIFY_FAILED" hatası alırsanız Uygulamalar (Applications) klasöründeki Python klasörüne gidip "Install Certificates.command" dosyasına çift tıklayın.
   
3. `main.py` dosyasını açıp `OGRENCI_NO` ve `SIFRE` kısımlarına kendi bilgilerinizi yazın.
4. Botu çalıştırın:
   ```bash
   python3 main.py
   ```

---
> **DİKKAT:** Kodları GitHub gibi yerlere yüklerken veya birisiyle paylaşırken kendi şifrenizi ve öğrenci numaranızı dosyadan silmeyi unutmayın!

## Lisans

Bu proje [MIT Lisansı](LICENSE) altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakabilirsiniz.
