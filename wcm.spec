Name:    wcm
Version: 0.20.0
Release: 3.1
Summary: A Far commander clone
License: MIT
Group:   File tools
URL:	 http://wcm.linderdaum.com/
Source:  WCMCommander-release-%{version}.tar.gz
BuildRequires: cmake
BuildRequires: gcc-c++ libX11-devel freetype-devel libsmbclient-devel libssh2-devel samba-common

%description
WCM Commander is a multi-platform open source file manager for Windows, Linux,
FreeBSD and OS X.

%prep
%setup -q -n WCMCommander-release-%{version}

%build
%cmake
make

%install
ln -s ../install-files src/install-files
%make_install

%files
%doc LICENSE CHANGELOG.txt readme_eng.txt README.md
%_bindir/*
%_datadir/applications/*.desktop
%_datadir/pixmaps/*.png
%_datadir/wcm

%changelog
* Tue Apr 19 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.20.0
- Rebuild for Fedora
* Sun Apr 26 2015 Andrey Cherepanov <cas@altlinux.org> 0.20.0-alt1
- New version
- The project was renamed to WCM Commander
* Mon Feb 23 2015 Andrey Cherepanov <cas@altlinux.org> 0.19.0.1-alt1
- New version
* Mon Jan 26 2015 Andrey Cherepanov <cas@altlinux.org> 0.18.1-alt1
- New version (ALT #30593)
* Sat Aug 23 2014 Vitaly Lipatov <lav@altlinux.ru> 0.16.1-alt1
- initial build for Sisyphus
