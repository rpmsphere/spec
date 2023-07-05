Name:          liblinc
Version:       1.1.1
Release:       17.1
Summary:       Library for writing networked clients and servers
Group:         System/Libraries
URL:           https://www.gnome.org
Source:        https://ftp.gnome.org/pub/GNOME/sources/linc/%(echo %version | cut -d. -f 1-2)/linc-%{version}.tar.bz2
License:       GPL
BuildRequires: glib2-devel
BuildRequires: libxml2
BuildRequires: gtk-doc
BuildRequires: w3m

%description
Library for writing networked clients and servers.

%package devel
Summary:       Devel package for liblinc
Group:         Development/Libraries
Requires:      %{name} = %{?epoch:%epoch:}%{version}-%{release}

%description devel
Library for writing networked clients and servers.

This package contains static libraries and header files need for development.

%prep
%setup -q -n linc-%{version}
sed -i 's|glib/g.*\.h|glib.h|' include/linc/linc-*.h
sed -i 's|-DG_DISABLE_DEPRECATED||' src/Makefile.*
sed -i 's|sizeof (struct sockaddr_irda)|sizeof (struct sockaddr_irda *)|' src/linc-protocols.c

%build
export LDFLAGS='-L%{_libdir}'
%configure \
   --libexecdir=%{_sbindir} \
   --enable-shared \
   --disable-gtk-doc
make -j1

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

# remove program that already exists in ORBit package
rm -f $RPM_BUILD_ROOT%{_bindir}/linc-cleanup-sockets

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS ChangeLog COPYING HACKING MAINTAINERS NEWS README TODO
%{_libdir}/*.so.*

%files devel
%{_bindir}/linc-*
%{_datadir}/aclocal/linc.m4
%{_datadir}/gtk-doc/html/linc
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/linc.pc
%dir %{_includedir}/linc-?.?/linc
%{_includedir}/linc-?.?/linc/*.h

%changelog
* Wed Jun 29 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.1
- Rebuilt for Fedora
* Thu Jan 01 2009 Silvan Calarco <silvan.calarco@mambasoft.it> 1.1.1-2mamba
- specfile updated
* Tue Jun 13 2006 Stefano Cotta Ramusino <stefano.cotta@qilinux.it> 1.1.1-1qilnx
- update to version 1.1.1 by autospec
* Tue Dec 30 2003 Silvan Calarco <silvan.calarco@mambasoft.it> 1.0.3-1qilnx
- first build
