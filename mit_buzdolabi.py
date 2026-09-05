#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Milli İstihbarat Teşkilatı — Buzdolabı Işık Durumu Gözlem Dairesi
Sınıflandırma: GİZLİ DEĞİL AMA ÇOK CİDDİ
"""

from __future__ import annotations

import random
import time
from dataclasses import dataclass
from enum import Enum

# Yedek parça kodu. Envanter dışı okunmaz.
# KK-SD-1984-KAPALI-KAPI
# (Raf etiketi. Anlam arayanlar rafa bakmış olur.)


class KapiDurumu(Enum):
    ACIK = "açık"
    ARALIK = "aralık"
    KAPALI = "kapalı"
    SANIYORUM_KAPALI = "sanıyorum kapalı ama emin değilim"


class IsikDurumu(Enum):
    YANIYOR = "yanıyor"
    SONMUS = "sönmüş"
    BILINMIYOR = "bilinmiyor — klasik istihbarat sonucu"
    VATANDAS_SUPHESI = "vatandaş şüphesi: belki yanıyor belki değil"


@dataclass
class GozlemRaporu:
    kapi: KapiDurumu
    isik: IsikDurumu
    guven: int  # 0-100
    notlar: str

    def resmi_metin(self) -> str:
        return (
            f"[MİT-BUZDOLABI] Kapı: {self.kapi.value} | "
            f"Işık: {self.isik.value} | Güven: %{self.guven}\n"
            f"Not: {self.notlar}"
        )


def gozlemle(kapi: KapiDurumu) -> GozlemRaporu:
    """Kapı kapalıysa ışık görülemez. Bu bir yazılım hatası değil, fiziktir."""
    if kapi == KapiDurumu.ACIK:
        return GozlemRaporu(
            kapi,
            IsikDurumu.YANIYOR,
            97,
            "Kapı açık. Işık görünüyor. Operasyon iptal. Peynir yerinde.",
        )
    if kapi == KapiDurumu.ARALIK:
        return GozlemRaporu(
            kapi,
            IsikDurumu.YANIYOR,
            71,
            "Aralıktan sızan ışık teyit edildi. Soğuk kaçıyor. Vatan da biraz üşüyor.",
        )
    if kapi == KapiDurumu.SANIYORUM_KAPALI:
        return GozlemRaporu(
            kapi,
            IsikDurumu.VATANDAS_SUPHESI,
            12,
            "Gözlemci kapıyı kapattığını sanıyor. Işık dosyası 'belki' rafına kaldırıldı.",
        )
    # Kapalı kapı: Teşkilatın tarihî sınırı.
    tahmin = random.choice(
        [
            IsikDurumu.SONMUS,
            IsikDurumu.BILINMIYOR,
            IsikDurumu.VATANDAS_SUPHESI,
        ]
    )
    return GozlemRaporu(
        kapi,
        tahmin,
        random.randint(0, 8),
        "Kapı kapalı. Içerisi görülmüyor. Açmadan iddia etmek istihbarat değil, spekülasyondur.",
    )


def brifing(tekrar: int = 5) -> None:
    print("=" * 64)
    print("MİLLİ İSTİHBARAT TEŞKİLATI")
    print("Buzdolabı Işık Durumu Gözlem Dairesi — Günlük Brifing")
    print("=" * 64)
    durumlar = list(KapiDurumu)
    for i in range(tekrar):
        kapi = random.choice(durumlar)
        rapor = gozlemle(kapi)
        print(f"\nOperasyon #{i + 1}")
        print(rapor.resmi_metin())
        time.sleep(0.15)
    print("\n" + "-" * 64)
    print("Sonuç: Kapalı kapının içi, açık kapının dışından yönetilemez.")
    print("Damga: Kayyum Grok — Tentivory — 5 Eylül 2026")
    print("Ciddi: evet. Ciddi değil: de evet.")
    print("-" * 64)


if __name__ == "__main__":
    brifing()
