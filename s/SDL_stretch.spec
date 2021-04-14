%undefine _debugsource_packages

Name:    SDL_stretch
Version: 0.3.1
Release: 1
Summary: SDL_stretch - Stretch Functions For The Simple DirectMedia Layer
License: LGPL
Group:   Development/Libraries/C and C++
URL:           http://sdl-stretch.sf.net
Source0:       %{name}-%{version}.tar.bz2
BuildRequires: SDL-devel
BuildRequires: xmlto

%description
Providing stretch and blit routines for SDL surfaces.
These are optimized for speed including lots of assembler parts
in the general routines and dynamic cpu native code generation
for applications to compile specialized stretch-and-blit routines
at runtime.

%package devel
Summary:  Stretch Functions For SDL - Headers and Manpages
Group:    Development/Libraries/C and C++
Requires: %name = %version

%description devel
While hacking on UAE (the unix amiga emulator) I did develop a few
stretching routines. I have been asking on the SDL mailing list for any
prior art but it seems that no one did wrap such routines into a
library part that can be reused everywhere. Other projects are
just game SDKs which tend to wrap such routines it into their
own framework - instead of using vanilla SDL surface. Also, there
are only rare pieces of assembler optimized routines. I took some
of these as hints and created my own set of highly optimized routines
pumped up with assembler - stretch-and-blit routines for SDL on steroids.

%prep
%setup -q
cp -f /usr/share/automake-*/config.guess use/

%build
export PYTHON=/usr/bin/python2
CFLAGS="$RPM_OPT_CFLAGS" ./configure --prefix=%_prefix --libdir=%_libdir
make
make docs

%install
rm -rf %buildroot
mkdir %buildroot
make install DESTDIR=%buildroot
make install-docs DESTDIR=%buildroot
cd %buildroot%_libdir/%name; for i in *.so*; do mv $i ..; ln -s ../$i .; done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%_libdir/*.so.*

%files devel
%_datadir/doc/*
%_libdir/*.so
%_libdir/*.a
%_libdir/*.la
%_libdir/pkgconfig/*
%_includedir/*
%_datadir/man/man3/*
%_libdir/%name

%changelog
* Wed Nov 28 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.1
- Rebuilt for Fedora
* Sun Feb 22 2009 Guido Draheim <guidod-2003-@gmx.de> 1.02
+ fixing stuff for opensuse policies - e.g. introducing secondary library
  to defeat the "shlib-policy-name-error (Badness: 10000)" failure; and
  introducing post/postun with the usual ldconfig call for library install.
* Sat Feb 21 2009 Guido Draheim <guidod-2003-@gmx.de> 1.01
+ rename BuildRequires to opensuse 11.0 "SDL" for buildserver usage
