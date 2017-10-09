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

**Before installing VisPy** you should ensure a working version of python is
installed on your computer, including all of the requirements included in the
**Backend Requirements** section above. A simple way to install most of these
requirements is to install the **Anaconda** scientific python distribution
from Continuum Analytics.
`Anaconda <https://www.anaconda.com/download/>`_ will
install most of the VisPy dependencies for you. If your computer is low on hard
disk space, or you would like a minimal python installation, you may install
the `Miniconda <https://conda.io/miniconda.html>`_ package also from
Continuum Analytics. Once Anaconda is installed, create a
`conda python environment <https://conda.io/docs/user-guide/tasks/manage-python.html>`_.

Next, install the following VisPy dependencies directly through `pip` or the Anaconda package installer.

.. code-block:: console

    $ conda install numpy pyqt

Once the python dependencies have been installed, install the latest
proprietary drivers for your computer's GPU. Generally these drivers may be
downloaded from the GPU manufacturer's website.

**To install the latest release version**, you can do:

.. code-block:: console

   $ pip install --upgrade vispy

**If you want to run the latest development version**, you can clone the
repository to your local machine and install with ``develop`` to enable easy
updates to latest ``master``:

.. code-block:: console

   $ git clone git://github.com/vispy/vispy.git  # creates "vispy" folder
   $ cd vispy
   $ python setup.py develop

To run the latest development version without cloning the repository, you
can also use this line:

.. code-block:: console

   $ pip install git+https://github.com/vispy/vispy.git


Testing installation
--------------------

It is strongly advised to run the vispy test suite right after installation to
check if everything is ok. To do this, just type:

.. code-block:: python

   >>> import vispy
   >>> vispy.test()
   ...

Please note that the test suite may be unstable on some systems. Any potential instability in the test suite does not necessarily imply instability in the working state of the provided VisPy examples.
