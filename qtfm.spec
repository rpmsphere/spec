%global debug_package %{nil}

Summary:	Qt File Manager
Name:		qtfm
Version:	6.2.0
Release:	1
URL:		http://qtfm.eu/
License:	GPL
Source:		https://github.com/rodlie/qtfm/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Requires:	p7zip
BuildRequires:	gcc-c++, qt5-devel, file-devel
Group:		Applications/File
  
%description
qtFM is a small, lightweight file manager for Linux desktops based on pure Qt
and works great with minimal desktop environments like Openbox.

%prep
%setup -q
#sed -i '223s|return false;|return "";|' src/mymodel.cpp

%build
#lrelease-qt5 %{name}.pro
qmake-qt5 PREFIX=/usr
make

%install
rm -rf %{buildroot}
%{makeinstall} INSTALL_ROOT=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%{_datadir}/doc/%{name}*
%{_bindir}/%{name}*
%{_datadir}/applications/%{name}*.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_sysconfdir}/xdg/autostart/qtfm-tray.desktop
%{_mandir}/man1/*

%changelog
* Thu Sep 05 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 6.2.0
- Rebuild for Fedora
* Fri Jun 29 2012 TI_Eugene <ti.eugene@gmail.com> - 5.5
- Next version
* Sat Nov 05 2011 TI_Eugene <ti.eugene@gmail.com> - 5.1
- Next version
* Wed Jun 01 2011 TI_Eugene <ti.eugene@gmail.com> - 4.9
- Initial build in OBS
