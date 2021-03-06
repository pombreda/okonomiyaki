.. _api:

===
API
===

.. module:: okonomiyaki

Only the below API should be considered public.

Platform-related features
=========================

EPDPlatform class
-----------------

.. currentmodule:: okonomiyaki.platforms

The main API is EPDPlatform. You can either create an explicit platform,
or try to guess the platform from the running system::

    platform = EPDPlatform.from_epd_string("rh5-32")
    platform = EPDPlatform.from_running_system()

One can access details through EPDPlatform instances' attributes.

.. autoclass:: EPDPlatform
   :members:

Enthought egg features
======================

.. currentmodule:: okonomiyaki.file_formats.egg

LegacySpecDepend class
----------------------

Represents the content of the spec/depend file in Enthought egg's metadata.
You can create one from an existing egg::

    spec = LegacySpecDepend.from_egg("numpy-1.7.1-1.egg")
    print spec.packages
    print spec.osdist

    # generate the spec/depend content
    print spec.to_string()

.. autoclass:: LegacySpec
   :members:

LegacySpec class
----------------

This models the content of the spec directory in Enthought egg's metadata.
You can create one from an existing egg::

    spec = LegacySpec.from_egg("numpy-1.7.1-1.egg")
    print spec.summary
    print spec.lib_depend
    print spec.lib_provide

    # generate the spec/depend content
    print spec.depend_content()

.. autoclass:: LegacySpec
   :members:

EggBuilder class
----------------

This is a class to build simple eggs from an existing LegacySpec (e.g. to
build debug eggs).

.. autoclass:: EggBuilder
    :members:

Repositories format
===================

.. currentmodule:: okonomiyaki.repositories

Classes in this module model our different index entries.

GritsEggEntry can be used to automatically create the grits key, tags and
metadata from an egg package.

.. autoclass:: GritsEggEntry
    :members:
