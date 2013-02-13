Project Release Cycle
====================

It's common to use a two-week release cycle for projects. All the development
work that is approved and ready will be pushed live every two weeks on the same day.


Branches
--------

"dev" is the branch with everything that is currently available for the next
release.

"master" is the branch with everything that should be live as of now.


Hot-fixes
---------

In between your project's main release cycle, features and bugs may be addressed as
"hot-fixes". These are intended to be needs that are of a high
priority. These fixes should *not* be merged to the "dev" branch, first.
However, they should be approved to be merged to "master". When the hot-fix is
merged to "master", it should immediately be tagged, pushed to live and merged
back to dev by the person pushing to live.


Tagging
-------

Each release will be tagged in our main Git repo for historical reference. If
we have a critical problem with one release, then we will be able to push the
HEAD of our last functioning tag to restore live until the problem is fixed.

The syntax for tagging is as follows::

    { major version }.{ two-digit year }.{ non-zero month }.{ month release number }

For example, the first release occurrence had the following tag::

    1.13.1.1

Presumably, the next release occurrence on January 16th, 2013 should have::

    1.13.1.2

Hot-fixes are given an extra minor number for tagging::

    { major version }.{ two-digit year }.{ non-zero month }.{ month release number }.{ hot-fix release number }

If we had a hot-fix after our first release occurrence and before the second
release occurrence, the tag should be::

    1.13.1.1.1

