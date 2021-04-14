Name:           matchbox-panel-manager
Version:        0.1
Release:        1
License:        GPL v2 or later
Source:         matchbox-panel-manager-0.1.tar.bz2
Patch0:         matchbox-panel-manager-mb-panel-manager-0.1.diff
Patch1:         matchbox-panel-manager-matchbox-panel-manager_no-return-in-nonvoid-function-0.1.diff
Group:          Productivity/Other
Summary:        Manager for panel
BuildRequires:  pkgconfig
BuildRequires:  startup-notification-devel
BuildRequires:  gtk2-devel, glib2-devel

%description
Panel manager for Matchbox WM.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure LIBS=-lX11
make    

%install
rm -rf %buildroot
make DESTDIR=%buildroot install

%clean
rm -rf %buildroot

%files
%{_bindir}/matchbox-panel-manager
%{_datadir}/applications/mb-panel-manager.desktop
%{_datadir}/pixmaps/mbpanelmgr.png

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1
- Rebuilt for Fedora
* Tue Feb 01 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1-12.20.ossii
- Rebuild for OSSII
* Tue Dec 02 2008 tuukka.pasanen@ilmi.fi
- packaged matchbox-panel-manager version 0.1 using the buildservice spec file wizard
