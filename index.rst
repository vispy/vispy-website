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


Vispy is a collaborative project that has the goal to allow more sharing 
of code between visualization projects based on OpenGL. It does this 
by providing powerful interfaces to OpenGL, at different levels of 
abstraction and generality.

Vispy is organized in layers:

  # Low level OpenGL API
  # Object oriented OpenGL API
  # Visuals layer
  # Functional interface
  # ... something with big data?
 
Vispy can be a basis for other libraries, which can hook into vispy at the desired level.
But vispy also aims to be a visualziation toolkit on its own (e.g. level 4).

Currently, layer 1 and 2 are in Beta stage, work on layer 3 is commencing.



Getting Started
---------------

Visualization with ``vispy`` is easy!  For more code samples, please
visit our `examples <http://api.vispy.org/en/latest/examples.html>`__.


.. container:: row-fluid

   .. container:: span6

      ::

        from vispy import app, gl

        c = app.Canvas(show=True)

        @c.connect
        def on_paint(event):
            gl.glClearColor(0,1,0,1)
            gl.glClear(gl.GL_COLOR_BUFFER_BIT)

        app.run()



Announcements
-------------

- **Presentation at Euroscipy**, Belgium, August 2013
- **EuroSciPy Sprint**, Belgium, August 2013
- **Release!** Version 0.1.0 14-08-2013



