%undefine _debugsource_packages

Name:		qonverter
Version: 0.9.1.1336027302
Release: 9.1
License:	GPL
Source:		quonverter-%{version}.tar.bz2
Group:		System
Summary:	QT-based simple desktop calculator & unit converter
BuildRequires:  libpng-devel
BuildRequires:	gcc-c++, make, pkgconfig, pkgconfig(QtGui)
URL:		http://code.google.com/p/qonverter/

%description
Qonverter is simple and easy-to-use unit & currency converter and calculator.
It tries to stay as simple as possible and it does NOT target at advanced users. 

%prep
%setup -q -n quonverter-%{version}

%build
lrelease-qt4 Qonverter.pro
qmake-qt4
make

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{makeinstall} INSTALL_ROOT=$RPM_BUILD_ROOT

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
#doc README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Wed May 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.1.1336027302
- Rebuilt for Fedora
* Mon Apr 09 2012 TI_Eugene <ti.eugene@gmail.com> 0.6.7
- Initital build in OBS
