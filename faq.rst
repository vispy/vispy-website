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

How do I cite VisPy?
--------------------

See the VisPy repository for citation information:
https://github.com/vispy/vispy/blob/main/CITATION.rst