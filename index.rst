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

      <h2>High-performance interactive data visualization in Python</h2>

      <a class="btn btn-warning clearfix" href="/download">
      <i class="icon-download icon-white"></i>Download</a>


Vispy is a **high-performance interactive 2D/3D data visualization
library**. Vispy leverages the computational power of modern **Graphics
Processing Units (GPUs)** through the **OpenGL** library to display
very large datasets. Applications of Vispy include:

* High-quality interactive scientific plots with millions of points.
* Direct visualization of real-time data.
* Fast interactive visualization of 3D models (meshes, volume rendering).
* OpenGL visualization demos.
* Scientific GUIs with fast, scalable visualization widgets (Qt or
  IPython notebook with WebGL).

We're now working on vispy's higher level interfaces, so that it will
become easy for everyone to create awesome and fast visualizations.


Announcements
-------------

- **Release!** Version 0.3, August 27, 2014
- **EuroSciPy 2014**: talk at Friday 28, and sprint at Sunday 31, August 2014
- `Article in **Linux Magazine**, French Edition <https://github.com/vispy/linuxmag-article>`__, July 2014
- **GSoC 2014**: `two GSoC students are currently working on Vispy under the PSF umbrella <https://github.com/vispy/vispy/wiki/Project.%20GSoC-2014>`__
- **Release!**, Version 0.2.1 04-11-2013
- **Presentation at BI forum**, Budapest, 6 November 2013
- **Presentation at Euroscipy**, Belgium, August 2013
- **EuroSciPy Sprint**, Belgium, August 2013
- **Release!** Version 0.1.0 14-08-2013


Using Vispy
-----------

Vispy is a young library under heavy development at this time. It
targets two categories of users:

1. **Users knowing OpenGL**, or willing to learn OpenGL, who want to
   create beautiful and fast interactive 2D/3D visualizations in Python
   as easily as possible.
2. **Scientists without any knowledge of OpenGL**, who are seeking a
   high-level, high-performance plotting toolkit.

If you're in the first category, you can already start using Vispy.
Vispy offers a Pythonic, NumPy-aware, user-friendly interface for OpenGL
ES 2.0 called **gloo**. You can focus on writing your GLSL code instead
of dealing with the complicated OpenGL API - Vispy takes care of that
automatically for you.

If you're in the second category, we're starting to build experimental
high-level plotting interfaces. Notably, Vispy now ships a very basic
and experimental OpenGL backend for matplotlib.


Installation
------------

Vispy runs on Python 2.6+ and Python 3.3+ and depends on NumPy. You
also need a backend (PyQt4, PySide, glfw, GLUT, pyglet, or SDL2).

As Vispy is under heavy development at this time, we highly recommend
you to use the development version on Github  (master branch). You need
to clone the repository and install Vispy with `python setup.py
install`.


Structure of Vispy
------------------

Currently, the main subpackages are:

* **app**: integrates an event system and offers a unified interface on
  top of many window backends (Qt4, wx, glfw, GLUT, IPython notebook
  with/without WebGL, and others). Relatively stable API.
* **gloo**: a Pythonic, object-oriented interface to OpenGL. Relatively
  stable API.
* **mpl_plot**: an OpenGL backend for matplotlib. Experimental.
* **scene**: this is the system underlying our upcoming high level
  visualization interfaces. Under heavy development and still
  experimental, it contains several modules.
    * **Visuals** are graphical abstractions representing 2D shapes, 3D
      meshes, text, etc.
    * **Transforms** implement 2D/3D transformations implemented on both
      CPU and GPU.
    * **Shaders** implements a shader composition system for plumbing
      together snippets of GLSL code.
    * The **scene graph** tracks all objects within a transformation
      graph.

The API of all public interfaces are subject to change in the future,
although **app** and **gloo** are *relatively* stable at this point.


Publications
------------

* `Hardware-accelerated interactive data visualization for neuroscience in Python <http://www.frontiersin.org/Journal/10.3389/fninf.2013.00036/full>`_ C. Rossant and K.D. Harris, Frontiers in Neuroinformatics, 7.36, (2013)

* `Shader-based Antialiased Dashed Stroked Polylines <http://jcgt.org/published/0002/02/08/>`_ N. P. Rougier. Journal of Computer Graphics Techniques, 2.2 (2013)

* `Higher Quality 2D Text Rendering <http://jcgt.org/published/0002/01/04/>`_ N. P. Rougier. Journal of Computer Graphics Techniques, 2.1 (2013)

* `Vispy, a future tool for interactive visualization <https://github.com/vispy/static/raw/master/vispy-biforum-2013.pdf>`_ - Talk at Budapest BI forum 2013

* `Vispy, a modern and interactive visualization framework <https://github.com/vispy/static/raw/master/vispy-euroscipy-2013.pdf>`_ - Talk at EuroScipy 2013

