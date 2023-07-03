%undefine _debugsource_packages

Name:		samegame
Version:	1.1.0
Release:	4.1
Summary:	Qt implementation of SameGame
Group:		Amusements/Games
License:	GPLv3
URL:		https://samegame.sourceforge.net/
Source0:	%{name}-%{version}.tar.gz
BuildRequires:	qt-devel

%description
Qt implementation of SameGame.

%prep
%setup -q

%build
qmake-qt4 . PREFIX=%{_prefix} VERSION=%{version}
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install INSTALL_ROOT=$RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT/%{_datadir}/doc/%{name}-%{version}

%clean
rm -rf %{buildroot}

%files
%doc gpl.txt readme.txt
%{_bindir}/*
%{_datadir}/applications/samegame.desktop
%{_datadir}/icons/hicolor/scalable/apps/samegame.svg

%changelog
* Tue May 05 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.0
- Rebuilt for Fedora
* Sat Mar 05 2011 Jari Karppinen <jari.p.karppinen at, gmail.com> 1.1.0-1
- Qt port.
* Sat Mar 05 2011 Jari Karppinen <arkiwursti at, gmail.com> 1.0.1-1
- Started using CMake, desktop entry and icon added, fixes for packaging.
* Wed Aug 12 2009 Jari Karppinen <arkiwursti at, gmail.com> 1.0.0-1
- Initial attempt at packaging.
