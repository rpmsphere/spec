%undefine _debugsource_packages

Name:               fireflies
Version:            2.07
Release:            24.1
Summary:            Slick OpenGL Screensaver
# https://somewhere.fscked.org/proj/fireflies/files/fireflies-%{version}.tar.gz
Source:             fireflies-%{version}.tar.bz2
Patch1:             fireflies-gcc4.patch
Patch2:             fireflies-makefile.patch
URL:                https://somewhere.fscked.org/proj/fireflies/
Group:              Amusements/Toys/Screensavers
License:            GPLv2+
BuildRequires:	    libpng-devel
BuildRequires:	    libpng12-devel
BuildRequires:      mesa-libGL-devel mesa-libGLU-devel
BuildRequires:      libX11-devel
BuildRequires:      libjpeg-devel
BuildRequires:      libtiff-devel
BuildRequires:      fltk-devel
BuildRequires:      gcc-c++ libstdc++-devel
BuildRequires:      gcc make glibc-devel
BuildRequires:      autoconf automake libtool pkgconfig
Requires:           xscreensaver

%description
Slick screensaver that uses OpenGL.

%prep
%setup -q
%__tar xzf libgfx-*.tar.gz
%patch1
%patch2
sed -i -e 's/png/png12/' -e 's/-lGLU/-lGLU -lX11 -lpng12/' configure* */configure*
sed -i 's|FL/fl_file_chooser.H|FL/Fl_File_Chooser.H|' libgfx/src/gui.cxx

%build
./configure --prefix=/usr \
    --with-bindir="%{_libdir}/xscreensaver" \
    --with-confdir="/etc/xscreensaver"

cd libgfx
./configure
cd src
make

%install
%__rm -rf "$RPM_BUILD_ROOT"
make DESTDIR=$RPM_BUILD_ROOT install

%clean
%__rm -rf "$RPM_BUILD_ROOT"

%files
%doc COPYING ChangeLog README
%config(noreplace) /etc/xscreensaver/fireflies.xml
%{_libdir}/xscreensaver/fireflies

%changelog
* Tue Oct 25 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 2.07
- Rebuilt for Fedora
* Thu Jun 24 2010 pascal.bleser@opensuse.org
- initial package (2.07)
