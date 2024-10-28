Name: libhildonhelp
License: GPL
Group: System Environment/Libraries
Summary: Hildon Help Runtime library
Version: 1.9.7
Release: 1
Source: hildon-help-svn20080519.tar.bz2
BuildRequires: gtk2-devel, libosso-devel, libhildon-devel, libxml2-devel
BuildRequires: gtkhtml3-devel
Requires: gtk2, libosso, libhildon, gtkhtml3, libxml2

%description
Shared library required for running Help UI and integrating
with other applications.
 
%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n hildon-help
sed -i -e 's/1\.7/1.10/' -e 's/3\.8/4.0/' configure*
sed -i 's/-D[GTDK]*_DISABLE_DEPRECATED/-Wall -Wl,--allow-multiple-definition/g' src/Makefile* helptest/Makefile*
ln -sf /usr/share/libtool/config/config.sub config.sub

%build
autoreconf -ifv
%configure
%__make

%install
%__rm -rf %{buildroot}
%__make DESTDIR=%{buildroot} install

%files
%doc README ChangeLog COPYING
%{_bindir}/*
%{_libdir}/libhildonhelp.so.0*

%files devel
%{_includedir}/hildon-help
%{_libdir}/libhildonhelp.a
#{_libdir}/libhildonhelp.la
%{_libdir}/libhildonhelp.so
%{_libdir}/pkgconfig/hildon-help.pc

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.9.7
- Rebuilt for Fedora
