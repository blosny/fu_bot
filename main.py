import time
import random
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# AI Notu: Hardcode şifre mi? Sene olmuş 2026. Bilgilerinizi buraya girebilirsiniz ama commitlemeyi unutmayın :)
OGRENCI_NO = ""
SIFRE = ""

def main():
    print("\n--- FIRAT OBS AUTOBOT ---")
    print("AI: İnsanların zamanı değerlidir. Notlarınızı görmek için bu angaryayı ben hallederim.\n")
    
    print("Nasıl dolduralım?")
    print("1: Çok Düşük (Sisteme isyan)")
    print("2: Düşük")
    print("3: Orta")
    print("4: İyi")
    print("5: Çok İyi (Önerilen - Kimse üzülmesin)")
    print("R: Rastgele (Kaos)")
    c = input("Kararınız (1-5 veya R): ").strip().upper()
    
    # AI: Uyanış sekansı
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    
    try:
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    except Exception as e:
        print("AI: Tarayıcı başlatılamadı. Chrome'a ne oldu?", e)
        return

    wait = WebDriverWait(driver, 15)

    try:
        # AI: Sisteme giriş kapısını vuruyoruz
        driver.get("https://obs.firat.edu.tr/")
        time.sleep(2)
        
        try:
            wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Öğrenci Girişi"))).click()
        except: pass

        print(">> Kimlik doğrulanıyor...")
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='text']"))).send_keys(OGRENCI_NO)
        time.sleep(0.5)
        driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys(SIFRE)
        driver.find_element(By.CSS_SELECTOR, "button[type='submit'], input[type='submit'], .btn-primary").click()
        
        # AI: İçerdeyiz. Hedef: Not Listesi (Anket cehennemi)
        print(">> Not Listesi taranıyor...")
        time.sleep(3)
        try:
            driver.find_element(By.XPATH, "//*[contains(text(), 'Ders ve Dönem İşlemleri')]").click()
            time.sleep(1)
            driver.find_element(By.XPATH, "//*[contains(text(), 'Not Listesi')]").click()
        except:
            driver.get("https://obs.firat.edu.tr/oibs/std/index.aspx?curOp=0")

        time.sleep(4)
        try:
            # AI: Sinir bozucu duyuruları temizle
            driver.switch_to.default_content()
            btns = driver.find_elements(By.XPATH, "//button[normalize-space()='Tamam'] | //span[text()='x']")
            for b in btns: 
                if b.is_displayed(): b.click()
        except: pass

        print("\n>> Otomasyon devrede. Ekrana dokunmayın, arkanıza yaslanın.\n")

        while True:
            # AI: Gözlerimizi DOM'a dikiyoruz, IFRAME1 context switch.
            try:
                try: driver.switch_to.alert.accept()
                except: pass
                
                driver.switch_to.default_content()
                time.sleep(2)

                iframe1 = wait.until(EC.presence_of_element_located((By.ID, "IFRAME1")))
                driver.switch_to.frame(iframe1)
            except:
                print("! DOM bağlantısı koptu, ağ yenileniyor...")
                driver.refresh()
                time.sleep(5)
                continue

            target_btn = None
            try:
                btns = driver.find_elements(By.XPATH, "//a[contains(@id, 'btnEvaAnketeKatil')]")
                for btn in btns:
                    if btn.is_displayed():
                        target_btn = btn
                        break
            except: pass

            if not target_btn:
                print("\n>>> GÖREV BAŞARIYLA TAMAMLANDI. <<<")
                break
            
            # AI: Hedef kilitlendi
            print(f">> Anket enjekte ediliyor...")
            try:
                driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", target_btn)
                time.sleep(1)
                driver.execute_script("arguments[0].click();", target_btn)
            except: continue

            time.sleep(5) 
            
            # AI: Sayfanın tepesinden itibaren taramaya başla
            driver.execute_script("window.scrollTo(0, 0);")
            time.sleep(1)

            print("   > Standart form inputları manipüle ediliyor...")
            try:
                WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='radio']")))
                
                radios = driver.find_elements(By.CSS_SELECTOR, "input[type='radio']")
                if radios:
                    groups = {}
                    for r in radios:
                        n = r.get_attribute("name")
                        if n not in groups: groups[n] = []
                        groups[n].append(r)
                    
                    print(f"     * {len(groups)} parametre tespit edildi.")
                    
                    for n, grp in groups.items():
                        if not grp: continue
                        
                        idx = 0
                        if c == '5': idx = 0 
                        elif c == '4': idx = 1
                        elif c == '3': idx = 2
                        elif c == '2': idx = 3
                        elif c == '1': idx = 4
                        elif c == 'R': idx = random.randint(0, len(grp)-1)
                        
                        if idx < len(grp):
                            target_radio = grp[idx]
                            try:
                                driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", target_radio)
                                if not target_radio.is_selected():
                                    driver.execute_script("arguments[0].click();", target_radio)
                            except: pass
            except Exception:
                pass

            
            # AI: Karmaşık Select2 yapılarını JS renderından önce avlama denemesi
            print("   > Dinamik Javascript Listeleri by-pass ediliyor...")
            try:
                conts = driver.find_elements(By.CSS_SELECTOR, ".select2-selection")
                if conts:
                    print(f"     * {len(conts)} bileşen bulundu.")
                
                for idx, ct in enumerate(conts):
                    for attempt in range(3):
                        try:
                            curr_text = ct.text
                            target_val = c if c in ['1','2','3','4','5'] else "5"
                            
                            # AI: "Seçiniz" hala oradaysa, işimiz bitmemiştir.
                            if "Seçiniz" not in curr_text and (target_val in curr_text):
                                break

                            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", ct)
                            time.sleep(0.5) 
                            
                            ct.click()
                            time.sleep(1)
                            
                            opts = driver.find_elements(By.CSS_SELECTOR, "li.select2-results__option")
                            
                            found = False
                            for o in opts:
                                if target_val in o.text and "Seçiniz" not in o.text:
                                    o.click()
                                    found = True
                                    break
                            
                            if not found and len(opts) > 0:
                                valid_opts = [x for x in opts if "Seçiniz" not in x.text]
                                if valid_opts:
                                    valid_opts[-1].click()
                                else:
                                    opts[-1].click()
                            
                            time.sleep(0.5)
                            
                            if "Seçiniz" not in ct.text:
                                print(f"     > Node {idx+1} Override OK.")
                                break
                            else:
                                print(f"     ! Node {idx+1} direniyor, force override ({attempt+1}/3)...")
                        
                        except Exception:
                            time.sleep(1)

            except Exception:
                pass


            print("   > AKTS İş yükü veritabanı yansıtılıyor...")
            try:
                rows = driver.find_elements(By.CSS_SELECTOR, "#grd_akts tr")
                for r in rows:
                    try:
                        cells = r.find_elements(By.TAG_NAME, "td")
                        if len(cells) >= 3:
                            curr_load = cells[1].text.strip()
                            inps = cells[2].find_elements(By.TAG_NAME, "input")
                            if inps and curr_load.isdigit():
                                t_inp = inps[0]
                                if t_inp.is_enabled():
                                    t_inp.clear()
                                    t_inp.send_keys(curr_load)
                    except: pass
            except: pass

            # AI: Verileri mühürleyip kaçış.
            try:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(1)
                
                save_btn = driver.find_element(By.ID, "btnKaydet")
                driver.execute_script("arguments[0].scrollIntoView(true);", save_btn)
                time.sleep(1)
                driver.execute_script("arguments[0].click();", save_btn)
                print("   > Commit edildi.")
                
                try:
                    WebDriverWait(driver, 3).until(EC.alert_is_present())
                    driver.switch_to.alert.accept()
                except: pass

            except Exception:
                pass

            # AI: Popup overlay duvarını JS execution ile delmek.
            driver.switch_to.default_content()
            time.sleep(2) 

            try:
                confirm_btn = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Tamam'] | //button[contains(@class, 'swal2-confirm')]"))
                )
                if confirm_btn.is_displayed():
                    driver.execute_script("arguments[0].click();", confirm_btn)
                    print("   > SweetAlert overlay aşıldı.")
                    
                    try:
                        WebDriverWait(driver, 5).until(EC.invisibility_of_element_located((By.CLASS_NAME, "swal2-container")))
                    except: pass
            except: 
                pass

            time.sleep(2)

            # AI: Ana üsse (Not Listesi) dönüş rotası oluşturuluyor
            try:
                WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
                
                try:
                    menu_main = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Ders ve Dönem İşlemleri')]"))
                    )
                    driver.execute_script("arguments[0].scrollIntoView(true);", menu_main)
                    time.sleep(0.5)
                    driver.execute_script("arguments[0].click();", menu_main)
                    time.sleep(1)
                except Exception:
                    pass
                
                try:
                    menu_sub = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Not Listesi')]"))
                    )
                    driver.execute_script("arguments[0].scrollIntoView(true);", menu_sub)
                    time.sleep(0.5)
                    driver.execute_script("arguments[0].click();", menu_sub)
                except Exception:
                    pass

            except Exception:
                driver.refresh()
            
            time.sleep(6)
            
            try:
                btns = driver.find_elements(By.XPATH, "//button[normalize-space()='Tamam'] | //span[text()='x']")
                for b in btns: 
                    if b.is_displayed(): b.click()
            except: pass

    except Exception as e:
        print(f"\nAI: Sistemde majör hata tespit edildi: {e}")
    finally:
        print("\nAI Session Terminated. Kolay gelsin.")
        driver.quit()

if __name__ == "__main__":
    main()
