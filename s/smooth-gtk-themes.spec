Summary: 	A collection of themes for the Smooth engine
Name: 		smooth-gtk-themes
Version: 	0.5.8
Release: 	3.1
License:	LGPL
URL: 		https://sourceforge.net/projects/smooth-engine/
Source0: 	smooth-themes-%{version}.tar.gz
Group: 		User Interface/Desktops
BuildArch: 	noarch
BuildRequires:	gtk2-devel
Requires:	gtk-smooth-engine

%description
A collection of (mostly) nice, clean, useable GTK themes for the Smooth engine.

%prep
%setup -q -n smooth-themes-%{version}

%build
%configure --disable-gtk-1 --enable-gtk-2
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/themes/*

%changelog
* Thu Jul 07 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5.8
- Rebuilt for Fedora
