import datetime


class WarehouseDocument:

    def __init__(self, document, cursor):
        self.cursor = cursor
        self.document_type_optima_id = document.document_type.optima_id
        self.document_type_optima_class = document.document_type.optima_class
        self.document_type_numbering = document.document_type.numbering
        self.document_type_details_id = 312000
        self.value_net = document.value_net
        self.value_gross = document.value_gross
        self.value_vat = document.value_vat
        self.source_store = document.source_store.optima_id
        self.destination_store = document.destination_store.optima_id
        self.current_number = self._get_current_number()

    def _get_current_number(self):
        query = "SELECT MAX(TrN_NumerNr) FROM CDN.TraNag WHERE TrN_DDfId={0} AND TrN_NumerString like '%/@numerS/{1}'"
        id = self.cursor.execute(query.format(self.document_type_optima_id, datetime.date.today().year)).fetchone()[0]
        new_id = id + 1
        self.number_string = self.document_type_numbering.replace('@numerS', str(new_id))
        return new_id

    def _get_optima_id(self):
        return self.cursor.execute("SELECT @@Identity").fetchone()[0]

    def export_to_optima(self):
        self.cursor.execute('INSERT INTO CDN.TraNag ('
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
                            'TrN_KodTransakcji, TrN_KodKraju, TrN_AkcyzaMiejsceWydania'
                            ') VALUES ('
                            '?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,'
                            '?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,'
                            '?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,'
                            '?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,'
                            '?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,'
                            '?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,'
                            '?,?,?)',
                            self.document_type_optima_id, self.document_type_optima_class, self.document_type_numbering,
                            self.current_number, 1, 0, datetime.datetime(2022, 6, 30, 0, 0, 0, 0), datetime.datetime(2022, 6, 30, 0, 0, 0, 0),
                            datetime.datetime(2022, 6, 30, 0, 0, 0, 0), datetime.datetime(2022, 6, 30, 0, 0, 0, 0), 0, 0, 0, 0, 0,
                            self.document_type_details_id,
                            1, 1, ".", 1, 0, 0, 0, 1, 1, ".", 1, 1, 0, 0, 0, 1,
                            datetime.datetime(2022, 6, 30, 0, 0, 0, 0), datetime.datetime(2022, 6, 30, 0, 0, 0, 0), self.value_net, self.value_vat,
                            self.value_gross, self.value_net, self.value_vat, self.value_gross, 3, 1.0000, 1,
                            0, 0, 0, 1, self.source_store, self.destination_store, 1, 0.00, 0.00, 0, 1, 2,
                            datetime.datetime(2022, 6, 30, 0, 0, 0, 0), 1, 2, datetime.datetime(2022, 6, 30, 0, 0, 0, 0), 0, datetime.datetime(2022, 6, 30, 0, 0, 0, 0),
                            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.00, 0, 0, 0, 0, 0, 1, 7, -1,
                            "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
                            "",
                            "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "")
        optima_id = self._get_optima_id()
        return optima_id


class WarehouseDocumentItem:
    def __init__(self, idx, document_item, cursor):
        self.cursor = cursor
        self.idx = idx
        self.tra_nag_id = document_item.document.optima_id
        self.document_type = document_item.document.document_type.optima_class
        self.product_id = document_item.product.optima_id
        self.product_name = document_item.product.name
        self.product_code = document_item.product.code
        self.unit = document_item.product.unit.short_name
        self.source_store = document_item.document.source_store.optima_id
        self.net_price = document_item.net_price
        self.gross_price = document_item.gross_price
        self.currency = 'PLN'
        self.quantity = document_item.quantity
        self.ssw = "10.71.11"
        self.vat = 5.00

    def _get_optima_id(self):
        return self.cursor.execute("SELECT @@Identity").fetchone()[0]

    def export_to_optima(self):
        self.cursor.execute('INSERT INTO CDN.TraElem ('
                              'TrE_TrNId, TrE_Lp, TrE_LpPow, TrE_TyPDokumentu,'
                              'TrE_Aktywny, TrE_RabatPromocyjny, TrE_RabatKorekta, TrE_PodmiotTyp,'
                              'TrE_PodID, TrE_TwrId, TrE_MagId, TrE_TwrNazwa, '
                              'TrE_TwrKod, TrE_TwrSWW, TrE_TwrTyp, TrE_Stawka, '
                              'TrE_Flaga, TrE_Zrodlowa, TrE_TwCNumer, TrE_TypNB,'
                              'TrE_Cena0, TrE_Rabat, TrE_CenaW, TrE_Waluta, '
                              'TrE_Kaucja, TrE_WyborDostaw, TrE_KursNumer, TrE_KursL,'
                              'Tre_KursM, TrE_CenaT, TrE_Ilosc, TrE_IloscKW, '
                              'TrE_Jm, TrE_JmZ, TrE_JmCalkowite, TrE_JMPrzelicznikL, '
                              'TrE_JMPRzelicznikM, TrE_IloscJM, TrE_IloscJMKW, TrE_WartoscNetto, '
                              'TrE_WartoscBrutto, TrE_KosztUslugi, TrE_KosztKGO, '
                              'Tre_AkcyzaJMPomPrzelicznikL, Tre_AkcyzaJMPomPrzelicznikM, TrE_AkcyzaOpal, TrE_AkcyzaStawka,'
                              'Tre_OdwrotneObciazenie, TrE_WartoscZakupuWylicz, TrE_Cena0WD, TrE_CenaWWD, '
                              'TrE_WartoscNettoWal, TrE_WartoscBruttoWal, TrE_Prog, TrE_UpustTyp, '
                              'TrE_Upust, TrE_UpustKnt, TrE_UpustKntTyp, TrE_IFA24Mag,'
                              'TrE_IFA24, TrE_ZTwID, TrE_ZestawWiazanie, TrE_ZTwGlowny, '
                              'TrE_ZTwIlosc, TrE_DoZwrotu, TrE_UslugaZlozonaId, TrE_UslugaZlozona, '
                              'TrE_PATrEId, TrE_KWRoznicaKursowa, Tre_CenaZCzteremaMiejscami, TrE_FakZalKwotaMax, '
                              'Tre_UstawAtrSQL, Tre_UstawAtrSQLDokTyp, TrE_SplitPay, TrE_KV7ID,'
                              'TrE_CzySaCechyWymagane, TrE_OplataCukrowaPrzelicznikML, TrE_OplataCukrowaOdCukrowStala, TrE_OplataCukrowaOdCukrowZmienna, '
                              'TrE_OplataCukrowaOdKofeinyTaurynyStala, TrE_OplataCukrowaOdCukrowZawartoscGram, TrE_OplataCukrowaOdCukrowZawartoscSokow20, TrE_OplataCukrowaOdCukrowZawartoscRoztwor,'
                              'TrE_OplataCukrowaOdSubstancjiSlodzacych, TrE_OplataCukrowaOdKofeinyTauryny, TrE_OplataCukrowaDoliczDoCeny, TrE_StawkaOSS,'
                              'TrE_DataDok, TrE_DataOpe, TrE_TwrEAN, TrE_TwrNumerKat,'
                              'TrE_TwrOpis, TrE_Akcyza_Kod, TrE_Akcyza_Wartosc, TrE_SJRodzajPaliwa,'
                              'TrE_SJSystemCertyfikacji, TrE_SJPopiol, TrE_SJCzesciLotne, TrE_SJWartoscOpalowa,'
                              'TrE_SJZdolnoscSpiekania, TrE_SJWymiarZiarna, TrE_SJZawartoscPodziarna, TrE_SJZawartoscNadziarna,'
                              'TrE_SJZawartoscWilgoci, TrE_KodCN, TrE_Atr1_Kod, TrE_Atr1_Wartosc,'
                              'TrE_Atr2_Kod, TrE_Atr2_Wartosc, TrE_Atr3_Kod, TrE_Atr3_Wartosc,'
                              'TrE_Atr4_Kod, TrE_Atr4_Wartosc, TrE_Atr5_Kod,TrE_Atr5_Wartosc,'
                              'TrE_ZTwKod, TrE_OplataCukrowaNumerPartiiTowaru, TrE_TwrKodDostawcy'
                              ')VALUES ('
                              '?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,'
                              '?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,'
                              '?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,'
                              '?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,'
                              '?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,'
                              '?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                              self.tra_nag_id, self.idx, self.idx, self.document_type, 1,
                              0.0000, 0.0000, 1, 1, self.product_id,
                              self.source_store, self.product_name,
                              self.product_code, self.ssw, 1, self.vat, 2, 0.00, 1, 1,
                              self.net_price, 0.00, self.net_price, self.currency,
                              0, 0, 0, 1.000, 1, self.net_price, self.quantity,
                              0.0000, self.unit, self.unit, 0, 1.00, 1, self.quantity, 1.0000,
                              self.net_price, self.gross_price,
                              0.00, 0.00, 1.00, 1, 0.00, 0.00, 0, 0.00,
                              self.net_price, self.net_price,
                              self.net_price, self.gross_price,
                              0.00, 0, 0.00, 0.00, 0, 0, 0, 0, 0, 0, 0.0000, 0.0000, 0, 0, 0, 0.00,
                              0, 0.00, -1, 1, 0, 0, -1, 1.00, 0.00, 0.00, 0.00, 0.000, 0, 0, 0, 0, 0.00, 0,
                              datetime.datetime(2022, 6, 30, 0, 0, 0, 0), datetime.datetime(2022, 6, 30, 0, 0, 0, 0),
                              "", "", "", "", "", "", "", "", "", "", "",
                              "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "")

        optima_id = self._get_optima_id()
        return optima_id
