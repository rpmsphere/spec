%undefine _debugsource_packages

Name:		ptbatterysystemtray
Version: 0.9.9
Release: 5.1
License:	GPL
Vendor:		Brieuc Roblin <brieuc.roblin@gmail.com>
Source:		%{name}-%{version}.tar.bz2
Group:		System/X11/Utilities
URL:		https://www.pyrotools.org/
Summary:	A simple battery monitor in the system tray, in Qt
BuildRequires:	gcc-c++, pkgconfig(QtGui)

%description
It allows to handle power management and CPU frequency.

%prep
%setup -q

%build
qmake-qt4 INSTALL_PREFIX=/usr
make

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{makeinstall} INSTALL_ROOT=$RPM_BUILD_ROOT

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS LICENCE NEWS README ChangeLog
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Sun Aug 05 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.9
- Rebuilt for Fedora
* Thu Jun 21 2012 TI_Eugene <ti.eugene@gmail.com> 0.9.9
- Next version (1.0.0.rc2)
- Switched to original git
* Fri Apr 29 2011 Petr Vanek <petr@scribus.info> 0.8.0
- Initial build at OBS
