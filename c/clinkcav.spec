Name:           clinkcav
Version:        2.4
Release:        1
Summary:        CyberLink/AV for C UPnP library
Group:          Development/Libraries
License:        opensource, see COPYING
URL:            http://clinkc.sourceforge.net/
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  clinkc-devel

%description
CyberLink/AV for C is a toolkit for creating UPnP devices and control points.
Main features are automatic discovery, search, expiration handling and different
controlling methods for UPnP control points and advertizing and eventing for UPnP
devices. . This package contains the dynamically loadable library needed by
applications which use CyberLinkC for C.

%package devel
Summary:        CyberLink/AV for C UPnP library
Requires:       %{name}

%description devel
Development files for CyberLink/AV for C UPnP library.

%prep
%setup -q
sed -i -e 's|cybergarage/cupnp\.h|cybergarage/upnp/cupnp.h|' -e 's/new=no/new=yes/' configure

%build
%configure --prefix=/usr LIBS='-lexpat -lpthread -luuid'
make

%install
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}

%clean
%__rm -rf %{buildroot}

%files
%doc ChangeLog COPYING
%{_libdir}/lib%{name}.so*

%files devel
%{_libdir}/lib%{name}.*a
%{_includedir}/cybergarage/upnp/std/av

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2.4
- Rebuilt for Fedora
