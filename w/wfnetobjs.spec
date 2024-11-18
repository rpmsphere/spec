%undefine _debugsource_packages

Name:           wfnetobjs
Version:        0.2.4
Release:        10.1
License:        GPL
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  intltool
Group:          Development/Libraries
Summary:        A library handling network objects
Source:         https://www.wallfire.org/download/%{name}-%{version}.tar.bz2
Patch0:         wfnetobjs-autofoomess.patch
Patch1:         wfnetobjs-0.2.4-gcc43.patch
#BuildRequires: compat-srpm-macros

%description
Wfnetobjs is essentially a library which handles network objects (hosts, ports, etc.).

%package devel
Group:          Development/Libraries
Summary:        Wfnetobjs is essentially a library which handles network objects (hosts, ports, etc.).
Requires:       wfnetobjs = %{version} libstdc++-devel

%description devel
Wfnetobjs is essentially a library which handles network objects (hosts, ports, etc.)

%prep
%setup -q
%patch 0 -p1
%patch 1
sed -i "s|@MKINSTALLDIRS@|`pwd`/mkinstalldirs|" Makefile* */Makefile*
sed -i -e 's|@INTL_LIBTOOL_SUFFIX_PREFIX@||' -e 's|@USE_INCLUDED_LIBINTL@|yes|' */Makefile*

%build
export NOCONFIGURE=true
echo | ./autogen.sh
export CFLAGS="%optflags -fno-strict-aliasing -Wno-format-security"
export CXXFLAGS="%optflags -fno-strict-aliasing -Wno-format-security"
touch config.rpath
%configure --disable-static --with-pic
sed -i 's|-Wall|-fPIE -Wall|' tools/Makefile
%{__make} %{?jobs:-j%jobs}

%install
%{__make} install DESTDIR=$RPM_BUILD_ROOT
%find_lang %{name}
%{__rm} -f $RPM_BUILD_ROOT%{_libdir}/*.la

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%{_libdir}/libwfnetobjs.so.0*

%files devel
%dir %{_includedir}/wallfire
%{_includedir}/wallfire/*.h
%{_libdir}/libwfnetobjs.so
%{_libdir}/libwfconfig.a

%changelog
* Wed Aug 01 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.4
- Rebuilt for Fedora
* Tue Sep  1 2009 crrodriguez@suse.de
- build with -fno-strict-aliasing
