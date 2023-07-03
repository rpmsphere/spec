%undefine _debugsource_packages

Name:		qcheckers
Version: 0.1.rev4
Release: 25.1
License:	GPL
Source0:	trunk-%{version}.tar.bz2
Source1:	%{name}.desktop
Source2:	%{name}.png
Group:		Amusements/Games
Summary:	Checkers Game
URL:		https://code.google.com/p/qcheckers
BuildRequires:  libpng-devel
BuildRequires:	gcc-c++, make, pkgconfig, pkgconfig(QtCore), pkgconfig(QtGui)

%description
Qt checkers game. Written as a course work in my university.
Features:
* Russian and international drafts (checkers)
* The player can choose a color
* Setting the depth of move search
* Viewing the history of moves 

%prep
%setup -q -n trunk-%{version}

%build
qmake-qt4
make

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__install} -Dp -m 0755 QCheckers $RPM_BUILD_ROOT%{_bindir}/%{name}
%{__install} -Dp -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
%{__install} -Dp -m 0644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%doc COPYING README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Wed May 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.rev4
- Rebuilt for Fedora
* Thu Dec 01 2011 TI_Eugene <ti.eugene@gmail.com> 0.1
- Initital build in OBS
