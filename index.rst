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
  
  1) To allow more sharing of code between visualization projects 
  and making it easier to use OpenGL. This is doen by providing an 
  object oriented interface to OpenGL and by providing a framework for 
  embedding OpenGL in applications and the browser.
  
  2) To create fast, interactive and beautiful (i.e. high quality) 
  visualizations, using a high level interface. Also for big data.

Vispy is organized in the following modules. The visualisation modules 
are organized in levels, that provide API's at increasing abstraction.

* vispy.gl: (level 1) low level OpenGL API 
* vispy.oogl: (level 2) object oriented OpenGL API
* vispy.visuals: (level 3) visuals layer (higher level visualization objects)
* To come: (level 4) Functional interface
* (level 5)... something with big data?
* vispy.app: simple application framework for creating/embedding OpenGL widgets
* vispy.event: event system.
 
Vispy can be a basis for other libraries, which can hook into vispy at the desired level.
But vispy also aims to be a visualziation toolkit on its own.

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



