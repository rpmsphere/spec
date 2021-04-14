%undefine _debugsource_packages

Name:           qnetwalk
BuildRequires:  gcc-c++ qt4-devel
License:        GNU General Public License (GPL)
Group:          Amusements/Games/Logic
Summary:        Game for System Administrators
Version:        1.4
Release:        1
URL:            http://qt.osdn.org.ua/qnetwalk.html
Source0:        %{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png

%description
This is a Qt-version of the popular NetWalk game for system administrators.
You have to connect all computers to the central server with as few clicks as possible.

Authors:
--------
    Andi Peredri <andi@ukr.net>

%prep
%setup -q
sed -i 's|-lSDL_mixer|-lSDL -lSDL_mixer|' %{name}.pro

%build
qmake-qt4
make %{?jobs:-j %jobs}

%install
make install INSTALL_ROOT=$RPM_BUILD_ROOT
mv $RPM_BUILD_ROOT/usr/games $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
install -m 0644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc COPYING ChangeLog README
%{_bindir}/qnetwalk
%{_datadir}/applications/qnetwalk.desktop
%{_mandir}/man6/qnetwalk.6.*
%{_datadir}/pixmaps/qnetwalk.xpm
%{_datadir}/qnetwalk
%{_datadir}/pixmaps/*
%exclude %{_datadir}/menu/qnetwalk

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.4
- Rebuilt for Fedora
* Mon Oct 27 2008 john@ossii.com.tw
- Rebuild for M6(OSSII)
* Fri May 16 2008 prusnak@suse.cz
- patched qmake project file (qnetwalk.patch)
- slightly modified spec file
* Mon Apr  7 2008 phoenixseve@gmx.de
- initial package created (version 1.3)
