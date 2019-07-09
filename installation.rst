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
context. This can be done using one Qt, GLFW, SDL2, Wx, or Pyglet. You can also
use a Jupyter notebook with WebGL for some visualizations although some visuals
may not be possible (ex. volume rendering).

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

.. note::

    On linux systems the `xrandr` command is used to determine the screen's
    DPI. On certain (virtual) displays it reports screen dimensions of
    0mm x 0mm. In this case users may attempt to fix their screen resolution
    or download the `xdpyinfo` (xorg-xdpyinfo) utility as an alternative to
    `xrandr`. A default DPI of 96 is used otherwise.

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

Via conda
---------

VisPy can be installed in a conda environment by using the package available
from the `conda-forge <https://conda-forge.org/>`_ channel:

.. code-block:: console

    conda install -c conda-forge vispy

Via PyPI
--------

VisPy can also be installed with ``pip`` to install it from PyPI:

.. code-block:: console

    pip install --upgrade vispy

Once the python dependencies have been installed, install the latest
proprietary drivers for your computer's GPU. Generally these drivers may be
downloaded from the GPU manufacturer's website.

Via GitHub
----------

**If you want to run the latest development version**, you can clone the
repository to your local machine and install vispy in "development" mode.
This means that any changes to the cloned repository will be immediately
available in the python environment:

.. code-block:: console

    # creates "vispy" folder
    git clone --recurse-submodules git://github.com/vispy/vispy.git
    cd vispy
    # create/initialize 'doc' and 'js' directories
    git submodule update --init --recursive
    pip install -e . --no-use-pep517

If you have cloned the repository in the past you may need to run the
submodule command above to initialize any git submodules.
To run the latest development version without cloning the repository, you
can also use this line:

.. code-block:: console

    pip install git+https://github.com/vispy/vispy.git

Jupyter Notebook Extension
--------------------------

If you would like to use the VisPy Jupyter Notebook Widget you must first
install the ``ipywidgets`` library and enable the extension by doing:

.. code-block:: console

    pip install ipywidgets
    jupyter nbextension enable --py widgetsnbextension
    jupyter nbextension enable --py vispy

When using `virtualenv <https://virtualenv.pypa.io/en/stable/>`_ and working in
an activated virtual environment, the ``--sys-prefix`` option may be required
to enable the extension and keep the environment isolated (i.e.
``jupyter nbextension enable --py widgetsnbextension --sys-prefix``).

Note if you have an old version of the extension installed you mean need to
manually delete it from `<python-prefix>/share/nbextensions/vispy`>

If you are installing vispy from source in a "development mode" you may need
to explicitly install the extension before enabling it (using the symlink
option to link the extension to your active development environment):

.. code-block:: console

    jupyter nbextension install --symlink --py vispy --sys-prefix

.. note::

    The Jupyter-based backend and extension should be considered experimental
    due to performance limitations; both by the WebGL standard and what is
    currently implemented in vispy. Users should strongly consider these
    limitations before using vispy for an operational WebGL application.

JupyterLab
----------

To install the JupyterLab extension you need to install it explicitly with the
following:

.. code-block:: console

    conda install -c conda-forge nodejs  # or some other way to have a recent node
    jupyter labextension install @jupyter-widgets/jupyterlab-manager
    jupyter labextension install vispy

If you have a "vispy" directory in your current directory this will try to
install from there, use `vispy@latest` instead.

Testing installation
--------------------

It is strongly advised to run the vispy test suite right after installation to
check if everything is ok. To do this, just type:

.. code-block:: python

   >>> import vispy
   >>> vispy.test()
   ...

Please note that the test suite may be unstable on some systems. Any potential
instability in the test suite does not necessarily imply instability in the
working state of the provided VisPy examples.

Usage in an interactive console
===============================

If running from a jupyter console, either the ``jupyter-qtconsole``, the
``jupyter-console``, or, the console within
`Spyder <https://pythonhosted.org/spyder/>`_, you may need to ensure a few
other
`IPython magic <https://ipython.org/ipython-doc/3/interactive/tutorial.html#magic-functions>`_
functions are called prior to using vispy in a given kernel. Before using any
VisPy code, we recommend running the following commands when starting your
python kernel:

.. code-block:: python

     >>> %gui qt
     >>> # your vispy code

Namely, this has the effect of sharing the event loop between application and the interactive
console allowing you use both simultaneously.

Switchable graphics
===================

If your laptop comes with switchable graphics you have to make sure to tell
python to use your graphics card instead of the integrated Intel graphics.
You can identify which graphics card will be used by running:

.. code-block:: python

   >>> import vispy
   >>> print(vispy.sys_info())

and look for Nvidia in the ``GL version``. For example:
``GL version:  '4.6.0 NVIDIA 390.25'``.


Windows
-------

In Windows, you should open the the Nvidia-console and add your specific
python to the list of programs that should use the dedicated graphics card.
Note that this setting is seperate for different conda environments so make
sure you have selected the one you are using VisPy with.

Linux
-----

On Linux with the proprietary Nvidia graphics drivers, you should run python
with ``primusrun python your_script.py``.

For use with a Jupyter kernel, say in Spyder or the ``jupyter-qtconsole``,
make sure the kernel is started with ``primusrun``. For example:

.. code-block:: bash

    $ primusrun spyder3

.. code-block:: bash

    $ primusrun jupyter-qtconsole


Modifyin default jupyter kernel
-------------------------------

If you want the jupyter-qtconsole to always use your Nvidia graphics card,
you can change the parameters in the default kernel. To find the default
kernel, run

.. code-block:: bash

   $ jupyter kernelspec list

then edit the ``kernel.json`` file to include ``"primusrun",`` as the first
parameter in ``argv``. For example:

.. code-block:: json

   {
     "argv": [
       "primusrun",
       "python",
       "-m",
       "ipykernel_launcher",
       "-f",
       "{connection_file}"
     ],
     "language": "python",
     "display_name": "Python 3"
   }

Using a similar configuration, you could have two kernels configurations, one
for the dedicated graphics card, and one for the integrated graphics.

Spyder has it's own configuration and I don't know exactly how to make its
console run with ``primusrun`` without running ``primusrun spyder3``.
