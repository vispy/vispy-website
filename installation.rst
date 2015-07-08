============
Installation
============


Package requirements
====================

The only mandatory requirement for VisPy is the `numpy <http://numpy.org>`_
package.


Backend requirements
====================

VisPy requires at least one toolkit for opening a window and creates an OpenGL
context. This can be done using one Qt, GLFW,SDL2, Wx, or Pyglet. You can also
use an IPython notebook (version 3+) with WebGL for some visualizations.

.. warning::

   You only need to have one of these packages, no need to install them all !


Hardware requirements
=====================

VisPy makes heavy use of the graphic card installed on your system. More
precisely, VisPy uses the Graphical Processing Unit (GPU) through
shaders. VisPy thus requires a fairly recent video card (~ less than 12 years
old) as well as an up-to-date video driver such that vispy can access the
programmable pipeline (as opposed to the fixed pipeline).

To get information on your system, you can type:

.. code-block:: python

   >>> print(vispy.sys_info())

The results of the above command and is long list of information related to
your system and video driver. The OpenGL version must be at least 2.1.


Installation
============

Once requirements are met, you can proceed with VisPy installation::

   $ pip install vispy

or upgrade any existing installation::

   $ pip install --upgrade vispy


Testing installation
--------------------

It is strongly advised to run the vispy test suite right after installation to
check if everything is ok. To do this, just type::

   >>> import vispy
   >>> vispy.test()
   ...
