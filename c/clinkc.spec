%undefine _debugsource_packages
Name:           clinkc
Version:        2.4
Release:        1
Summary:        CyberLink for C UPnP library
Group:          Development/Libraries
License:        opensource, see COPYING
URL:            http://clinkc.sourceforge.net/
Source0:        http://sourceforge.net/projects/clinkc/files/clinkc/%{version}/%{name}240.tar.gz
BuildRequires:  doxygen

%description
CyberLink for C is a toolkit for creating UPnP devices and control points.
Main features are automatic discovery, search, expiration handling and different
controlling methods for UPnP control points and advertizing and eventing for UPnP
devices. . This package contains the dynamically loadable library needed by
applications which use CyberLinkC for C.

%package devel
Summary:        CyberLink for C UPnP library
Requires:       %{name}	

%description devel
Development files for CyberLink for C UPnP library.

%prep
%setup -q -n %{name}
sed -i 's/2\.3/2.4/' configure.in
sed -i 's/doxygen/doxygen-objc/' Doxyfile.objc

%build
aclocal
autoconf
automake
%configure --prefix=/usr --enable-anyaddr CFLAGS=-fPIC
make

%install
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}
%__rm -rf %{buildroot}%{_datadir}/doc/%{name}0

%clean
%__rm -rf %{buildroot}

%files
%doc ChangeLog COPYING
%{_libdir}/lib%{name}*

%files devel
%{_includedir}/cybergarage
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/doc/%{name}*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2.4
- Rebuilt for Fedora
