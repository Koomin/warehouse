import decimal

from django.db import models

from warehouse_app.utils.utils import OptimaConnection
from warehouse_app.products.models import Product
from warehouse_app.stores.models import Store
from warehouse_app.warehouse.models import WarehouseModel


class DocumentType(WarehouseModel):
    optima_id = models.PositiveIntegerField()
    optima_class = models.PositiveIntegerField()
    short_name = models.CharField(max_length=50, null=True, blank=True)
    name = models.CharField(max_length=255, null=False, blank=False)
    numbering = models.CharField(max_length=255, null=False, blank=False)
    type_id = models.PositiveIntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.short_name


class Document(WarehouseModel):
    optima_id = models.PositiveIntegerField(null=True, blank=True)
    document_type = models.ForeignKey(DocumentType, on_delete=models.CASCADE, null=False, blank=False)
    optima_full_number = models.CharField(max_length=255, null=True, blank=True)
    value_net = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=False, default=0.00)
    value_vat = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=False, default=0.00)
    value_gross = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=False, default=0.00)
    source_store = models.ForeignKey(Store, on_delete=models.CASCADE, null=False, blank=False,
                                     related_name='document_source')
    destination_store = models.ForeignKey(Store, on_delete=models.CASCADE, null=True, blank=True,
                                          related_name='document_destination')
    exported = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def save_to_optima(self):
        for idx, document_item in enumerate(self.document_items.all()):
            connection = OptimaConnection()
            connection.cursor.execute(f'INSERT INTO CDN.TraElem (TrE_TrNId, TrE_Lp, TrE_LpPow, TrE_TyPDokumentu,'
                                      ' TrE_Aktywny, TrE_RabatPromocyjny, TrE_RabatKorekta, TrE_PodmiotTyp, TrE_PodID,'
                                      'TrE_TwrId, TrE_MagId, TrE_TwrNazwa, TrE_TwrKod, TrE_TwrSWW, TrE_TwrTyp, TrE_Stawka, '
                                      'TrE_Flaga, TrE_Zrodlowa, TrE_TwCNumer, TrE_TypNB, TrE_Cena0, TrE_Rabat, TrE_CenaW,'
                                      'TrE_Waluta, TrE_Kaucja, TrE_WyborDostaw, TrE_KursNumer, TrE_KursL, Tre_KursM, '
                                      'TrE_CenaT, TrE_Ilosc, TrE_IloscKW, TrE_Jm, TrE_JmZ, TrE_JmCalkowite, '
                                      'TrE_JMPrzelicznikL, TrE_JMPRzelicznikM, TrE_IloscJM, TrE_IloscJMKW,'
                                      ' TrE_WartoscNetto, TrE_WartoscBrutto, TrE_WartoscZakupu, TrE_KosztUslugi,'
                                      'TrE_KosztKGO, Tre_AkcyzaJMPomPrzelicznikL, Tre_AkcyzaJMPomPrzelicznikM, '
                                      'TrE_AkcyzaOpal, TrE_AkcyzaStawka, Tre_OdwrotneObciazenie, TrE_WartoscZakupuWylicz, '
                                      'TrE_Cena0WD, TrE_CenaWWD, TrE_WartoscNettoWal, TrE_WartoscBruttoWal, TrE_Prog,'
                                      'TrE_UpustTyp, TrE_Upust, TrE_UpustKnt, TrE_UpustKntTyp, TrE_IFA24Mag, TrE_IFA24,'
                                      'TrE_ZTwID, TrE_ZestawWiazanie, TrE_ZTwGlowny, TrE_ZTwIlosc, TrE_DoZwrotu, TrE_UslugaZlozonaId, '
                                      'TrE_UslugaZlozona, TrE_PATrEId, TrE_KWRoznicaKursowa, Tre_CenaZCzteremaMiejscami, '
                                      'TrE_FakZalKwotaMax, Tre_UstawAtrSQL, Tre_UstawAtrSQLDokTyp, TrE_SplitPay, TrE_KV7ID,'
                                      ' TrE_CzySaCechyWymagane, TrE_OplataCukrowaPrzelicznikML, TrE_OplataCukrowaOdCukrowStala,'
                                      'TrE_OplataCukrowaOdCukrowZmienna, TrE_OplataCukrowaOdKofeinyTaurynyStala,'
                                      'TrE_OplataCukrowaOdCukrowZawartoscGram, TrE_OplataCukrowaOdCukrowZawartoscSokow20, '
                                      'TrE_OplataCukrowaOdCukrowZawartoscRoztwor, TrE_OplataCukrowaOdSubstancjiSlodzacych, '
                                      'TrE_OplataCukrowaOdKofeinyTauryny, TrE_OplataCukrowaDoliczDoCeny, TrE_StawkaOSS)'
                                      'VALUES ({self.optima_id}, {idx}, {idx}, {self.document_type.optima_class}, 1,'
                                      ' 0.0000, 0.0000, 1, 1, {self.document_item.product.optima_id},'
                                      ' {self.source_store.optima_id}, {self.document_item.product.name},'
                                      '{self.document_item.product.code}, "10.71.11", 1, 5.00, 2, 0.00, 1, 1,'
                                      ' {self.document_item.net_price}, 0.00, {self.document_item.net_price},"PLN", '
                                      '0, 0, 0, 1.000, 1, {self.document_item.net_price}, {self.document_item.quantity},'
                                      '0.0000, {self.document_item.product.unit.short_name},'
                                      ' {self.document_item.product.unit.short_name}, 0, 1.00, 1, 1.0000, 1.0000,'
                                      '{self.document_item.net_price}, {self.document_item.gross_price},'
                                      '{self.document_item.net_price}, 0.00, 0.00, 1.00, 1, 0.00, 0.00, 0, 0.00,'
                                      '{self.document_item.net_price}, {self.document_item.net_price}, '
                                      '{self.document_item.net_price}, {self.document_item.gross_price},'
                                      '0.00, 0, 0.00, 0.00, 0, 0, 0, 0, 0, 0, 0.0000, 0.0000, 0, 0, 0, 0.00,'
                                      '0, 0.00, -1, 1, 0, 0, -1, 1.00, 0.00, 0.00, 0.00, 0.000, 0, 0, 0, 0, 0.00, 0)')

    def recalculate_values(self):
        value_net = 0
        value_gross = 0
        for document_item in self.document_items.all():
            value_net += document_item.net_price * document_item.quantity
            value_gross += document_item.gross_price * document_item.quantity
        value_vat = value_gross - value_net
        self.value_vat += value_vat
        self.value_gross += value_gross
        self.value_net += value_net
        self.save()


class DocumentItem(WarehouseModel):
    optima_id = models.PositiveIntegerField(null=True, blank=True)
    document = models.ForeignKey(Document, on_delete=models.CASCADE, null=False, blank=False,
                                 related_name='document_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, blank=False,
                                related_name='document_items')
    quantity = models.PositiveIntegerField(null=False, blank=False)
    net_price = models.DecimalField(max_digits=12, decimal_places=2)
    gross_price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=False)

    def save(self, *args, **kwargs):
        self.gross_price = decimal.Decimal(self.net_price * decimal.Decimal(1.05)).quantize(decimal.Decimal('.01'),
                                                                                            rounding=decimal.ROUND_HALF_UP)
        super().save(*args, **kwargs)
        self.document.recalculate_values()
