Name:           granite
Version:	0.4.0.1
Release:	1
License:	GPLv3.0
Summary:	A development library for elementary development
URL:		https://launchpad.net/granite
Group:		System/Libraries
Source:		https://launchpad.net/granite/0.4/0.4.0.1/+download/%{name}-%{version}.tar.xz
BuildRequires:	cmake
BuildRequires:	vala-devel >= 0.16
BuildRequires:	pkgconfig
BuildRequires:	libgee-devel 
BuildRequires:	gobject-introspection-devel 
BuildRequires:	gettext-devel
BuildRequires:	gtk3-devel
Requires: 	hicolor-icon-theme

%description
Granite is an extension of GTK. Among other things, it provides the 
commonly-used widgets such as modeswitchers, welcome screens, AppMenus, 
search bars, and more found in elementary apps.

%package devel
Group:		Development/Libraries
Summary:	Development headers and libraries for granite
Requires:	%{name} = %{version}-%{release}

%description devel
Development headers and libraries for granite.

%prep
%setup -q

%build
cmake . \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_INSTALL_LIBDIR=%{_libdir}
make

%install
make install DESTDIR=%{buildroot}
 
%files
%doc AUTHORS COPYING
%{_datadir}/icons/hicolor/*/actions/*.svg
%{_datadir}/locale/
%{_libdir}/girepository-1.0/Granite-1.0.typelib
%{_libdir}/libgranite.so.3
%{_libdir}/libgranite.so.3.0.1

%files devel
%{_bindir}/granite-demo
%{_datadir}/applications/granite-demo.desktop
%{_includedir}/%{name}
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/Granite-1.0.gir
%{_datadir}/vala/vapi/%{name}.*

%changelog
* Fri Nov 11 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.0.1
- Rebuild for Fedora
* Mon Sep 21 2015 David Vasquez <davidjeremias82 AT gmail DOT com> 0.3.1
- Updated to 0.3.1
* Tue Jun 18 2013 David Vasquez <davidjeremias82 AT gmail DOT com>
- initial build rpm version 0.2.1
