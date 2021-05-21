%global debug_package %{nil}

Name:           slop
Version:        7.3.49
Release:        8.1
Summary:        Query for a selection from the user and print the region to stdout
License:        GPL-3.0+
Group:          Productivity/Graphics/Other
URL:            https://github.com/naelstrof/slop
Source0:        https://github.com/naelstrof/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  glm-devel
BuildRequires:  glew-devel
BuildRequires:  libicu-devel
BuildRequires:  libXrender-devel
BuildRequires:  mesa-libEGL-devel
BuildRequires:  imlib2-devel

%description
slop (Select Operation) queries for a selection from the user and prints
the region to stdout. It grabs the mouse and turns it into a crosshair,
lets the user click and drag to make a selection (or click on a window)
while drawing a pretty box around it, then finally prints the selection's
dimensions to stdout.

%prep
%setup -q

%build
%cmake
%make_build

%install
%make_install
#install -Dm755 bin/%{name} %{buildroot}%{_bindir}/%{name}
#install -Dm644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
%ifarch x86_64 aarch64
mv %{buildroot}/usr/lib %{buildroot}/usr/lib64
%endif

%files
%doc COPYING README.md license.txt
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_includedir}/*
%{_libdir}/lib*

%changelog
* Tue Sep 12 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 7.3.49
- Rebuilt for Fedora
* Thu Sep  3 2015 nemysis@openSUSE.org
- Update to 4.2.19, announce message is here:
    https://github.com/naelstrof/slop/releases/tag/v4.2.19
* Sun Jul 12 2015 nemysis@gmx.ch
- Update to 4.2.18, announce message is here:
    https://github.com/naelstrof/slop/releases
* Sun Jul 12 2015 nemysis@gmx.ch
- Update to 4.2.17, announce message is here:
    https://github.com/naelstrof/slop/releases/tag/v4.2.17
- Remove BuildRequires for pkgconfig(xext)
- Add BuildRequires for glm-devel, pkgconfig(gl), pkgconfig(glew),
  pkgconfig(glu), pkgconfig(imlib2) and pkgconfig(xrandr)
* Sat Jun 27 2015 nemysis@gmx.ch
- Remove v3.1.5.tar.gz, forgotten in previous commit
* Fri Jun 26 2015 nemysis@gmx.ch
- Update to 4.1.16, announce message:
  Added opacity capabilities. --color now checks for an alpha value,
  but it's optional.
  Added new option --highlight. Which instead of drawing a border around
  the selection, it draws over the selection. Best used with --color
  with an alpha set below 1.
  Added option --minimumsize and --maximumsize, setting them both to
  the same value disables drag selections.
  Slop windows now let all events fall through.
  Incredibly improved rendering quality and speed, no longer do I
  re-size or move windows around. For some reason that's really
    expensive in X11...
  Slop now outputs the ID of a selected window if any.
  Minor bugfixes and adjustments.
- Change Source0 Web URL, to have right slop-4.1.16.tar.gz
- Add BuildRequires for cmake and gengetopt
- Add BuildRoot
- Use %%{name} instead of maim
- Add Documentation
- Add %%changelog
* Mon Oct 20 2014 rneuhauser@suse.cz
- slop-3.1.5
* Fri Oct 17 2014 rneuhauser@suse.cz
- slop-3.1.4
