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
use a Jupyter notebook (version 3+) with WebGL for some visualizations although
it is not fully functional at this time.

.. warning::

   You only need to have one of these packages, no need to install them all!


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


Installation options
====================

**To install the latest release version**, you can do::

   $ pip install --upgrade vispy

**If you want to run the latest development version**, you can clone the
repository to your local machine and install with ``develop`` to enable easy
updates to latest``master``::

   $ git clone git://github.com/vispy/vispy.git  # creates "vispy" folder
   $ cd vispy
   $ python setup.py develop

To run the latest development version without cloning the repository, you
can also use this line::

   $ pip install -e git+https://github.com/vispy/vispy#egg=vispy-dev


Testing installation
--------------------

It is strongly advised to run the vispy test suite right after installation to
check if everything is ok. To do this, just type::

   >>> import vispy
   >>> vispy.test()
   ...
