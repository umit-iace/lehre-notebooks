Notebooks zu verschiedenen Lehrveranstaltungen des IACE
=======================================================

.. image:: https://mybinder.org/badge_logo.svg
 :target: https://mybinder.org/v2/gh/umit-iace/lehre-notebooks/main

Advanced Control
----------------

.. |pad| unicode:: 0xA0 0xA0 0xA0 0xA0 0xA0 0xA0 0xA0 0xA0 0xA0 0xA0 0xA0 0xA0
   .. Breite der Bildspalte erzwingen; GitHub ignoriert :width: in RST

.. list-table::
   :header-rows: 1
   :widths: 15 20 12 28 25

   * - System
     - |pad|\ Skizze\ |pad|
     - Modell
     - Themen
     - Notebooks
   * - Zweimassen­schwinger
     - .. image:: images/twomass_thumb.png
     - linear
     - Modellierung, Steuerung, Regelung
     - | `Normalformen <zweimassenschwinger/Normalformen.ipynb>`__
       | `Vergleich Steuerung <zweimassenschwinger/VergleichSteuerung.ipynb>`__
   * - Brückenkran
     - .. image:: images/craneNonLin_thumb.png
     - linear / nichtlinear
     - Modellierung, Steuerung, Regelung, Beobachter
     - | `Normalformen <brueckenkran/Normalformen.ipynb>`__
       | `Regelung <brueckenkran/Regelung.ipynb>`__
       | `Vergleich Steuerung <brueckenkran/VergleichSteuerung.ipynb>`__
   * - Magnetlager
     - .. image:: images/magBall_thumb.png
     - nichtlinear
     - Modellierung, Steuerung, Regelung, Beobachter
     - | `Regelung <magnetlager/Regelung.ipynb>`__
       | `Vergleich Steuerung <magnetlager/VergleichSteuerung.ipynb>`__
   * - Gleichstrommotor
     - .. image:: images/dcMotor_thumb.png
     - linear
     - Normalformen, Steuerung, Regelung, Regulator
     - | `Normalformen <gleichstrommotor/Normalformen.ipynb>`__
       | `Regulator <gleichstrommotor/Regulator.ipynb>`__
       | `Vergleich Steuerung <gleichstrommotor/VergleichSteuerung.ipynb>`__
   * - Zweitank­system
     - .. image:: images/twoTank_thumb.png
     - nichtlinear
     - Normalform, Nulldynamik, E/A-Linearisierung, Flachheit, Steuerung, Regelung
     - | `Vergleich Steuerung <zweitank/VergleichSteuerung.ipynb>`__
       | `Vergleich Regelung <zweitank/VergleichRegelung.ipynb>`__
   * - Klimatisierung
     - .. image:: images/hvac_thumb.png
     - –
     - Parameteridentifikation
     - `Parameteridentifikation <klimatisierung/Parameteridentifikation.ipynb>`__
   * - allgemein
     - .. image:: images/saturation_thumb.png

       .. image:: images/smith_thumb.png
     - –
     - Stellgrößen­beschränkung, Smith-Prädiktor
     - | `Stellgrößen­beschränkung <allgemein/Stellgroessenbeschraenkung.ipynb>`__
       | `Totzeitsystem <allgemein/Totzeitsystem.ipynb>`__

Systeme mit örtlich verteilten Parametern
-----------------------------------------

*Beispielsysteme folgen.*

..
   Neue Systeme nach folgendem Muster ergänzen:

   .. list-table::
      :header-rows: 1
      :widths: 15 20 12 28 25

      * - System
        - Modell
        - Themen
        - Notebooks
      * - <System>
        - .. image:: images/<bild>_thumb.png
        - <Modell>
        - <Themen>
        - | `<Titel> <<ordner>/<Notebook>.ipynb>`__
