Name:		grive
Version:	0.2.0
Release:	17.1
Summary:	Open source implementation of Google Drive client
Group:		Networking/File transfer
License:	GPLv2
URL:		http://www.lbreda.com/grive/
Source0:	http://www.lbreda.com/grive/_media/packages/%{version}/%{name}-%{version}.tar.gz
Patch0:		grive-0.2.0-json-c.patch
BuildRequires:	cmake
BuildRequires:	libgcrypt-devel
BuildRequires:	json-c-devel
BuildRequires:	libcurl-devel
BuildRequires:	expat-devel
BuildRequires:	boost-devel
BuildRequires:	binutils-devel
BuildRequires:	yajl-devel

%description
The purpose of grive project is to provide an independent open source
implementation of Google Drive client for GNU/Linux. It uses the Google
Document List API to talk to the servers in Google. The code is written
in standard C++.

Currently as of version 0.2.0, grive can do two-side synchronization
between the Google Drive and local directory. It can download and upload
changed files. New directories in Google Drive and local directory will
also be downloaded/uploaded.

%prep
%setup -q
%patch0
sed -i -e 's|json_tokener_errors|json_tokener_error_desc|' -e '359d' libgrive/src/protocol/Json.cc
sed -i -e 's|bfd_section_size(abfd, section)|bfd_section_size(section)|' -e 's|bfd_get_section_vma(abfd, section)|bfd_section_vma(section)|' libgrive/src/bfd/SymbolInfo.cc

%build
%cmake
make

%install
%make_install

%files
%{_bindir}/%{name}
%{_mandir}/man?/%{name}.*

%changelog
* Mon Oct 14 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.0
- Rebuilt for Fedora
* Thu Jul 11 2013 fwang <fwang> 0.2.0-2.mga4
+ Revision: 452818
- rebuild for new boost
* Sat Jun 29 2013 wally <wally> 0.2.0-1.mga4
+ Revision: 448403
- imported package grive
