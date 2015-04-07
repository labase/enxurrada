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
Enxurrada - Pacote cliente
############################################################

Define a função main do módulo enxurrada, criando uma instância de Enxurrada

"""
__version__ = "0.1.0"
from .core import Enxurrada


def main(browser):
    print('Enxurrada '+__version__)
    enxurrada = Enxurrada(browser)
    return enxurrada