%global _default_patch_fuzz 2

Summary:	A low-level event loop management library
Name:		liboop
Version:	1.0.1
Release:	1
License:	LGPL
Group:		System/Libraries
URL:		http://www.lysator.liu.se/liboop/
Source0:	%{name}-%{version}.tar.gz
Patch0:		liboop-linkage_fix.diff
# Add 8.5 and 8.6 to tcl versions configure script detects - AdamW 2008/12
Patch1:		liboop-1.0-tcl86.patch
BuildRequires:	libtool
BuildRequires:	automake
BuildRequires:	tcl-devel

%description
Liboop is a low-level event loop management library for POSIX-based 
operating systems. It supports the development of modular,
multiplexed applications which may respond to events from several
sources. It replaces the "select() loop" and allows the
registration of event handlers for file and network I/O, timers and
signals. Since processes use these mechanisms for almost all
external communication, liboop can be used as the basis for almost
any application.

%package devel
Summary:	Static library and header files for the %{name} library
Group:		Development/C
Requires:	%{name} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description devel
Liboop is a low-level event loop management library for POSIX-based 
operating systems. It supports the development of modular,
multiplexed applications which may respond to events from several
sources. It replaces the "select() loop" and allows the
registration of event handlers for file and network I/O, timers and
signals. Since processes use these mechanisms for almost all
external communication, liboop can be used as the basis for almost
any application.

%prep
%setup -q
%patch0 -p0
%patch1 -p1 -b .tcl86

%build
# this bit is done with automake for good reason. If you use newer
# versions, it will run fine, but the final built libraries will have
# no .so extension. Quite bizarre. - AdamW 2008/12
export WANT_AUTOCONF_2_5=1
libtoolize --copy --force; aclocal; autoconf; automake --add-missing
export CFLAGS="%{optflags} -fPIC"
%configure --disable-static --without-glib --without-tcl --without-readline
make

%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%files
%{_libdir}/*.so.*

%files devel
%{_includedir}/*.h
%{_libdir}/*.so
#{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/pkgconfig/*.pc

%changelog
* Fri Dec 28 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.1
- Rebuild for Fedora
* Sat Aug 24 2013 dlucio <dlucio> 1.0-13.mga4
+ Revision: 470566
- bump release
* Sat Jan 12 2013 umeabot <umeabot> 1.0-12.mga3
+ Revision: 357931
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild
* Sun Dec 16 2012 dlucio <dlucio> 1.0-11.mga3
+ Revision: 331695
- some requieres not necesary at mageia are dropped
- no static
- imported package liboop
