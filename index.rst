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


Vispy is an **OpenGL-based interactive visualization library in
Python**. Its goal is to make it easy to create beautiful and fast
dynamic visualizations. For example, **scientific plotting** of tens
of millions of points, interacting with complex polygonial models, and
(dynamic) volume rendering. All thanks to the graphics card's hardware
acceleration.


Status
------

Vispy will eventually offer graphical APIs at multiple levels, including
a matplotlib-like scientific plotting library. Currently, only the
lowest-level API is implemented: it brings an easy-to-use Pythonic
object-oriented interface to OpenGL. This layer requires you to have
basic knowledge of modern OpenGL (notably the OpenGL shading language,
GLSL). 

For this reason, 
**Vispy is not yet suitable for the general scientist, but it will be in the future** 
(in several months at the very least).
We are currently working on higher level layers. They will hide most
OpenGL concepts and let you create beautiful visualizations in a few
lines of code. Stay tuned!


Announcements
-------------

- **Release!**, Version 0.2.1 04-11-2013
- **Presentation at BI forum**, Budapest, 6 November 2013
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
        from vispy import app
        from vispy.gloo import gl

        c = app.Canvas(show=True)

        @c.connect
        def on_paint(event):
            gl.glClearColor(0,1,0,1)
            gl.glClear(gl.GL_COLOR_BUFFER_BIT)

        app.run()


Organization
------------
Vispy is organized in the following modules:

* **vispy.app**: simple application framework for creating/embedding OpenGL widgets
* **vispy.util**: Various utilities, mostly for internal use
* **vispy.gloo**: object oriented OpenGL API
* **vispy.visuals**: visuals layer (planned)
* **vispy.pyplot**: functional interface (planned)

The visualisation modules are organized in levels that provide API's at 
increasing abstraction. Libraries and applications that
use vispy can use it at the desired level.

``vispy.app`` and ``vispy.gloo`` are currently in beta stage; we try to
keep the API's stable, but may introduce small changes.


Installation
------------

Vispy runs on Python 2.6 and higher, including Python 3. 
Vispy depends on Numpy and PyOpenGL.

Since Vispy is pure Python, installation is easy: ``pip install vispy``. 
Alternatively, you can get the source and run ``python setup.py install``.


About us
--------

The core development team consists of Luke Campagnola, Almar Klein,
Nicolas Rougier and Cyrille Rossant. We have each written our own Python
visualization toolkit (PyQtGraph, Visvis, Glumpy and Galry,
respectively), and decided to team-up.

Vispy will eventually replace all of our visualization libraries, so
you can expect vispy to have all the features of our respective toolkits
combined, and more.


Publications on Vispy 
---------------------

* `Vispy, a future tool for interactive visualization <https://github.com/vispy/static/raw/master/vispy-biforum-2013.pdf>`_ - Talk at Budapest BI forum 2013

* `Vispy, a modern and interactive visualization framework <https://github.com/vispy/static/raw/master/vispy-euroscipy-2013.pdf>`_ - Talk at EuroScipy 2013


