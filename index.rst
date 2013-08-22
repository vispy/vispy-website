.. meta_lalala::
   :google-site-verification: 

.. title:: Vispy: OpenGL-based interactive visualization in Python

.. container_commented:: well hero row-fluid summary-box

   .. raw:: html

      <div class="gallery-random">
        <script src="http://vispy.org/docs/dev/_static/random.js"></script>
        <script type="text/javascript">
          insert_gallery();
        </script>
      </div>

      <h2>Image processing in Python</h2>

    lalala some text

   .. raw:: html

      <a class="btn btn-warning clearfix" href="/download">
      <i class="icon-download icon-white"></i>Download</a>


Vispy is a collaborative project that has two main goals: 
1) To make it easier to use OpenGL (also in the browser) 
and allow more sharing of code between visualization projects. 
2) To create fast, interactive and beautiful (i.e. high quality) 
visualizations, using a high level interface (also for big data).

Vispy is organized in the following modules:

* **vispy.gl**: low level OpenGL API (level 1)
* **vispy.oogl**: object oriented OpenGL API (level 2)
* **vispy.visuals**: visuals layer (level 3)
* To come: functional interface (level 4) 
* ... something with big data? (level 5)
* **vispy.app**: simple application framework for creating/embedding OpenGL widgets
* **vispy.event**: event system.
 
The visualisation modules are organized in levels that provide API's at 
increasing abstraction. Libraries and applications that
use vispy can use it at the desired level.

Currently, layer 1 and 2 are in Beta stage, work on layer 3 is commencing.



Announcements
-------------

- **Presentation at Euroscipy**, Belgium, August 2013
- **EuroSciPy Sprint**, Belgium, August 2013
- **Release!** Version 0.1.0 14-08-2013


Getting Started
---------------

Visualization with ``vispy`` is easy!  For more code samples, please
visit the examples section in the `documentation <http://vispy.readthedocs.org>`__.


.. container:: row-fluid

   .. container:: span6

      ::
        
        # Note that this needs vispy version > 0.1.0
        from vispy import app, gl

        c = app.Canvas(show=True)

        @c.connect
        def on_paint(event):
            gl.glClearColor(0,1,0,1)
            gl.glClear(gl.GL_COLOR_BUFFER_BIT)

        app.run()



Installation
------------

Vispy runs on Python 2.6 and higher, including Python 3. 
Vispy depends on Numpy and PyOpenGL.

Since Vispy is pure Python, installation is easy: ``pip install vispy``. 
Alternatively, you can get the source and run ``python setup.py install``.



