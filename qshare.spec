Name:           qshare
Version:        2.1.5
Release:        9.1
License:        GNU General Public License version 3.0 (GPLv3)
Source0:        http://www.zuzuf.net/qshare/files/%{name}-%{version}-src.tar.bz2
Group:          Productivity/File utilities
Summary:        Qt file share
BuildRequires:  cmake
BuildRequires:  libpng-devel
BuildRequires:  gcc-c++ libxml2-devel
BuildRequires:  qt4-devel >= 4.5.0
BuildRequires:  qt-webkit-devel
BuildRequires:  avahi-compat-howl-devel
BuildRequires:  avahi-compat-libdns_sd-devel
Requires:       avahi

%description
qShare is a FTP server with a built-in service discovery feature that makes
qShare clients aware of other clients running on the same network. It also
supports Zeroconf on Linux. You can easily add/remove folders from the shared
folders list, set access rights, toggle password protection, etc...
 
The most useful feature is probably the file search feature. The built-in FTP
server implements a FIND command used by qShare to look for files on all known
computers of the network with very little network/CPU overload.

%prep
%setup -q

%build
%cmake
make

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%doc AUTHORS README COPYING
%{_datadir}/%{name}
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/*
%{_datadir}/kde4/services/ServiceMenus/

%changelog
* Tue Aug 23 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 2.1.5
- Rebuild for Fedora
* Sun Feb 27 2011 iattilagy@gmail.com
- packaged qshare-2.1.0 version 2.1.0 using the buildservice spec file wizard
