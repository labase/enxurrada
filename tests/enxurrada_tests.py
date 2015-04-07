# -*- coding: UTF8 -*-
# Este arquivo é parte do programa Enxurrada
# Copyright 2013-2015 Carlo Oliveira <carlo@nce.ufrj.br>,
# `Labase <http://labase.selfip.org/>`__; `GPL <http://is.gd/3Udt>`__.
#
# Enxurrada é um software livre; você pode redistribuí-lo e/ou
# modificá-lo dentro dos termos da Licença Pública Geral GNU como
# publicada pela Fundação do Software Livre (FSF); na versão 2 da
# Licença.
#
# Este programa é distribuído na esperança de que possa ser  útil,
# mas SEM NENHUMA GARANTIA; sem uma garantia implícita de ADEQUAÇÃO
#  a qualquer MERCADO ou APLICAÇÃO EM PARTICULAR. Veja a
# Licença Pública Geral GNU para maiores detalhes.
#
# Você deve ter recebido uma cópia da Licença Pública Geral GNU
# junto com este programa, se não, veja em <http://www.gnu.org/licenses/>

"""
############################################################
Enxurrada - Teste Principal
############################################################

Verifica a funcionalidade do cliente web.

"""
import unittest
from enxurrada.core import Enxurrada
from enxurrada import main
import sys
if sys.version_info[0] == 2:
    from mock import MagicMock, patch, ANY
else:
    from unittest.mock import MagicMock, patch, ANY


class EnxurradaTest(unittest.TestCase):
    class Evento:
        x = y = 42
    EV = Evento()

    def setUp(self):
        self.gui = MagicMock(name="gui")
        modules = {
            'urllib': self.gui,
            'urllib.request': self.gui.request,
            'urllib.request.urlopen': self.gui.request.urlopen
        }
        uop = MagicMock(name="file")
        self.gui.request.urlopen.return_value = (uop, 0, 0)
        # uop.read = MagicMock(name="data", return_value=WCONT)
        self.module_patcher = patch.dict('sys.modules', modules)
        self.module_patcher.start()
        self.gui.__le__ = MagicMock(name="APPEND")
        self.app = Enxurrada(self.gui)
        self.EV.x = self.EV.y = 42

    def test_main(self):
        """cria instancia de enxurrada"""
        imp = main(self.gui)
        self.assertIsInstance(imp, Enxurrada, "Instância não criada")


if __name__ == '__main__':
    unittest.main()