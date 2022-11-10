%global _name CloudCross

Name: cloudcross
Version: 1.4.8
Release: 1
License: BSD
Group: Networking/File transfer
Summary: Syncronization of local files and folders with clouds
#Source: %{_name}-%{version}.tar.gz
Source: %{_name}-master.tar.gz
URL: https://cloudcross.mastersoft24.ru/#usage
BuildRequires: curl-devel
BuildRequires: qt5-qtbase-devel

%description
CloudCross it's open source software for the synchronization of local
files and folders with multiple cloud storages. On this moment
CloudCross supports sync with Yandex.Disk Google Drive Cloud mail.ru
OneDrive and Dropbox. This program was written in pure Qt, without any
third-party libraries.

%prep
%setup -n %_name-master

%build
%qmake_qt5
%make_build

%install
##install -D ccross %buildroot/%_bindir/ccross
%makeinstall INSTALL_ROOT=%buildroot
install -Dm644 ccross-app/doc/ccross %buildroot%_mandir/man1/ccross.1

%files
%doc ccross-app/doc/*.* README* CHANGES*
%_bindir/*
%_mandir/man1/*

%changelog
* Sun Oct 23 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 1.4.8
- Rebuilt for Fedora
* Sat Oct 26 2019 Fr. Br. George <george@altlinux.ru> 1.4.5-alt1
- Autobuild version bump to 1.4.5
* Tue Jan 29 2019 Fr. Br. George <george@altlinux.ru> 1.4.4-alt1
- Autobuild version bump to 1.4.4
* Mon Mar 19 2018 Fr. Br. George <george@altlinux.ru> 1.4.1-alt1
- Autobuild version bump to 1.4.1
* Wed Jul 26 2017 Fr. Br. George <george@altlinux.ru> 1.4.0-alt1
- Autobuild version bump to 1.4.0
* Wed Jul 26 2017 Fr. Br. George <george@altlinux.ru> 1.3.1-alt1
- Initial build for ALT
