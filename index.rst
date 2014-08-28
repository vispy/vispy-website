.. meta_lalala::
   :google-site-verification: 

.. title:: Vispy: OpenGL-based interactive visualization in Python


.. slider:: ../_images/gallery
   This is where the gallery images get shown
   The html below is to make the gallery actually work :)


.. raw:: html
   
   <style rel="stylesheet" type="text/css">
      #carousel figure img  {
         height: 200px;
         padding: 0px;
         border: 1px solid #D4D4D4;
         }
   </style>
   
   <script>
      function shuffle(array) {
         var elementsRemaining = array.length, temp, randomIndex;
         while (elementsRemaining > 1) {
            randomIndex = Math.floor(Math.random() * elementsRemaining--);
            if (randomIndex != elementsRemaining) {
               temp = array[elementsRemaining];
               array[elementsRemaining] = array[randomIndex];
               array[randomIndex] = temp;
            }
         }
         return array;
      }
      
      $('#carousel ul').anoSlide(
         {
            items: 2,
            lazy: true,
            speed: 1000,
            auto: 4000,
            delay: 100,
            autostop: false,
            
            onConstruct: function(instance)
            {
               shuffle(instance.slides);
            },
            /* rewind should be instant */
            onStart: function(ui)
            {
               if (ui.index==0) 
               {
                  ui.instance.options.speed = 0;
               }            
            },
            onEnd: function(ui)
            {
               if (ui.index==0) 
               {
                  ui.instance.options.speed = 1000;
               }            
            },
         })
         
   </script>



Announcements
-------------

- **Release!** Version 0.3, August 27, 2014
- **EuroSciPy 2014**: talk at Saturday 30, and sprint at Sunday 31, August 2014
- `Article in **Linux Magazine**, French Edition <https://github.com/vispy/linuxmag-article>`__, July 2014
- **GSoC 2014**: `two GSoC students are currently working on Vispy under the PSF umbrella <https://github.com/vispy/vispy/wiki/Project.%20GSoC-2014>`__
- **Release!**, Version 0.2.1 04-11-2013
- **Presentation at BI forum**, Budapest, 6 November 2013
- **Presentation at Euroscipy**, Belgium, August 2013
- **EuroSciPy Sprint**, Belgium, August 2013
- **Release!** Version 0.1.0 14-08-2013


.. readme_insert:: ../README.rst
   The vispy readme gets inserted here.


Publications
------------

* `Hardware-accelerated interactive data visualization for neuroscience in Python <http://www.frontiersin.org/Journal/10.3389/fninf.2013.00036/full>`_ C. Rossant and K.D. Harris, Frontiers in Neuroinformatics, 7.36, (2013)

* `Shader-based Antialiased Dashed Stroked Polylines <http://jcgt.org/published/0002/02/08/>`_ N. P. Rougier. Journal of Computer Graphics Techniques, 2.2 (2013)

* `Higher Quality 2D Text Rendering <http://jcgt.org/published/0002/01/04/>`_ N. P. Rougier. Journal of Computer Graphics Techniques, 2.1 (2013)

* `Vispy, a future tool for interactive visualization <https://github.com/vispy/static/raw/master/vispy-biforum-2013.pdf>`_ - Talk at Budapest BI forum 2013

* `Vispy, a modern and interactive visualization framework <https://github.com/vispy/static/raw/master/vispy-euroscipy-2013.pdf>`_ - Talk at EuroScipy 2013

