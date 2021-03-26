Summary:	DXT compression library
Name:		squish
Version:	1.10
Release:	14.1
License:	MIT
Group:		System Environment/Libraries
URL:		http://code.google.com/p/libsquish/
Source0:	http://libsquish.googlecode.com/files/%{name}-%{version}.tar.gz
Source1:	squish-autogen.sh
Source2:	squish-configure.ac
Source3:	squish-Makefile.am
Source4:	squish.pc.in
Patch0:		squish-maths.h.patch
Patch1:		squish-Doxyfile.patch
Patch2:		squish-1.10-gcc43.patch
BuildRequires:	automake, autoconf, libtool, graphviz, doxygen
BuildRequires:	netpbm
BuildRequires:	ghostscript-core

%description
The squish library is a cross-platform open source implementation of DXT
compression (and decompression). DXT compression is a very well-designed
compression scheme for colour textures with an optional alpha channel.

squish is written in standard C++ and has the following features:
    * Supports the DXT1, DXT3 and DXT5 formats.
    * Optimised for both SSE and Altivec SIMD instruction sets.
    * Builds on multiple platforms (x86 and PPC tested).
    * Very simple interface.

%package	devel
Summary:	Development files for the squish DXT compression library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description    devel
This package contains the libraries and header files needed for
developing applications which use the squish library.

%prep
%setup -q
%patch0
%patch1
%patch2 -p1 -b .gcc43
%{__cp} %{SOURCE1} autogen.sh
%{__cp} %{SOURCE2} configure.ac
%{__cp} %{SOURCE3} Makefile.am
%{__cp} %{SOURCE4} squish.pc.in
%{__mv} config.h squish_config.h

%build
sh autogen.sh
%configure --disable-static \
%ifarch x86_64 ia64
  --enable-sse
%endif

%{__make} %{?_smp_mflags}
doxygen Doxyfile

%install
%{__rm} -rf %{buildroot}
%{__make} DESTDIR=%{buildroot} INSTALL="%{__install} -p" install
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc README ChangeLog 
%{_libdir}/libsquish.so.*

%files devel
%doc docs/html/*
%{_includedir}/squish
%{_libdir}/libsquish.so
%{_libdir}/pkgconfig/squish.pc

%changelog
* Fri Oct 18 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.10
- Rebuild for Fedora
* Sun Nov  8 2009 Nicolas Chauvet <kwizart@fedoraproject.org> - 1.10-3
- Disable sse on i686 (broken)
* Wed Apr 29 2009 kwizart <kwizart at gmail.com> - 1.10-2
- Backport patch for gcc43
- Enable SSE on i686 x86_64 ia64
* Thu Nov 08 2007 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> - 1.10-1
- Initial version
