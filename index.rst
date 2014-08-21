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


Vispy is a **high-performance interactive 2D/3D data visualization library**. 
Vispy leverages the computational power of modern 
**Graphics Processing Units (GPUs)** through the **OpenGL** library to 
display very large datasets. Applications of Vispy include:

* High-quality interactive scientific plots with tens of millions of points.
* Direct visualization of real-time data.
* Fast interactive visualization of 3D models (meshes, volume rendering).
* OpenGL visualization demos.
* Scientific GUIs with fast, scalable visualization widgets (Qt or IPython notebook with WebGL).

We currently offer full support for building visualizations using OpenGL.
We also provide experimental support for high-level graphical interfaces
to create visualizations without any knowledge of OpenGL.


Announcements
-------------

- **Release!** Version 0.2.2, August 22, 2014
- **EuroSciPy 2014**: talk and sprint, August 2014
- `Article in **Linux Magazine**, French Edition <https://github.com/vispy/linuxmag-article>`__, July 2014
- **GSoC 2014**: `two GSoC students are currently working on Vispy under the PSF umbrella <https://github.com/vispy/vispy/wiki/Project.%20GSoC-2014>`__
- **Release!**, Version 0.2.1 04-11-2013
- **Presentation at BI forum**, Budapest, 6 November 2013
- **Presentation at Euroscipy**, Belgium, August 2013
- **EuroSciPy Sprint**, Belgium, August 2013
- **Release!** Version 0.1.0 14-08-2013


Installation
------------

Vispy runs on Python 2.6 - Python 3.4 and depends on Numpy.

As Vispy is under heavy development at this time, we highly recommend you to use
the `development version on Github <https://github.com/vispy/vispy>`__ (master branch).
You need to clone the repository and install Vispy with ``python setup.py install``.


About us
--------

The core development team consists of Luke Campagnola, Almar Klein,
Nicolas Rougier, Eric Larson, Cyrille Rossant. Four of us have written our own 
Python visualization toolkit (PyQtGraph, Visvis, Glumpy and Galry), and 
we decided to team-up to create a unique high-performance, high-quality 
interactive visualization library.

* `User mailing list <https://groups.google.com/forum/#!forum/vispy>`__
* `Dev mailing list <https://groups.google.com/forum/#!forum/vispy-dev>`__
* `Dev chat room <https://gitter.im/vispy/vispy>`__


Publications
------------

* `Hardware-accelerated interactive data visualization for neuroscience in Python <http://www.frontiersin.org/Journal/10.3389/fninf.2013.00036/full>`_ C. Rossant and K.D. Harris, Frontiers in Neuroinformatics, 7.36, (2013)

* `Shader-based Antialiased Dashed Stroked Polylines <http://jcgt.org/published/0002/02/08/>`_ N. P. Rougier. Journal of Computer Graphics Techniques, 2.2 (2013)

* `Higher Quality 2D Text Rendering <http://jcgt.org/published/0002/01/04/>`_ N. P. Rougier. Journal of Computer Graphics Techniques, 2.1 (2013)

* `Vispy, a future tool for interactive visualization <https://github.com/vispy/static/raw/master/vispy-biforum-2013.pdf>`_ - Talk at Budapest BI forum 2013

* `Vispy, a modern and interactive visualization framework <https://github.com/vispy/static/raw/master/vispy-euroscipy-2013.pdf>`_ - Talk at EuroScipy 2013

