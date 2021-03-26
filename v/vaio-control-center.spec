Name:           vaio-control-center
Version:        20110915
Release:        7.1
Summary:        GUI to Adjust Vaio Specific Hardware Controls
License:        GPL-2.0+
Group:          Hardware/Other
URL:            http://code.google.com/p/vaio-f11-linux/wiki/VaioControlCenter
Source0:        %{name}-git.%{version}.tar.bz2
Source1:        %{name}.desktop
BuildRequires:  desktop-file-utils
BuildRequires:  qt-devel

%description
This project focuses on getting full Linux compatibility with the Sony Vaio F
series hardware.

%prep
%setup -q -n %{name}

%build
qmake-qt4 QMAKE_CXXFLAGS+="%{optflags}" QMAKE_CFLAGS+="%{optflags}" -config release vaio-control-center.pro
make %{?_smp_mflags}

%install
install -Dm 755 vaio-control-center %{buildroot}%{_bindir}/vaio-control-center
install -Dm 644 vcc/vaio.png %{buildroot}%{_datadir}/pixmaps/vaio.png
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}

%files
%doc COPYING
%{_bindir}/vaio-control-center
%{_datadir}/applications/vaio-control-center.desktop
%{_datadir}/pixmaps/vaio.png

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 20110915
- Rebuild for Fedora
* Mon Aug 27 2012 asterios.dramis@gmail.com
- Use desktop-file-utils instead of deprecated %%suse_update_desktop_file macro
  for installing the desktop file. Replaced update-desktop-files build
  requirement with desktop-file-utils for this.
* Mon Aug 27 2012 asterios.dramis@gmail.com
- Removed %%clean section (not needed anymore).
- Renamed the program name in the desktop file from "Vaio Control Center" to
  "Vaio-control-center".
* Fri Oct 28 2011 asterios.dramis@gmail.com
- Initial release (version git.20110915).
- Added a desktop file for the application.
