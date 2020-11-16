Getting Started - gloo
======================

The gloo layer of VisPy is the lowest level interface and is the closest thing
to OpenGL that VisPy provides. This also means it is the most complicated.
While OpenGL is complicated, gloo tries to provide a simple to use
object-oriented layer on top of that. The guide below will walk through the
basics of using VisPy's gloo interface to create a visualization.

.. include:: _canvas_app.rst

Basic Script
------------

To start any gloo visualization we will need to create a ``Canvas`` object and
an ``Application``. Here is the most basic working example we can create:

.. code-block:: python

    import sys
    from vispy import app, gloo

    canvas = app.Canvas(keys='interactive')


    @canvas.connect
    def on_draw(event):
        gloo.set_clear_color((0.2, 0.4, 0.6, 1.0))
        gloo.clear()


    canvas.show()

    if __name__ == '__main__' and sys.flags.interactive == 0:
        app.run()

If you run the above code you should see a single window with a solid
blue-ish background.

Let's go through this code one chunk at a time:

1. We start out by importing the the `sys` module from the Python standard
   library followed by the vispy :mod:`~vispy.app` and :mod:`~vispy.gloo`
   modules.
2. We create a ``Canvas`` object representing the overall space
   where our visualization will take place.
3. We define a simple "on_draw" function telling OpenGL to fill the
   Canvas with a specific RGBA (Red, Green, Blue, Alpha) color. The color
   components are defined as floating point numbers between 0 and 1.
   We use the ``canvas.connect`` decorator method to attach this method
   to any "draw" events coming from the canvas. When using this technique
   the function must be named ``on_<event>``. For more on the available
   events that can be connected to, see the
   :class:`vispy.app.canvas.Canvas` docstring.
4. We call :meth:`canvas.show() <vispy.app.canvas.Canvas.show>` to display
   the Canvas object on the screen. VisPy will talk to the underlying GUI
   backend (PyQt, Wx, etc) to construct a native GUI "widget" with our
   OpenGL visualization inside.
5. The script ends with us running a default VisPy
   :class:`~vispy.app.application.Application` object. Later on we'll see
   how we can define the exact Application we want to use, but in this early
   stage we won't need to. The if statement here is a common occurrence in
   VisPy example scripts so that the Application is only started when the
   code is run as a script (instead of imported). This also helps with more
   advanced usage where we run this script in an interactive Python
   interpreter.

.. note::

    The above code is also available in the ``examples/basics/gloo/start.py``
    script.

Basic Script (Alternative)
--------------------------

Another common way to structure a script like this is to subclass the
``Canvas`` class and override the necessary methods directly. This can be
useful if you want to keep all parts of your visualization contained in the
``Canvas`` object instead of throughout a script. Here is what the above
"connect style" script would look like as a subclass:

.. code-block:: python

    import sys
    from vispy import app, gloo

    class MyCanvas(app.Canvas):
        def on_draw(self, event):
            gloo.set_clear_color((0.2, 0.4, 0.6, 1.0))
            gloo.clear()


    canvas = MyCanvas(keys='interactive')
    canvas.show()

    if __name__ == '__main__' and sys.flags.interactive == 0:
        app.run()

Create an OpenGL Program
------------------------

As mentioned earlier, the ``gloo`` interface provides a low-level
object-oriented interface on top of OpenGL. If we want to do anything more
complicated that a solid color, we'll need to start using these OpenGL
objects. We'll start with the below code to draw a simple shape in our
Canvas. As mentioned in :doc:`index`, if you aren't familiar with OpenGL then
it is highly recommended that you read :doc:`modern-gl` before diving into
the below code.

.. code-block:: python

    from vispy import gloo
    from vispy import app
    import numpy as np

    # Create vertices
    vPosition = np.array([[-0.8, -0.8, 0.0], [+0.7, -0.7, 0.0],
                          [-0.7, +0.7, 0.0], [+0.8, +0.8, 0.0, ]], np.float32)


    VERT_SHADER = """ // simple vertex shader
    attribute vec3 a_position;
    void main (void) {
        gl_Position = vec4(a_position, 1.0);
    }
    """

    FRAG_SHADER = """ // simple fragment shader
    uniform vec4 u_color;
    void main()
    {
        gl_FragColor = u_color;
    }
    """


    class Canvas(app.Canvas):

        def __init__(self):
            app.Canvas.__init__(self, keys='interactive')

            # Create program
            self._program = gloo.Program(VERT_SHADER, FRAG_SHADER)

            # Set uniform and attribute
            self._program['u_color'] = 0.2, 1.0, 0.4, 1
            self._program['a_position'] = gloo.VertexBuffer(vPosition)

            gloo.set_clear_color('white')

            self.show()

        def on_resize(self, event):
            width, height = event.physical_size
            gloo.set_viewport(0, 0, width, height)

        def on_draw(self, event):
            gloo.clear()
            self._program.draw('triangle_strip')


    if __name__ == '__main__':
        c = Canvas()
        app.run()

Similar to the previous example, we've created a subclass of the ``Canvas``
object to hold on to all of the objects we create. We start by defining an
OpenGL :class:`~vispy.gloo.program.Program` which expects two shaders in the
simplest case: a vertex shader and a fragment shader.

Now that we have the Program, we are able to start setting uniforms and
attributes used by the shaders. In this example we've included the
``.show()`` call inside the ``__init__`` method so the Canvas is shown as soon
as it is created.

Lastly, we create two event handlers. One for the "resize" event so when the
user resizes the GUI window we can update the size of the OpenGL canvas
(viewport). The other handler is for "draw" where we clear the canvas,
setting it to the "clear color" of white, and then tell our GL Program to draw
or execute itself.

Future
------

More instructions coming soon...

