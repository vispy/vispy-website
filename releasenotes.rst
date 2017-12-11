=============
Release notes
=============

**Vispy 0.5.2**

  * Fix PyPI packaging to include LICENSE.txt
  * Fix initial axis limits in PlotWidget (#1386)
  * Fix zoom event position in Pyglet backend (#1388)
  * Fix camera importing (#1389, #1172)
  * Refactor `EllipseVisual` and `RectangleVisual` (#1387, #1349)
  * Fix `one_scene_four_cams.py` example (#1391, #1124)
  * Add `two_qt_widgets.py` example (#1392, #1298)
  * Fix order of alignment values for proper processing (#1395, #641)

**Vispy 0.5.1**

  * Fix 'doc' directory being installed with source tarball
  * Fix 'ArrowVisual' when used with a Scene camera and in 3D space
  * Fix 'SphereVisual' rows/cols order in 'latitude' method
  * Fix DPI calculation on linux when xrandr returns 0mm screen dimension

**Vispy 0.5**

  * Major refactor of all cameras and visuals
  * Add support for wxPython 4.0+ (project phoenix)
  * Improve Jupyter Notebook support (not full support)
  * Improve Python 3 support
  * Add colormaps
  * Add various new visuals `GridMesh`, `BoxVisual`, `PlaneVisual`, etc.
  * Various bug fixes and performance improvements (177+ pull requests)
  * Remove experimental matplotlib backend (`mpl_plot`)
  * Drop Python 2.6 support

**Vispy 0.4**

There have been many changes, which include:

  * minor tweaks and bugfixes to gloo
  * experimental support for "collections" (batched GL draw calls)
  * many new Visuals (Volume, Isocurve, etc.)
  * improvements and extensions of the SceneGraph system
  * proper HiDPI support
  * an experimental native high-level plotting interface vispy.plot


**Vispy 0.3**

Many changes:

  * Added multiple new application backends, including a IPython browser
    backend.
  * Experimental support for high-level visualizations through
    '`vispy.scene`` and ``vispy.scene.visuals``.
  * Experimental support for matplotlib plotting through ``vispy.mpl_plot``.
  * Loads of bugfixes.


**Vispy 0.2.1**

Small fix in the setup script. The buf prevented pip from working.


**Vispy 0.2**

In this release we focussed on improving and finalizing the object
oriented OpenGL interface ``vispy.gloo``. Some major (backward
incompatible) changes were done. However, from this release we consider
the ``vispy.gloo`` package relatively stable and we try to minimize
backward incompatibilities.

Changes in more detail:

  * ``vispy.oogl`` is renamed to ``vispy.gloo``
  * ``vispy.gl`` is moved to ``vispy.gloo.gl`` since most users will
    use gloo to interface with OpenGL.
  * Improved (and thus changed) several parts of the gloo API.
  * Some parts of gloo were refactored and should be more robust.
  * Much better coverage of the test suite.
  * Compatibility with Python 2.6 (Jerome Kieffer)
  * More examples and a gallery on the website to show them off. 


**Vispy 0.1.0**

First release. We have an initial version of the object oriented interface
to OpenGL, called `vispy.oogl`.
