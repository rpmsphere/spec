Name:         	dynamips 
Version:        0.2.16
Release:        4.1
License:        GPL
BuildRequires:  cmake
BuildRequires:  elfutils-libelf-devel
BuildRequires:  libpcap-devel
BuildRequires:  libuuid-devel
Source:         https://codeload.github.com/GNS3/dynamips/tar.gz/v0.2.16#/%{name}-%{version}.tar.gz
Group:          Emulators
Summary:        Cisco router Emulator

%description
Dynamips is a software that emulates Cisco IOS on a traditional PC.

%prep
%setup -q

%build
%cmake
%{__make}

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT mandir=%{_mandir} bindir=%{_bindir}

%files
%{_docdir}/%{name}
%{_bindir}/dynamips
%{_bindir}/nvram_export
%{_mandir}/man?/*.?.gz

%changelog
* Thu Jan 19 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.16
- Rebuild for Fedora
* Fri Jun 20 2008 crrodriguez@suse.de
- update to version 0.2.8 RC per user requests
