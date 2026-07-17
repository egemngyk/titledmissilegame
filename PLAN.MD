# PLAN

## Proje Hakkında

Bu proje, **Ursina Engine** kullanılarak geliştirilecek çok platformlu (öncelikli hedef PC) bir 3D oyundur.

İlk hedef Windows, Linux ve macOS üzerinde çalışan sağlam bir sürüm geliştirmektir. Oyun tamamlandıktan sonra performans optimizasyonları yapılacak ve ardından Android'e taşınması için gerekli çalışmalar gerçekleştirilecektir. Mobil kontroller ve dokunmatik arayüz, Android sürümü başarılı şekilde çalıştırıldıktan sonra geliştirilecektir.

Proje boyunca temiz kod, modüler mimari ve uzun vadede büyüyebilecek bir yapı hedeflenmektedir.

---

# Proje Yapısı

```text
titledmissilegame/
├── .venv/
├── pyproject.toml
├── uv.lock
├── .gitignore
├── README.md
│
├── assets/                 # Tüm görsel/ses dosyaları
│   ├── models/
│   ├── textures/
│   ├── sounds/
│   ├── music/
│   ├── fonts/
│   └── shaders/
│
├── saves/                  # Kayıt dosyaları
│
├── configs/                # Ayarlar
│   ├── game.json
│   ├── graphics.json
│   └── controls.json
│
├── src/
│   ├── main.py             # Sadece oyunu başlatır
│   │
│   ├── core/               # Motor benzeri sistemler
│   │   ├── game.py
│   │   ├── input_manager.py
│   │   ├── scene_manager.py
│   │   ├── audio_manager.py
│   │   ├── save_manager.py
│   │   └── settings.py
│   │
│   ├── entities/           # Oyundaki nesneler
│   │   ├── player.py
│   │   ├── enemy.py
│   │   ├── npc.py
│   │   ├── item.py
│   │   └── projectile.py
│   │
│   ├── world/              # Dünya sistemi
│   │   ├── terrain.py
│   │   ├── chunk.py
│   │   ├── biome.py
│   │   └── world_generator.py
│   │
│   ├── systems/            # Oyun mekanikleri
│   │   ├── combat.py
│   │   ├── inventory.py
│   │   ├── crafting.py
│   │   ├── health.py
│   │   ├── quest.py
│   │   └── day_night.py
│   │
│   ├── ui/                 # Arayüz
│   │   ├── hud.py
│   │   ├── inventory_ui.py
│   │   ├── pause_menu.py
│   │   ├── settings_menu.py
│   │   └── mobile_controls.py
│   │
│   └── utils/              # Yardımcı fonksiyonlar
│       ├── math_utils.py
│       ├── file_utils.py
│       ├── debug.py
│       └── constants.py
│
└── tests/
```

---

# Yol Haritası

## Yapılacaklar

- [x] Temel yapıyı oluştur
- [x] Boş bir arazi oluştur
- [X] Füze elemanını oluştur
- [ ] Füze elemanını kontrol edilebilir yap
- [ ] Füze elemanını uçabilir yap
- [ ] Yer çekimi ve diğer fizik unsurlarını ekle

---

## Notlar

- Öncelik masaüstü sürümüdür.
- Performans optimizasyonu oyun tamamlandıktan sonra yapılacaktır.
- Android desteği ayrı bir geliştirme aşaması olacaktır.
- Kod mümkün olduğunca modüler tutulacaktır.