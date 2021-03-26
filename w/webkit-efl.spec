%define svnrel 72693

Summary: Port of WebKit to EFL
Name: webkit-efl
Version: 0.1.0
Release: 1
License: LGPLv2+
Group: Graphical desktop/Enlightenment
URL: http://trac.enlightenment.org/e/wiki/EWebKit
Source: http://packages.profusion.mobi/webkit-efl/webkit-efl-svn-r%{svnrel}.tar.bz2
Patch0: webkit-efl-svn-r72693-libinstall.patch
Patch1: webkit-efl-svn-r72693-curl-link.patch
BuildRequires: cmake
BuildRequires: bison
BuildRequires: flex
BuildRequires: gperf
BuildRequires: ecore-devel
BuildRequires: edje
BuildRequires: embryo
BuildRequires: edje-devel
BuildRequires: evas-devel
BuildRequires: libeina-devel
BuildRequires: libicu-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: sqlite-devel
BuildRequires: curl-devel
BuildRequires: gstreamer-plugins-base-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: cairo-devel
BuildRequires: gtk2-devel
BuildRequires: libxml2-devel
BuildRequires: libxslt-devel
Provides:	ewebkit

%description
Also known as WebKit-EFL, this is the port of WebKit to EFL. In order to
keep it general and as independent as possible it uses (directly) a small
subset of EFL libraries: Evas, Ecore and Edje. Complex non-HTML elements
such as menus are delegated by means of callbacks that one should implement
as desired, probably using Elementary as Eve does.

%package devel
Summary: Enlightenment WebKit Library - devel files
Group: System/Libraries
Requires: %name = %version-%release
Provides: ewebkit-devel = %version-%release

%description devel
Enlightenment WebKit Library (ewebkit) development headers and development libraries.

%prep
%setup -q -n webkit-efl-svn-r%{svnrel}
%patch0 -p0
%patch1 -p0

%build
%cmake -DPORT=Efl -DNETWORK_BACKEND=curl -DCMAKE_INSTALL_LIBDIR=%{_libdir}
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/ewebkit*
%{_libdir}/libewebkit.so.0
%{_libdir}/libewebkit.so.0.*

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/ewebkit*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.0
- Rebuild for Fedora
* Sun Jun 05 2011 Funda Wang <fwang@mandriva.org> 0.1.0-0.72693.3mdv2011.0
+ Revision: 682815
- rebuild for new icu
* Mon Mar 14 2011 Funda Wang <fwang@mandriva.org> 0.1.0-0.72693.2
+ Revision: 644577
- rebuild for new icu
* Sun Dec 19 2010 Funda Wang <fwang@mandriva.org> 0.1.0-0.72693.1mdv2011.0
+ Revision: 622916
- import webkit-efl
