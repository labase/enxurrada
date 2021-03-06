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
Enxurrada - Principal
############################################################

Módulo que define o modelo computacional de enchentes

"""
GUI = None


class Enxurrada:
    """Classe que define o editor de apresentações no espaço 2D

    :param navegador: Referência ao módulo navegador do Brython
    """
    BACIA = []

    def __init__(self, navegador):
        """Constroi os objetos iniciais. """
        global GUI
        self.gui = GUI = navegador
        self.svg = navegador.svg
        self.html = navegador.html
        self.ajax = navegador.ajax
        self.svgcanvas = self.cursor = self.icon = self.menu = self.back = self.div = None
        self.load = self.save = lambda ev: None
        self.dim = (800, 600)

