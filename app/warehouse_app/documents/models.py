import datetime
import decimal
import pyodbc
import logging

from django.db import models

from warehouse_app.utils.utils import OptimaConnection
from warehouse_app.products.models import Product
from warehouse_app.stores.models import Store
from warehouse_app.warehouse.models import WarehouseModel

logger = logging.getLogger()


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
        connection = OptimaConnection()
        cursor = connection.cursor
        logger.info('Start optima save')
        try:
            #TODO SELECT LATEST TrN_NumerNr FOR NUMERSTRIN CREATION
            #TODO AFTER INSERT GET LATEST NUMBER AND SAVE ON OBJECT
            #TODO PREPARE DOCUMENT ITEM TO SAVE TO OPTIMA
            #TODO MOVE QUERY TO HELPER CLASS
            cursor.execute('INSERT INTO CDN.TraNag ('
                           'TrN_DDfId, TrN_TypDokumentu, TrN_NumerString, TrN_NumerNr,'
                           'TrN_Bufor, TrN_Anulowany, TrN_DataDok, TrN_DataWys,'
                           'TrN_DataOpe, TrN_DataKur, TrN_TaxFreePotwierdzony, TrN_Korekta,'
                           'TrN_Fiskalna, TrN_StatusInt, TrN_Detal,TrN_Rodzaj,'
                           'TrN_PodmiotTyp, TrN_PodID, TrN_PodNazwa1, TrN_Finalny,'
                           'TrN_PodatekVat, TrN_Export, TrN_ZwolnionyZAkcyzy, TrN_OdbiorcaTyp,'
                           'TrN_OdbID, TrN_OdbNazwa1, TrN_PlatnikTyp, TrN_PlatnikID, '
                           'TrN_FADokumentDostawy, TrN_FinalnyWegiel, TrN_NrListuPrzewozowegoTypKuriera, TrN_FPlId, '
                           'TrN_Termin, TrN_TerminZwrotuKaucji,TrN_RazemNetto, TrN_RazemVAT, '
                           'TrN_RazemBrutto, TrN_RazemNettoWal,TrN_RazemVATWal, TrN_RazemBruttoWal,'
                           'TrN_KursNumer, TrN_KursL, TrN_KursM, TrN_PlatElemWalSys,'
                           'TrN_VatDlaDokWal, TrN_PlatKaucje, TrN_BlokadaPlatnosci, TrN_MagZrdId, '
                           'TrN_MagDocId, TrN_TypNB, TrN_Rabat, TrN_RabatWartosc,'
                           'TrN_TrSTyp, TrN_OpeZalID, TrN_StaZalId, TrN_TS_Zal, '
                           'TrN_OpeModID, TrN_StaModId, TrN_TS_Mod, TrN_Centrala,'
                           'TrN_DataTransportu, TrN_TrybNettoVAT, TrN_PARodzajKor, TrN_MetodaKasowa,'
                           'TrN_EdycjaTabelkiVAT, TrN_PlatnoscNaWZ, TrN_BzpId, TrN_RezerwacjaWew, '
                           'TrN_PAFACzesciowe, TrN_AktualizacjaCenyZakKor, TrN_StawkaNPOO, TrN_WartoscOO,'
                           'TrN_AwizoId, TrN_DokMOSMMId, TrN_PunktyZam, TrN_PunktyZap, '
                           'Trn_Sent, TrN_PCID, TrN_eSklepZrodlo, TrN_eSklepStatusDostawy, '
                           'TrN_NumerObcy, TrN_NumerPelnyPrw, TrN_PodNazwa2, TrN_PodNazwa3, '
                           'TrN_PodKraj, TrN_PodWojewodztwo, TrN_PodPowiat, TrN_PodGmina,'
                           'TrN_PodUlica, TrN_PodNrDomu, TrN_PodNrLokalu, TrN_PodMiasto,'
                           'TrN_PodKodPocztowy, TrN_PodPoczta,TrN_PodAdres2, TrN_PodNipKraj,'
                           'TrN_PodNipE, TrN_PodmiotGLN, TrN_OdbNazwa2, TrN_OdbNazwa3,'
                           'TrN_OdbKraj, TrN_OdbWojewodztwo, TrN_OdbPowiat,TrN_OdbGmina,'
                           'TrN_OdbUlica, TrN_OdbNrDomu, TrN_OdbNrLokalu, TrN_OdbMiasto,'
                           'TrN_OdbKodPocztowy, TrN_OdbPoczta, TrN_OdbAdres2, TrN_OdbNipKraj,'
                           'TrN_OdbNipE, TrN_OdbiorcaGLN, TrN_Kategoria, TrN_Waluta,'
                           'TrN_Odebral, TrN_Opis, TrN_NotaKorPrzed, TrN_NotaKorPo,'
                           'TrN_KodTransakcji, TrN_KodKraju, TrN_AkcyzaMiejsceWydania) VALUES ('
                           '?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,'
                           '?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,'
                           '?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,'
                           '?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,'
                           '?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,'
                           '?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,'
                           '?,?,?)',
                            self.document_type.optima_id, self.document_type.optima_class, self.document_type.numbering,
                            2, 1, 0, datetime.datetime.now(), datetime.datetime.now(), datetime.datetime.now(),
                            datetime.datetime.now(), 0, 0, 0, 0, 0, 312000, 1, 1, ".", 1, 0, 0, 0, 1, 1, ".",
                            1, 1, 0, 0, 0, 1, datetime.datetime.now(), datetime.datetime.now(),
                            self.value_net, self.value_vat, self.value_gross,
                            self.value_net, self.value_vat, self.value_gross, 3, 1.0000, 1,
                            0, 0, 0, 1, self.source_store.optima_id, self.destination_store.optima_id,
                            1, 0.00, 0.00, 0, 1, 2, datetime.datetime.now(), 1, 2, datetime.datetime.now(),
                            0, datetime.datetime.now(), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.00, 0, 0, 0, 0, 0, 1, 7, -1, "",
                            "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
                            "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "")
            tra_nag_id = cursor.execute("SELECT @@Identity").fetchone()[0]
            logger.info(tra_nag_id)
            # for idx, document_item in enumerate(self.document_items.all()):
            #     query_string_2 = (f'INSERT INTO CDN.TraElem (TrE_TrNId, TrE_Lp, TrE_LpPow, TrE_TyPDokumentu,'
            #                   f' TrE_Aktywny, TrE_RabatPromocyjny, TrE_RabatKorekta, TrE_PodmiotTyp, TrE_PodID,'
            #                   f'TrE_TwrId, TrE_MagId, TrE_TwrNazwa, TrE_TwrKod, TrE_TwrSWW, TrE_TwrTyp, TrE_Stawka, '
            #                   f'TrE_Flaga, TrE_Zrodlowa, TrE_TwCNumer, TrE_TypNB, TrE_Cena0, TrE_Rabat, TrE_CenaW,'
            #                   f'TrE_Waluta, TrE_Kaucja, TrE_WyborDostaw, TrE_KursNumer, TrE_KursL, Tre_KursM, '
            #                   f'TrE_CenaT, TrE_Ilosc, TrE_IloscKW, TrE_Jm, TrE_JmZ, TrE_JmCalkowite, '
            #                   f'TrE_JMPrzelicznikL, TrE_JMPRzelicznikM, TrE_IloscJM, TrE_IloscJMKW,'
            #                   f' TrE_WartoscNetto, TrE_WartoscBrutto, TrE_WartoscZakupu, TrE_KosztUslugi,'
            #                   f'TrE_KosztKGO, Tre_AkcyzaJMPomPrzelicznikL, Tre_AkcyzaJMPomPrzelicznikM, '
            #                   f'TrE_AkcyzaOpal, TrE_AkcyzaStawka, Tre_OdwrotneObciazenie, TrE_WartoscZakupuWylicz, '
            #                   f'TrE_Cena0WD, TrE_CenaWWD, TrE_WartoscNettoWal, TrE_WartoscBruttoWal, TrE_Prog,'
            #                   f'TrE_UpustTyp, TrE_Upust, TrE_UpustKnt, TrE_UpustKntTyp, TrE_IFA24Mag, TrE_IFA24,'
            #                   f'TrE_ZTwID, TrE_ZestawWiazanie, TrE_ZTwGlowny, TrE_ZTwIlosc, TrE_DoZwrotu, TrE_UslugaZlozonaId, '
            #                   f'TrE_UslugaZlozona, TrE_PATrEId, TrE_KWRoznicaKursowa, Tre_CenaZCzteremaMiejscami, '
            #                   f'TrE_FakZalKwotaMax, Tre_UstawAtrSQL, Tre_UstawAtrSQLDokTyp, TrE_SplitPay, TrE_KV7ID,'
            #                   f' TrE_CzySaCechyWymagane, TrE_OplataCukrowaPrzelicznikML, TrE_OplataCukrowaOdCukrowStala,'
            #                   f'TrE_OplataCukrowaOdCukrowZmienna, TrE_OplataCukrowaOdKofeinyTaurynyStala,'
            #                   f'TrE_OplataCukrowaOdCukrowZawartoscGram, TrE_OplataCukrowaOdCukrowZawartoscSokow20, '
            #                   f'TrE_OplataCukrowaOdCukrowZawartoscRoztwor, TrE_OplataCukrowaOdSubstancjiSlodzacych, '
            #                   f'TrE_OplataCukrowaOdKofeinyTauryny, TrE_OplataCukrowaDoliczDoCeny, TrE_StawkaOSS)'
            #                   f'VALUES ({tra_nag_id}, {idx}, {idx}, {self.document_type.optima_class}, 1,'
            #                   f' 0.0000, 0.0000, 1, 1, {self.document_item.product.optima_id},'
            #                   f' {self.source_store.optima_id}, {self.document_item.product.name},'
            #                   f'{self.document_item.product.code}, "10.71.11", 1, 5.00, 2, 0.00, 1, 1,'
            #                   f' {self.document_item.net_price}, 0.00, {self.document_item.net_price},"PLN", '
            #                   f'0, 0, 0, 1.000, 1, {self.document_item.net_price}, {self.document_item.quantity},'
            #                   f'0.0000, {self.document_item.product.unit.short_name},'
            #                   f' {self.document_item.product.unit.short_name}, 0, 1.00, 1, 1.0000, 1.0000,'
            #                   f'{self.document_item.net_price}, {self.document_item.gross_price},'
            #                   f'{self.document_item.net_price}, 0.00, 0.00, 1.00, 1, 0.00, 0.00, 0, 0.00,'
            #                   f'{self.document_item.net_price}, {self.document_item.net_price}, '
            #                   f'{self.document_item.net_price}, {self.document_item.gross_price},'
            #                   f'0.00, 0, 0.00, 0.00, 0, 0, 0, 0, 0, 0, 0.0000, 0.0000, 0, 0, 0, 0.00,'
            #                   f'0, 0.00, -1, 1, 0, 0, -1, 1.00, 0.00, 0.00, 0.00, 0.000, 0, 0, 0, 0, 0.00, 0)')
            #     logger.info(query_string_2)
            #     cursor.execute(query_string_2)
        except Exception as err:
            logger.info(err)
            connection.cnxn.rollback()
        else:
            connection.cnxn.commit()
            self.optima_id = tra_nag_id
            self.save()

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
