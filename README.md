
# YaST - Old Travis Backup

![Obsolete badge](https://img.shields.io/badge/status-obsolete-red.svg)

:skull: The old YaST Travis packages are buried here, RIP! :skull:

## Description

This repository contains a backup of the old Travis packages used by YaST.
Originally we built YaST DEB packages to use them at Travis which is running
an Ubuntu distribution by default.

But this was not reliable and required extra effort to keep the packages
building and working at Travis. Later we switched to Docker and use the native
openSUSE build environment in a Docker container and these packages become
obsolete.

## License

The YaST Debian packaging files have the usual GNU GPLv2 license. However the
other non-YaST packages might have a different license.

## Warnings

- :warning: We do not provide any support for these packages, use at your risk!
- :warning: The repository is provided just for your reference, the YaST
  packages actually have never fully worked in Ubuntu. We used the packages just
  for running the unit tests where we mocked (simulated) the system access with
  successful result.
- :warning: Due to backup of the source tarballs the Git repository size is
  *huge* (~260MB)! Do not clone the repository unless you really need it!
- :warning: The repository contains a snapshot taken at some point of time, the
  packages are not updated anymore.
- The packaging took us quite some time so it might be still useful for someone
  who wants to play with YaST in Debian or Ubuntu, this might be a good
  entry point.
