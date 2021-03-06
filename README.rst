aio.testing
===========

Test utils for the aio_ asyncio framework

.. _aio: https://github.com/phlax/aio


Build status
------------

.. image:: https://travis-ci.org/phlax/aio.testing.svg?branch=master
	       :target: https://travis-ci.org/phlax/aio.testing


Installation
------------

Requires python >= 3.4

Install with:

.. code:: bash

	  pip install aio.testing


Aio testing provides 2 decorators for running asyncio tests

- *aio.testing.run_until_complete*:

  - creates a test loop
  - calls the test with loop.run_until_complete

- *aio.testing.run_forever*:
  
  - creates a test loop
  - calls test using loop.run_forever
  - waits for number of seconds specified in "timeout" (default = 1)
  - if test returns a callable, calls it as a coroutine
  - waits for number of seconds specified in "sleep" (default = 0)

	  

@aio.testing.run_until_complete
-------------------------------

aio.testing provides a method decorator for running asyncio-based tests

.. code:: python

	  import unittest
	  import asyncio

	  import aio.testing


	  class MyTestCase(unittest.TestCase):

	      @aio.testing.run_until_complete
	      def test_example():
	          yield from asyncio.sleep(2)
		  self.assertTrue(True)

		  
Prior to the test running asyncio.get_new_loop() is called and set using asyncio.set_event_loop().

On completion of the test asyncio.set_event_loop() is again called with the original event loop.


@aio.testing.run_forever
------------------------

If your code needs to test long-running tasks, you can use the @aio.testing.run_forever decorator.

The @aio.testing.run_forever decorator uses loop.run_forever to run the test.

Any setup required can be done in the body of the test function which can optionally return a test callback

The callback is wrapped in a coroutine, and called after 1 second

.. code:: python

	  import unittest
	  import asyncio

	  import aio.testing


	  class MyFutureTestCase(unittest.TestCase):

	      @aio.testing.run_forever
	      def test_example():
	          yield from asyncio.sleep(2)

		  def callback_test(self):
		      yield from asyncio.sleep(2)		  
		      self.assertTrue(True)

		  # this function is called 1 second after being returned		      
		  return callback_test


As with aio.testing.run_until_complete, the test is run in a separate loop.

		  
@aio.testing.run_forever with timeout
-------------------------------------

You can specify how many seconds to wait *before* running the callback tests by setting the timeout value


.. code:: python

	  import unittest
	  import asyncio

	  import aio.testing


	  class MyFutureTestCase(unittest.TestCase):

	      @aio.testing.run_forever(timeout=10)
	      def test_example():
	          yield from asyncio.sleep(2)

		  def callback_test(self):
		      yield from asyncio.sleep(2)		  
		      self.assertTrue(True)

		  # this function is called 10 seconds after being returned		      
		  return callback_test


@aio.testing.run_forever with sleep
-----------------------------------

Sometimes a test needs to wait for some time after services have been stopped and the test loop has been destroyed.

You can specify how many seconds to wait *after* running the callback tests by setting the sleep value


.. code:: python

	  import unittest
	  import asyncio

	  import aio.testing


	  class MyFutureTestCase(unittest.TestCase):

	      @aio.testing.run_forever(sleep=10)
	      def test_example():
	          yield from asyncio.sleep(2)

		  def callback_test(self):
		      yield from asyncio.sleep(2)		  
		      self.assertTrue(True)

		  return callback_test
		  

Supplying your own event loop
-----------------------------------

By default, aio.testing creates a new event loop for each test. There may be
times that you prefer to control which event loop the tests are executed on.
For example, you may create some expensive resource on a loop in a fixture
that you wish to share among tests.

Both aio.testing.run_until_complete and aio.testing.run_forever accept an
optional named argument called :code:`loop`. The value of :code:`loop` should
be a `context manager`_ that returns a loop. aio.testing provides the
:code:`current_loop` context manager which simply returns the value of
asyncio.get_event_loop():

.. _context manager: https://docs.python.org/3/reference/datamodel.html#context-managers

.. code:: python

	  import unittest
	  import asyncio

	  import aio.testing


	  class MyTestCase(unittest.TestCase):

              @classmethod
              def setUpClass(cls):
                  cls.loop = asyncio.get_event_loop()

	      @aio.testing.run_until_complete(loop=aio.testing.current_loop)
	      def test_example():
	          yield from asyncio.sleep(2)
		  self.assertEqual(asyncio.get_event_loop(), MyTestCase.loop)


Contributing
-----------------------------------

To run unit tests, use:

.. code:: bash

	  python setup.py test

To run doc tests, use:

.. code:: bash

	  python -m doctest aio/testing/README.rst

