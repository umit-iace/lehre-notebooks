Notebooks zu verschiedenen Lehrveranstaltungen des IACE
=======================================================

.. image:: https://mybinder.org/badge_logo.svg
 :target: https://mybinder.org/v2/gh/umit-iace/lehre-notebooks/main

Advanced Control
----------------

.. list-table::
   :header-rows: 1
   :widths: 15 20 12 28 25

   * - System
     - Skizze
     - Modell
     - Themen
     - Notebooks
   * - Zweimassenschwinger
     - .. image:: images/twomass.png
          :width: 200px
     - linear
     - Modellierung, Steuerung, Regelung
     - | `Normalformen <zweimassenschwinger/Normalformen.ipynb>`__
       | `Vergleich Steuerung <zweimassenschwinger/VergleichSteuerung.ipynb>`__
   * - Brückenkran
     - .. image:: images/craneNonLin.png
          :height: 150px
     - linear/nichtlinear
     - Modellierung, Steuerung, Regelung, Beobachter
     - | `Normalformen <brueckenkran/Normalformen.ipynb>`__
       | `Regelung <brueckenkran/Regelung.ipynb>`__
       | `Vergleich Steuerung <brueckenkran/VergleichSteuerung.ipynb>`__
   * - Magnetlager
     - .. image:: images/magBall.png
          :height: 150px
     - nichtlinear
     - Modellierung, Steuerung, Regelung, Beobachter
     - | `Regelung <magnetlager/Regelung.ipynb>`__
       | `Vergleich Steuerung <magnetlager/VergleichSteuerung.ipynb>`__
   * - Gleichstrommotor
     - .. image:: images/dcMotor.png
          :width: 200px
     - linear
     - Normalformen, Steuerung, Regelung, Regulator
     - | `Normalformen <gleichstrommotor/Normalformen.ipynb>`__
       | `Regulator <gleichstrommotor/Regulator.ipynb>`__
       | `Vergleich Steuerung <gleichstrommotor/VergleichSteuerung.ipynb>`__
   * - Klimatisierung
     - .. image:: images/hvac.png
          :width: 200px
     - –
     - Parameteridentifikation
     - `Parameteridentifikation <klimatisierung/Parameteridentifikation.ipynb>`__
   * - allgemein
     - .. image:: images/saturation.png
          :width: 200px

       .. image:: images/smith.png
          :width: 200px
     - –
     - Stellgrößenbeschränkung, Smith-Prädiktor
     - | `Stellgrößenbeschränkung <allgemein/Stellgroessenbeschraenkung.ipynb>`__
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
        - .. image:: images/<bild>.png
             :width: 200px
        - <Modell>
        - <Themen>
        - | `<Titel> <<ordner>/<Notebook>.ipynb>`__
