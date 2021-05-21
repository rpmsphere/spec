Summary:	WebKit-EFL demo application
Name:		eve
Version:	0.3.0
Release:	1
License: 	GPLv3
Group: 		Graphical desktop/Enlightenment
Source:		http://download.enlightenment.org/snapshots/LATEST/%{name}-%{version}.tar.gz
URL:		http://www.enlightenment.org/
BuildRequires: 	ecore-devel
BuildRequires:	webkit-efl-devel

%description
WebKit-EFL demo application.

%prep
%setup -q

%build
%configure
make

%install
rm -fr %buildroot
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS COPYING* README
%{_bindir}/%name
%{_datadir}/%name
%{_datadir}/pixmaps/*.png
%{_datadir}/applications/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuilt for Fedora
* Thu Oct 27 2011 Wei-Lun Chao <bluebat@member.fsf.org> 0.3.0-1.ossii
- Initial package
