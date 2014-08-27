.. meta_lalala::
   :google-site-verification: 

.. title:: Vispy: OpenGL-based interactive visualization in Python


Vispy is a **high-performance interactive 2D/3D data visualization
library**. Vispy leverages the computational power of modern **Graphics
Processing Units (GPUs)** through the **OpenGL** library to display very
large datasets. Applications of Vispy include:

-  High-quality interactive scientific plots with millions of points.
-  Direct visualization of real-time data.
-  Fast interactive visualization of 3D models (meshes, volume
   rendering).
-  OpenGL visualization demos.
-  Scientific GUIs with fast, scalable visualization widgets (Qt or
   `IPython notebook <http://ipython.org/notebook.html>`__ with WebGL).

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

Vispy runs on Python 2.6+ and Python 3.3+ and depends on NumPy. You also
need a backend (PyQt4/PySide, glfw, GLUT, pyglet, or SDL).

As Vispy is under heavy development at this time, we highly recommend
you to use the development version on Github (master branch). You need
to clone the repository and install Vispy with
``python setup.py install``.

Structure of Vispy
------------------

Currently, the main subpackages are:

-  **app**: integrates an event system and offers a unified interface on
   top of many window backends (Qt4, wx, glfw, GLUT, IPython notebook
   with/without WebGL, and others). Relatively stable API.
-  **gloo**: a Pythonic, object-oriented interface to OpenGL. Relatively
   stable API.
-  **mpl\_plot**: an OpenGL backend for matplotlib. Experimental.
-  **scene**: this is the system underlying our upcoming high level
   visualization interfaces. Under heavy development and still
   experimental, it contains several modules.

   -  **Visuals** are graphical abstractions representing 2D shapes, 3D
      meshes, text, etc.
   -  **Transforms** implement 2D/3D transformations implemented on both
      CPU and GPU.
   -  **Shaders** implements a shader composition system for plumbing
      together snippets of GLSL code.
   -  The **scene graph** tracks all objects within a transformation
      graph.

The API of all public interfaces are subject to change in the future,
although **app** and **gloo** are *relatively* stable at this point.

About us
--------

The core development team consists of:

-  `Luke Campagnola <http://luke.campagnola.me/>`__
-  `Almar Klein <http://www.almarklein.org/>`__
-  `Eric Larson <http://larsoner.com>`__
-  `Cyrille Rossant <http://cyrille.rossant.net>`__
-  `Nicolas Rougier <http://www.loria.fr/~rougier/index.html>`__

Four of us have written our own Python visualization toolkit
(`PyQtGraph <http://www.pyqtgraph.org/>`__ by LC,
`Visvis <https://code.google.com/p/visvis/>`__ by AK,
`Glumpy <https://github.com/rougier/Glumpy>`__ by NR, and
`Galry <https://github.com/rossant/galry>`__ by CR), and we decided to
team up to create a unique high-performance, high-quality interactive
visualization library.


Publications
------------

* `Hardware-accelerated interactive data visualization for neuroscience in Python <http://www.frontiersin.org/Journal/10.3389/fninf.2013.00036/full>`_ C. Rossant and K.D. Harris, Frontiers in Neuroinformatics, 7.36, (2013)

* `Shader-based Antialiased Dashed Stroked Polylines <http://jcgt.org/published/0002/02/08/>`_ N. P. Rougier. Journal of Computer Graphics Techniques, 2.2 (2013)

* `Higher Quality 2D Text Rendering <http://jcgt.org/published/0002/01/04/>`_ N. P. Rougier. Journal of Computer Graphics Techniques, 2.1 (2013)

* `Vispy, a future tool for interactive visualization <https://github.com/vispy/static/raw/master/vispy-biforum-2013.pdf>`_ - Talk at Budapest BI forum 2013

* `Vispy, a modern and interactive visualization framework <https://github.com/vispy/static/raw/master/vispy-euroscipy-2013.pdf>`_ - Talk at EuroScipy 2013

