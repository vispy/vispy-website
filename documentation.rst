Documentation
=============

VisPy is a **high-performance interactive 2D/3D data visualization
library** leveraging the computational power of modern **Graphics
Processing Units (GPUs)** through the **OpenGL** library to display very
large datasets.


Getting started
---------------

VisPy is under heavy development at this time, and we are still working on a
complete user guide for Vispy. VisPy targets two primary categories of users:

1. **Users knowing OpenGL**, or willing to learn OpenGL, who want to
   create beautiful and fast interactive 2D/3D visualizations in Python
   as easily as possible. Users in this category can write their own
   visualizations with :mod:`vispy.gloo` (requires knowing OpenGL/GLSL)

2. **Scientists without any knowledge of OpenGL**, who are seeking a
   high-level, high-performance plotting toolkit. Use the :mod:`vispy.plot`
   and :mod:`vispy.scene` interfaces for high-level work
   (**WARNING**: experimental / developing code).

Please check out the :doc:`gallery` for inspiration.


Installation instructions
-------------------------

.. toctree::
   :maxdepth: 2

   installation
   raspberry


API Reference
-------------

.. toctree::
   :maxdepth: 2
   
   vispy - Top-level tools <vispy>
   vispy.app - Application, event loops, canvas, backends <app>
   vispy.color - Handling colors <color>
   vispy.geometry - Visualization-related geometry routines <geometry>
   vispy.gloo - User-friendly, Pythonic, object-oriented interface to OpenGL <gloo>
   vispy.io - Data IO <io>
   vispy.plot - Vispy native plotting module [experimental] <plot>
   vispy.scene - The system underlying the upcoming high-level visualization interfaces [experimental] <scene>
   vispy.visuals - The visuals that are used for high-level plotting <visuals>
   vispy.util - Miscellaneous utilities <util>
   releasenotes


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
