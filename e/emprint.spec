Summary: 	E17 screen capture utility
Name: 		emprint
Version: 	0.1.0
Release: 	20101225
Source:		%{name}-%{version}.tar.gz
License: 	BSD
Group: 		Graphical desktop/Enlightenment
URL: 		http://www.enlightenment.org/
# Common
BuildRequires:	imlib2-devel
BuildRequires:	libX11-devel
# Enlightenment BR
BuildRequires:	libeina-devel
BuildRequires: 	eet-devel
BuildRequires:  evas-devel
BuildRequires:	ecore-devel
BuildRequires:	efreet-devel
BuildRequires:	embryo-devel
BuildRequires:	edje-devel
BuildRequires:	emotion-devel
BuildRequires:	e_dbus-devel
BuildRequires:	exchange-devel
BuildRequires:	eeze-devel

%description
Emprint is a utility for taking screenshots of the entire screen, a specific
window, or a specific region. It is written with the Enlightenment Foundation
Libraries.

%prep
%setup -q

%build
./autogen.sh --disable-static --prefix=/usr
make

%install
rm -rf %{buildroot}
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf %{buildroot}

%files
%doc AUTHORS README ChangeLog NEWS TODO
%{_bindir}/*
%{_datadir}/%name

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuild for Fedora
* Fri Jan 21 2011 Wei-Lun Chao <bluebat@member.fsf.org>
- Rebuild for OSSII

* Sat Dec 25 2010 Texstar <texstar at gmail.com> 20101225-1pclos2010
- update svn

* Wed Dec 15 2010 Texstar <texstar at gmail.com> 20101215-1pclos2010
- update svn 55246
