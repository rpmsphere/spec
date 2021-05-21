%undefine _debugsource_packages

Name:           eaglemode
URL:            http://eaglemode.sourceforge.net/
Summary:        The most advanced Zoomable User Interface
License:        GPL-3.0+
Group:          Development/Tools/Other
Version:        0.95.0
Release:        1
Source:         http://dl.sourceforge.net/project/%{name}/%{name}-%{version}/%{name}-%{version}.tar.bz2
Source1:        %{name}.desktop
Source2:        %{name}_16x16.png
Source3:        %{name}_24x24.png
Source4:        %{name}_32x32.png
Source5:        %{name}_48x48.png
BuildRequires:  gcc-c++
BuildRequires:  gtk2-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  perl-interpreter
BuildRequires:  libX11-devel
BuildRequires:  librsvg2-devel
BuildRequires:  xine-lib-devel
BuildRequires:  poppler-glib-devel
BuildRequires:  vlc-devel

%description
Eagle Mode is an advanced solution for a futuristic style of man-machine
communication in which the user can visit almost everything simply by
zooming in. It has a professional file manager, file viewers and players
for most of the common file types, a chess game, a 3D mines game, a netwalk
game, a multi-function clock and some fractal fun, all integrated in a
virtual cosmos. Besides, that cosmos also provides a Linux kernel
configurator in form of a kernel patch.

By featuring a separate popup-zoomed control view, help texts in the things
they are describing, editable bookmarks, multiple input methods, fast
anti-aliased graphics, a virtually unlimited depth of panel tree, and by its
portable C++ API, Eagle Mode aims to be a cutting edge of zoomable user interfaces. 

Authors:
--------
        Oliver Hamann olha@users.sourceforge.net

%prep
%setup -q

%build
export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$CFLAGS"
perl make.pl build

%install
rm -rf $RPM_BUILD_ROOT
perl make.pl install dir=$RPM_BUILD_ROOT/%{_libdir}/eaglemode
cd $RPM_BUILD_ROOT/%{_libdir}/eaglemode
mkdir -p  ../../../%{_docdir}/eaglemode
cp -r doc ../../../%{_docdir}/eaglemode
#mv -T doc ../../share/doc/packages/eaglemode
#ln -s ../../share/doc/packages/eaglemode doc
mkdir -p ../../share/eaglemode
cp -r res ../../share/eaglemode
#mv -T res ../../share/eaglemode
#ln -s ../../share/eaglemode res
mkdir -p $RPM_BUILD_ROOT/etc/eaglemode
cp -r etc/* $RPM_BUILD_ROOT/etc/eaglemode
#mv -T etc $RPM_BUILD_ROOT/etc/eaglemode
#ln -s $RPM_BUILD_ROOT/etc/eaglemode etc

mkdir -p $RPM_BUILD_ROOT/usr/bin
cd $RPM_BUILD_ROOT/usr/bin
ln -s ../../%{_libdir}/eaglemode/eaglemode.sh eaglemode

chmod +x $RPM_BUILD_ROOT/%{_libdir}/eaglemode/lib/*.so
cd $RPM_BUILD_ROOT/%{_libdir}
ln -s eaglemode/lib/*.so .

mkdir -p $RPM_BUILD_ROOT/usr/include
cd $RPM_BUILD_ROOT/usr/include
ln -s ../../%{_libdir}/eaglemode/include/* .
mkdir -p $RPM_BUILD_ROOT/usr/share/icons/hicolor/16x16/apps
mkdir -p $RPM_BUILD_ROOT/usr/share/icons/hicolor/24x24/apps
mkdir -p $RPM_BUILD_ROOT/usr/share/icons/hicolor/32x32/apps
mkdir -p $RPM_BUILD_ROOT/usr/share/icons/hicolor/48x48/apps
mkdir -p $RPM_BUILD_ROOT/usr/share/applications
cp -avL %{S:2} $RPM_BUILD_ROOT/usr/share/icons/hicolor/16x16/apps/eaglemode.png
cp -avL %{S:3} $RPM_BUILD_ROOT/usr/share/icons/hicolor/24x24/apps/eaglemode.png
cp -avL %{S:4} $RPM_BUILD_ROOT/usr/share/icons/hicolor/32x32/apps/eaglemode.png
cp -avL %{S:5} $RPM_BUILD_ROOT/usr/share/icons/hicolor/48x48/apps/eaglemode.png
cp -avL %{S:1} $RPM_BUILD_ROOT/usr/share/applications/eaglemode.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/*
%{_docdir}/%{name}
%{_datadir}/%{name}
%{_libdir}/lib*.so
%{_libdir}/%{name}
%{_sysconfdir}/%{name}
%{_includedir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/%name.png

%changelog
* Mon Aug 24 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 0.95.0
- Rebuilt for Fedora
* Sat Jan  7 2012 joop.boonen@opensuse.org
- Reformated the spec file to meet the openSUSE standard
* Sun Nov 13 2011 joop.boonen@opensuse.org
- Build version 0.83.0
- Added missing buildreq
  libpoppler-glib-devel and gtk2-devel
* Mon Jul  4 2011 joop.boonen@opensuse.org
- Build version 0.82.0
* Thu May 12 2011 joop.boonen@opensuse.org
- Build version 0.81.0
* Wed Dec  8 2010 joop.boonen@opensuse.org
- Build version 0.80.0
* Tue Aug 24 2010 joop.boonen@opensuse.org
- Build version 0.79.0
* Sat Jul 24 2010 joop.boonen@opensuse.org
- etc files can now be found in /etc/eaglemode
  in stead of /etc/eaglemode/etc
- added export CFLAGS="$RPM_OPT_FLAGS"
- and export CXXFLAGS="$CFLAGS"
* Sat Jun 26 2010 joop.boonen@opensuse.org
- Build version 0.78.0
* Wed Feb 10 2010 joop.boonen@opensuse.org
- Build version 0.76.0
* Sun Jan 10 2010 joop.boonen@opensuse.org
- building with menu item
* Sat Jan  9 2010 joop.boonen@opensuse.org
- added all requirements according to te eagle mode webpage
* Sun Nov  8 2009 joop.boonen@opensuse.org
- Build version 0.75.1
