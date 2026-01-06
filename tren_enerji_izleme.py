import tkinter as tk
from tkinter import ttk
import random
import time
import math
from collections import deque
from datetime import datetime

class TrenParcasi:
    def __init__(self, isim, min_enerji, max_enerji, birim="kW"):
        self.isim = isim
        self.min_enerji = min_enerji
        self.max_enerji = max_enerji
        self.birim = birim
        self.guncel_enerji = random.uniform(self.min_enerji, self.max_enerji)
        self.display_enerji = self.guncel_enerji
        self.toplam_tuketim = 0
        self.history = deque(maxlen=100)
        self.phase = random.random() * 2 * math.pi
        self.trend_direction = random.choice([-1, 1])
        self.time_offset = random.random() * 10
    
    def sentetik_veri_uret(self):
        t = time.time() + self.time_offset
        
        center = (self.min_enerji + self.max_enerji) / 2
        drift = (center - self.guncel_enerji) * 0.02
        
        sinus = math.sin(t * 0.5 + self.phase) * 0.15 * (self.max_enerji - self.min_enerji)
        noise = random.uniform(-0.1, 0.1) * (self.max_enerji - self.min_enerji)
        
        yeni = self.guncel_enerji + drift + sinus + noise
        self.guncel_enerji = max(self.min_enerji * 0.5, min(self.max_enerji * 1.2, yeni))
        
        self.toplam_tuketim += self.guncel_enerji * 0.0001667
        self.history.append(self.guncel_enerji)
        
        return self.guncel_enerji

class EnerjiIzlemePaneli:
    def __init__(self, root):
        self.root = root
        self.root.title("Elektrikli Tren Enerji İzleme Sistemi")
        self.root.geometry("1400x900")
        self.root.configure(bg="#0a0e27")
        
        self.parcalar = [
            TrenParcasi("Traksiyon Motoru 1", 150, 350),
            TrenParcasi("Traksiyon Motoru 2", 150, 350),
            TrenParcasi("Traksiyon Motoru 3", 150, 350),
            TrenParcasi("Traksiyon Motoru 4", 150, 350),
            TrenParcasi("HVAC Sistemi", 30, 80),
            TrenParcasi("Aydınlatma", 10, 25),
            TrenParcasi("Kapı Mekanizmaları", 5, 20),
            TrenParcasi("Kontrol Sistemleri", 8, 15),
            TrenParcasi("Yardımcı Güç Ünitesi", 20, 50),
            TrenParcasi("Fren Sistemi", 10, 40),
            TrenParcasi("İletişim Sistemleri", 3, 8),
            TrenParcasi("Batarya Şarj", 0, 100)
        ]
        
        self.calisiyor = True
        self.ui_olustur()
        self.animasyon_baslat()
    
    def ui_olustur(self):
        # Üst başlık bölümü
        baslik_frame = tk.Frame(self.root, bg="#1a1f3a", height=100)
        baslik_frame.pack(fill=tk.X, padx=0, pady=0)
        baslik_frame.pack_propagate(False)
        
        # Sol taraf - Logo ve başlık
        sol_frame = tk.Frame(baslik_frame, bg="#1a1f3a")
        sol_frame.pack(side=tk.LEFT, padx=30, pady=10, fill=tk.BOTH, expand=True)
        
        logo_label = tk.Label(
            sol_frame,
            text="⚡",
            font=("Arial", 48),
            bg="#1a1f3a",
            fg="#00d9ff"
        )
        logo_label.pack(side=tk.LEFT, padx=(0, 15))
        
        baslik_text_frame = tk.Frame(sol_frame, bg="#1a1f3a")
        baslik_text_frame.pack(side=tk.LEFT, fill=tk.Y)
        
        baslik = tk.Label(
            baslik_text_frame,
            text="ELEKTRİKLİ TREN",
            font=("Arial", 24, "bold"),
            bg="#1a1f3a",
            fg="#ffffff",
            anchor="w"
        )
        baslik.pack(anchor="w")
        
        alt_baslik = tk.Label(
            baslik_text_frame,
            text="Gerçek Zamanlı Enerji İzleme Sistemi",
            font=("Arial", 12),
            bg="#1a1f3a",
            fg="#7c8db5",
            anchor="w"
        )
        alt_baslik.pack(anchor="w")
        
        # Sağ taraf - Saat ve tarih
        sag_frame = tk.Frame(baslik_frame, bg="#1a1f3a")
        sag_frame.pack(side=tk.RIGHT, padx=30, pady=10)
        
        self.saat_label = tk.Label(
            sag_frame,
            text="00:00:00",
            font=("Arial", 32, "bold"),
            bg="#1a1f3a",
            fg="#00d9ff"
        )
        self.saat_label.pack()
        
        self.tarih_label = tk.Label(
            sag_frame,
            text="",
            font=("Arial", 11),
            bg="#1a1f3a",
            fg="#7c8db5"
        )
        self.tarih_label.pack()
        
        # Durum göstergesi
        durum_frame = tk.Frame(sag_frame, bg="#1a1f3a")
        durum_frame.pack(pady=(5, 0))
        
        self.durum_indicator = tk.Canvas(durum_frame, width=12, height=12, bg="#1a1f3a", highlightthickness=0)
        self.durum_indicator.pack(side=tk.LEFT, padx=(0, 5))
        self.durum_indicator.create_oval(2, 2, 10, 10, fill="#00ff88", outline="")
        
        durum_text = tk.Label(
            durum_frame,
            text="SİSTEM AKTİF",
            font=("Arial", 9, "bold"),
            bg="#1a1f3a",
            fg="#00ff88"
        )
        durum_text.pack(side=tk.LEFT)
        
        # Özet bilgi paneli
        ozet_frame = tk.Frame(self.root, bg="#0a0e27", height=100)
        ozet_frame.pack(fill=tk.X, padx=20, pady=(10, 5))
        ozet_frame.pack_propagate(False)
        
        # Toplam güç kartı
        self.guc_karti = self.info_karti_olustur(ozet_frame, "TOPLAM GÜÇ", "0.0 kW", "#00d9ff", 0)
        # Toplam tüketim kartı
        self.tuketim_karti = self.info_karti_olustur(ozet_frame, "TOPLAM TÜKETİM", "0.0 kWh", "#ff6b9d", 1)
        # Ortalama verimlilik
        self.verimlilik_karti = self.info_karti_olustur(ozet_frame, "ORTALAMA VERİMLİLİK", "0%", "#ffd93d", 2)
        
        # Scrollable ana panel
        container = tk.Frame(self.root, bg="#0a0e27")
        container.pack(fill=tk.BOTH, expand=True, padx=20, pady=(5, 20))
        
        self.canvas = tk.Canvas(container, bg="#0a0e27", highlightthickness=0)
        scrollbar = ttk.Scrollbar(container, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg="#0a0e27")
        
        self.canvas_window = self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=scrollbar.set)
        
        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Canvas genişlik değiştiğinde içeriği yeniden boyutlandır
        def on_canvas_configure(event):
            canvas_width = event.width
            self.canvas.itemconfig(self.canvas_window, width=canvas_width)
        
        self.canvas.bind("<Configure>", on_canvas_configure)
        
        # Scrollable frame değiştiğinde scroll bölgesini güncelle
        def on_frame_configure(event):
            self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        
        self.scrollable_frame.bind("<Configure>", on_frame_configure)
        
        # Mouse wheel scroll - tüm widgetlara bind et
        def bind_mousewheel(widget):
            widget.bind("<MouseWheel>", self._on_mousewheel)
            widget.bind("<Button-4>", self._on_mousewheel)
            widget.bind("<Button-5>", self._on_mousewheel)
            for child in widget.winfo_children():
                bind_mousewheel(child)
        
        bind_mousewheel(self.root)
        
        # Grid için sütun yapılandırması
        self.scrollable_frame.grid_columnconfigure(0, weight=1)
        self.scrollable_frame.grid_columnconfigure(1, weight=1)
        self.scrollable_frame.grid_columnconfigure(2, weight=1)
        
        # Her parça için widget oluştur
        self.parca_widgets = {}
        for i, parca in enumerate(self.parcalar):
            frame = self.parca_widget_olustur(self.scrollable_frame, parca, i)
            self.parca_widgets[parca.isim] = frame
    
    def info_karti_olustur(self, parent, baslik, deger, renk, konum):
        kart = tk.Frame(parent, bg="#141b2d", relief=tk.FLAT, bd=0)
        kart.grid(row=0, column=konum, padx=10, pady=10, sticky="nsew")
        parent.grid_columnconfigure(konum, weight=1)
        
        # İç padding
        ic = tk.Frame(kart, bg="#141b2d")
        ic.pack(padx=20, pady=15, fill=tk.BOTH, expand=True)
        
        baslik_label = tk.Label(
            ic,
            text=baslik,
            font=("Arial", 10, "bold"),
            bg="#141b2d",
            fg="#7c8db5"
        )
        baslik_label.pack(anchor="w")
        
        deger_label = tk.Label(
            ic,
            text=deger,
            font=("Arial", 28, "bold"),
            bg="#141b2d",
            fg=renk
        )
        deger_label.pack(anchor="w", pady=(5, 0))
        
        kart.deger_label = deger_label
        return kart
    
    def parca_widget_olustur(self, parent, parca, index):
        # Modern kart tasarımı
        frame = tk.Frame(parent, bg="#141b2d", relief=tk.FLAT, bd=0)
        row = index // 3
        col = index % 3
        frame.grid(row=row, column=col, padx=8, pady=8, sticky="nsew")
        
        # İç padding
        inner = tk.Frame(frame, bg="#141b2d")
        inner.pack(padx=18, pady=18, fill=tk.BOTH, expand=True)
        
        # Üst kısım: İsim ve durum
        ust_frame = tk.Frame(inner, bg="#141b2d")
        ust_frame.pack(fill=tk.X, pady=(0, 12))
        
        isim_label = tk.Label(
            ust_frame,
            text=parca.isim,
            font=("Arial", 12, "bold"),
            bg="#141b2d",
            fg="#ffffff",
            anchor="w"
        )
        isim_label.pack(side=tk.LEFT)
        
        # Durum göstergesi
        durum_canvas = tk.Canvas(ust_frame, width=8, height=8, bg="#141b2d", highlightthickness=0)
        durum_canvas.pack(side=tk.RIGHT)
        durum_canvas.create_oval(1, 1, 7, 7, fill="#00ff88", outline="")
        
        # Enerji değeri (büyük)
        enerji_label = tk.Label(
            inner,
            text="0.0 kW",
            font=("Arial", 24, "bold"),
            bg="#141b2d",
            fg="#00d9ff"
        )
        enerji_label.pack(anchor="w", pady=(0, 8))
        
        # Progress bar container
        progress_container = tk.Frame(inner, bg="#1a2332", height=8)
        progress_container.pack(fill=tk.X, pady=(0, 8))
        progress_container.pack_propagate(False)
        
        progress_bar = tk.Canvas(progress_container, bg="#1a2332", highlightthickness=0, height=8)
        progress_bar.pack(fill=tk.BOTH, expand=True)
        
        # Bilgi satırı
        info_frame = tk.Frame(inner, bg="#141b2d")
        info_frame.pack(fill=tk.X, pady=(0, 10))
        
        yuzde_label = tk.Label(
            info_frame,
            text="0%",
            font=("Arial", 10, "bold"),
            bg="#141b2d",
            fg="#7c8db5"
        )
        yuzde_label.pack(side=tk.LEFT)
        
        toplam_label = tk.Label(
            info_frame,
            text="0.0 kWh",
            font=("Arial", 10),
            bg="#141b2d",
            fg="#7c8db5"
        )
        toplam_label.pack(side=tk.RIGHT)
        
        # Sparkline grafik
        spark = tk.Canvas(inner, width=320, height=60, bg="#0a0e27", highlightthickness=0)
        spark.pack(fill=tk.X)
        
        # Widget referansları
        frame.enerji_label = enerji_label
        frame.progress_bar = progress_bar
        frame.yuzde_label = yuzde_label
        frame.toplam_label = toplam_label
        frame.spark = spark
        frame.durum_canvas = durum_canvas
        
        return frame
    
    def renk_hesapla(self, deger, min_val, max_val):
        oran = (deger - min_val) / (max_val - min_val) if max_val > min_val else 0
        
        if oran < 0.4:
            return "#00ff88"
        elif oran < 0.7:
            return "#ffd93d"
        else:
            return "#ff6b9d"
    
    def draw_sparkline(self, canvas, data, min_val, max_val, color):
        if len(data) < 2:
            return
        
        w = canvas.winfo_width() or 320
        h = canvas.winfo_height() or 60
        
        # Sadece değişiklik varsa çiz
        current_data = getattr(canvas, '_last_data', None)
        if current_data == list(data)[-10:]:  # Son 10 değer aynıysa çizme
            return
        
        canvas._last_data = list(data)[-10:]
        canvas.delete("all")
        
        pts = list(data)
        min_v = min(min_val, min(pts))
        max_v = max(max_val, max(pts))
        span = max_v - min_v if max_v > min_v else 1
        
        n = len(pts)
        step = w / (n - 1) if n > 1 else w
        
        # Gradient fill altı
        for i in range(len(pts) - 1):
            x1 = i * step
            x2 = (i + 1) * step
            y1 = h - ((pts[i] - min_v) / span) * (h - 10)
            y2 = h - ((pts[i + 1] - min_v) / span) * (h - 10)
            
            # Alt taraf fill
            canvas.create_polygon(
                x1, h, x1, y1, x2, y2, x2, h,
                fill=color, stipple="gray50", outline=""
            )
        
        # Çizgi
        coords = []
        for i, v in enumerate(pts):
            x = i * step
            y = h - ((v - min_v) / span) * (h - 10)
            coords.extend([x, y])
        
        if len(coords) >= 4:
            canvas.create_line(coords, fill=color, width=2, smooth=True)
            
            # Son nokta vurgusu
            canvas.create_oval(
                coords[-2] - 3, coords[-1] - 3,
                coords[-2] + 3, coords[-1] + 3,
                fill=color, outline="#ffffff", width=1
            )
    
    def draw_progress(self, canvas, percentage, color):
        # Sadece değişiklik varsa çiz
        last_state = getattr(canvas, '_last_progress', None)
        current_state = (percentage, color)
        if last_state == current_state:
            return
        
        canvas._last_progress = current_state
        canvas.delete("all")
        
        w = canvas.winfo_width() or 320
        h = 8
        
        # Arka plan
        canvas.create_rectangle(0, 0, w, h, fill="#1a2332", outline="")
        
        # İlerleme
        progress_w = (w * percentage) / 100
        if progress_w > 0:
            canvas.create_rectangle(0, 0, progress_w, h, fill=color, outline="")
    
    def veri_guncelle(self):
        if not self.calisiyor:
            return
        
        try:
            toplam_guc = 0
            toplam_tuketim = 0
            toplam_yuzde = 0
            
            for parca in self.parcalar:
                enerji = parca.sentetik_veri_uret()
                
                # Yumuşatma
                prev_display = parca.display_enerji
                smoothed = prev_display + (enerji - prev_display) * 0.3
                parca.display_enerji = smoothed
                
                toplam_guc += smoothed
                toplam_tuketim += parca.toplam_tuketim
                
                # UI güncelle
                widget = self.parca_widgets[parca.isim]
                renk = self.renk_hesapla(smoothed, parca.min_enerji, parca.max_enerji)
                yuzde = (smoothed / parca.max_enerji) * 100 if parca.max_enerji > 0 else 0
                toplam_yuzde += yuzde
                
                widget.enerji_label.config(text=f"{smoothed:.1f} {parca.birim}", fg=renk)
                widget.yuzde_label.config(text=f"{yuzde:.0f}%")
                widget.toplam_label.config(text=f"{parca.toplam_tuketim:.2f} kWh")
                
                self.draw_progress(widget.progress_bar, yuzde, renk)
                self.draw_sparkline(widget.spark, parca.history, parca.min_enerji, parca.max_enerji, renk)
            
            # Özet kartlarını güncelle
            self.guc_karti.deger_label.config(text=f"{toplam_guc:.1f} kW")
            self.tuketim_karti.deger_label.config(text=f"{toplam_tuketim:.2f} kWh")
            ortalama_verimlilik = (toplam_yuzde / len(self.parcalar)) if len(self.parcalar) > 0 else 0
            self.verimlilik_karti.deger_label.config(text=f"{ortalama_verimlilik:.0f}%")
            
        except Exception as e:
            print(f"Hata: {e}")
        
        # Tekrar çağır
        if self.calisiyor:
            self.root.after(50, self.veri_guncelle)
    
    def saat_guncelle(self):
        if not self.calisiyor:
            return
        
        try:
            simdi = datetime.now()
            self.saat_label.config(text=simdi.strftime("%H:%M:%S"))
            
            # Türkçe ay isimleri
            aylar = ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran",
                     "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"]
            gunler = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]
            
            tarih_str = f"{simdi.day} {aylar[simdi.month-1]} {simdi.year}, {gunler[simdi.weekday()]}"
            self.tarih_label.config(text=tarih_str)
            
            # Durum göstergesini animasyon yap
            renk = "#00ff88" if int(simdi.timestamp()) % 2 == 0 else "#00dd77"
            self.durum_indicator.delete("all")
            self.durum_indicator.create_oval(2, 2, 10, 10, fill=renk, outline="")
            
        except Exception as e:
            print(f"Saat hatası: {e}")
        
        # Tekrar çağır
        if self.calisiyor:
            self.root.after(1000, self.saat_guncelle)
    
    def animasyon_baslat(self):
        self.veri_guncelle()
        self.saat_guncelle()
    
    def _on_mousewheel(self, event):
        # Windows ve MacOS için mouse wheel scroll
        if event.num == 5 or event.delta < 0:
            # Aşağı scroll
            self.canvas.yview_scroll(1, "units")
        elif event.num == 4 or event.delta > 0:
            # Yukarı scroll
            self.canvas.yview_scroll(-1, "units")
        return "break"

def main():
    root = tk.Tk()
    
    style = ttk.Style()
    style.theme_use('clam')
    
    app = EnerjiIzlemePaneli(root)
    
    # Pencere kapatma işleyicisi
    def kapat():
        app.calisiyor = False
        root.after(100, lambda: root.destroy())
    
    root.protocol("WM_DELETE_WINDOW", kapat)
    
    # Ana döngü
    root.mainloop()

if __name__ == "__main__":
    main()