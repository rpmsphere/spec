Name:           h5utils
Version:        1.13.2
Release:        1
Summary:        Utilities for Data Conversions from hdf5
License:        GPL-2.0-or-later AND MIT
Group:          Productivity/Scientific/Electronics
URL:            https://github.com/stevengj/h5utils
Source0:        https://github.com/stevengj/h5utils/releases/download/%{version}/h5utils-%{version}.tar.gz
BuildRequires:  hdf5-devel
BuildRequires:  libjpeg-devel
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(zlib)
#Requires:       meep

%description
h5utils is a set of utilities for visualization and conversion of
scientific data in the HDF5 format.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc AUTHORS ChangeLog
%{_bindir}/h5*
%{_mandir}/man1/h5*.1*
%{_datadir}/h5utils

%changelog
* Sun Jan 15 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 1.13.2
- Rebuilt for Fedora
* Wed Dec  5 2018 Todd R <toddrme2178@gmail.com>
- Update to version 1.13.1
  * Fixed man page problems
  * Fixed h5topng compilation for modern libpng versions. Thanks to Daisuke Fujimura (@fd00 on github) for posting patches.
  * Moved hosting to Github and translated documentation to Markdown.
- Remove unneeded h5utils-png14.patch
* Mon Mar 25 2013 joop.boonen@opensuse.org
- Cleaned the spec file up
- Added a png14 patch
* Sun May 29 2011 werner.ho@gmx.de
- fixed hdf5-devel package name change
* Sun Sep 19 2010 werner.ho@gmx.de
- fixed libhdf5 dependancy
* Sat Oct 10 2009 werner.ho@gmx.de
- new version 1.12.1
* Sun Nov 23 2008 werner.ho@gmx.de
- build fixes for factory
* Sun Jul 20 2008 werner.ho@gmx.de
- new version 1.11.1
* Sun Oct 21 2007 werner.ho@gmx.de
- Initial build of version 1.10.1
