%global debug_package %{nil}

Name:		qtpuzzle
Version: 0.0.1.rev278
Release: 19.1
License:	GPL
Source0:	%{name}-%{version}.tar.bz2
Source1:    %{name}.png
Group:		Amusements/Games
Summary:	Puzzle Game
URL:		http://code.google.com/p/qtdesktop
BuildRequires:  libpng-devel
BuildRequires:	gcc-c++, make, pkgconfig, pkgconfig(QtCore), pkgconfig(QtGui)

%description
%{summary}

%prep
%setup -q

%build
qmake-qt4
make

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{makeinstall} INSTALL_ROOT=$RPM_BUILD_ROOT
install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/%{name}.png
sed -i 's|#Icon|Icon|' %{buildroot}%{_datadir}/applications/%{name}.desktop

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Wed May 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0.1.rev278
- Rebuild for Fedora
* Thu Dec 01 2011 TI_Eugene <ti.eugene@gmail.com> 0.0.1
- Initital build in OBS
