FAQ
===

VisPy is a big project with a lot of features and sometimes a couple ways to
do things. It sits on top of the very complex OpenGL library. We've tried to
document what we could in an organized and easy to find manner, but some
topics don't quite fit. This set of Frequently Asked Questions is where you'll
find the answer to some of these miscellaneous questions.

Why is my visualization slower when I add more Visual objects?
--------------------------------------------------------------

Each Visual object in VisPy is an OpenGL Program consisting of at least a
vertex shader and a fragment shader (see :doc:`getting_started/modern-gl`).
In general, except for some very specific cases, OpenGL Programs can only
be executed one at a time by a single OpenGL context. This means that in
your VisPy visualization each Visual object you tell VisPy to draw will
extend how long each update (draw) takes. When frames per second (FPS) or
responsiveness are a concern, this means each Visual you add reduces the
performance of your visualization.

While VisPy is constantly striving to improve performance, there are things
that you can do in the mean time (depending on your particular case). The
most important change that you can make is to lower the number of Visual
objects you have. For a lot of Visuals it is possible to combine them into
one by putting a little extra work into the data you provide them. For example,
instead of creating 10 separate LineVisuals, create 1 LineVisual that draws
10 lines. While this is a simple example, the same concept applies to other
types of Visuals in VisPy and more complex use cases. As a last resort for
the most complex cases, a custom Visual (custom shader code) may be necessary.
Before writing a custom Visual, check with VisPy maintainers by asking a
question on gitter or creating a question as a GitHub issue.

Is VisPy multi-threaded or thread-safe?
---------------------------------------

VisPy does not have any special multi-thread or multi-process handling except
for the funcionality provided by the GUI framework backends that it uses. For
example, PyQt5/PySide2 provide QThread objects for running code in another
thread. These libraries also provide ways of transferring data safely or
communicating between threads; mainly signals and slots. However, there is a
limit to what operations can be performed outside the main thread.

The main or GUI thread for most GUI frameworks is the **only** thread that can
perform drawing operations or operations that will trigger drawing. This
includes OpenGL functions. This means
that calling ``self.update()`` on a VisPy ``Canvas`` or ``Visual`` object must
ultimately be done in the main thread. Data that will be drawn can be created
or updated in a secondary thread, but the main/GUI thread must still be the
one to do the redraw. Since many Visual objects automatically call
``self.update()`` for property or data modifications this can be difficult to
do in the most performant way. Updates or requests for changes to better support
thread-safe data updates are welcome.

How to render headless/off-screen with VisPy?
---------------------------------------------

There are two strategies to render without windows with VisPy:

1. Use Xvfb that simulates an X server in memory without displaying windows.
   This can be used with any VisPy backend.
2. Use a backend that directly renders into memory buffers, e.g. OSMesa or EGL
   (`further info <https://stackoverflow.com/a/55758789>`_).

Then, in your VisPy script, use ::

    image = canvas.render()
    import imageio
    imageio.imwrite("rendered.png", image)

to save the rendered scene to an image file.

Xvfb
^^^^

Wrap the command to launch your script with ``xfvb-run``: ::

    xvfb-run -a python my_script.py

https://www.x.org/releases/X11R7.6/doc/man/man1/Xvfb.1.xhtml

OSMesa
^^^^^^

Using the OSMesa (Off-Screen Mesa) backend: ::

    import vispy
    vispy.use("osmesa")

VisPy tries to detect the OSMesa shared library, but, if needed, it can be set
explicitly with ::

    export OSMESA_LIBRARY=/usr/lib/libOSMesa.so

https://mesa-docs.readthedocs.io/en/latest/osmesa.html

EGL
^^^

Using the EGL backend: ::

    import vispy
    vispy.use("egl")

VisPy tries to detect the EGL shared library, but, if needed, it can be set
explicitly with ::

    # Choose one, or adapt to your system.
    export EGL_LIBRARY=/usr/lib/libEGL.so
    export EGL_LIBRARY=/usr/lib/libEGL_mesa.so
    export EGL_LIBRARY=/usr/lib/libEGL_nvidia.so

https://en.wikipedia.org/wiki/EGL_(API)

How to achieve transparency with 2D objects?
--------------------------------------------

It is possible to render 2D visuals, such as ``ImageVisual``, with translucency
(i.e. partial transparency, a see-through effect). To do that, you must:
1. Enable translucency for the visuals, if not the default for the visual:
   ``visual.set_gl_state('translucent')``.
2. Position the visuals at different depth levels (z-levels): ::

    visual1.transform = vispy.STTransform(translate=(0, 0, 1)
    visual2.transform = vispy.STTransform(translate=(0, 0, 2)

   Higher ``z`` means more at the back.

3. Draw the visuals from back to front. The order can be forced with: ::

    visual1.order = 2
    visual2.order = 1

   The object at the back (``visual2``) comes first in the drawing order.


How do I cite VisPy?
--------------------

See the VisPy repository for citation information:
https://github.com/vispy/vispy/blob/main/CITATION.rst