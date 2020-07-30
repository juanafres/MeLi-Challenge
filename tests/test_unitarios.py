import unittest 
from mutant import Mutant, Stats
import app




class MutantsTest(unittest.TestCase):
    def setUp(self):
        self.client = app
        self.humano = Mutant()
        self.estadistica = Stats()

    def humano_no_mutante(self):
        resp = self.humano.is_mutant(str('["AAATTT","CCCGGG","CTCAGT","ACAGGC","AATTCG","CCCATG"]'))
        self.assertFalse(resp)

    def humano_mutante(self):
        resp = self.humano.is_mutant(str('["AAAAAT","CCCGGG","CTCAGT","ACAGGC","AATTCG","CCCATG"]'))
        self.assertTrue(resp)

    def humano_invalido(self):
        resp = self.humano.is_mutant(str('["AAATTT","CCCGGG","CTCHHT","ACAGGC","AATTCG","CCCATG"]'))
        self.assertFalse(resp)

    def humano_mutante_horizontal(self):
        resp = self.humano.is_mutant(str('["AAAAAT","CCCGCG","CTCAGT","ACAGGC","AATTCG","CCCATG"]'))
        self.assertTrue(resp)
    
    def humano_mutante_vertical(self):
        resp = self.humano.is_mutant(str('["AAATTT","ACCGGG","ATCAGT","ACAGGC","AATTCG","CCCATG"]'))
        self.assertTrue(resp)

    def humano_mutante_diagonal(self):
        resp = self.humano.is_mutant(str('["AAATTT","CACGGG","CTAAGT","ACAAGC","AATTAG","CCCATA"]'))
        self.assertTrue(resp)

    def obtener_estadisticas(self):
        resp = self.estadistica.get_stats_dna()
        assert resp is not None

    def method_invalid(self):
        res = self.client.get('/mutant/')
        self.assertEqual(400, res.status_code)

    def method_ok_no_json(self):
        res = self.client.post('/mutant/')
        self.assertEqual(400, res.status_code)

    def stats_ok(self):
        res = self.client.get('/stats')
        self.assertEqual(200, res.status_code)


if __name__ == '__main__':
    unittest.main()


