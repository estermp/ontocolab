#! /usr/bin/env python
# -*- coding: UTF8 -*-
# Este arquivo é parte do programa Ontocolab
# Copyright 2011-2016 Ester M. Poegere <estermp@ufrj.br>,
# `Labase <http://labase.selfip.org/>`__; `GPL <http://is.gd/3Udt>`__.
#
# Ontocolab é um software livre; você pode redistribuí-lo e/ou
# modificá-lo dentro dos termos da Licença Pública Geral GNU como
# publicada pela Fundação do Software Livre (FSF); na versão 2 da
# Licença.
#
# Este programa é distribuído na esperança de que possa ser útil,
# mas SEM NENHUMA GARANTIA; sem uma garantia implícita de ADEQUAÇÃO
# a qualquer MERCADO ou APLICAÇÃO EM PARTICULAR. Veja a
# Licença Pública Geral GNU para maiores detalhes.
#
# Você deve ter recebido uma cópia da Licença Pública Geral GNU
# junto com este programa, se não, veja em <http://www.gnu.org/licenses/>


class Main:
    """
    Executa o ambiente cliente da ferramenta Ontocolab.

    :param go: Referência para o Pacote Gojs
    :param binding: Go js binding
    :param graph_model: Go js graph Model
    """

    def __init__(self, go, binding, graph_model):
        config = {
            "undoManager.isEnabled": True
        }
        mydiagram = mk(go.Diagram, "myDiagramDiv", config)
        mydiagram.nodeTemplate = mk(
            go.Node, "Auto",
            mk(go.Shape, "RoundedRectangle", binding("fill", "color")),
            mk(go.TextBlock, {"margin": 3}, binding("text", "key"))
        )

        mydiagram.model = graph_model(
            [
                {"key": "Alpha", "color": "lightblue"},
                {"key": "Beta", "color": "orange"},
                {"key": "Gamma", "color": "lightgreen"},
                {"key": "Delta", "color": "pink"}
            ],
            [
                {"from": "Alpha", "to": "Beta"},
                {"from": "Alpha", "to": "Gamma"},
                {"from": "Beta", "to": "Beta"},
                {"from": "Gamma", "to": "Delta"},
                {"from": "Delta", "to": "Alpha"}
            ])

mk = lambda *_: []


def main(make, go, binding, graph_model):
    """
    Programa principal do módulo cliente.

    :param make:
    :param go: Referência para o Pacote Gojs
    :param binding: Go js binding
    :param graph_model: Go js graph Model
    :return:
    """
    global mk
    mk = make

    Main(go, binding, graph_model)
