%define git_date 20100812
%define git_commit 2f149fb

Name:           iat
Version:        0.1.7git%{git_date}
Release:        6.1
License:        GPL-2.0+
Summary:        ISO 9660 Analyzer Tool
URL:            https://iat.berlios.de
Group:          Productivity/Other
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  libtool

%description
ISO 9660 Analyzer Tool is a tool for detecting the structure of many
types of CD/DVD image. With ISO 9660 Analyzer Tool you can:
- Create Cuesheet file from image CD/DVD.
- Create TOC file from image CD/DVD.
- Convert image CD/DVD to ISO 9660.
- Debug image.

%package -n libiat
Summary:        IAT Shared Library
Group:          System/Libraries

%description -n libiat
Shared library for the ISO 9660 Analyzer Tool.

%package -n libiat-devel
Summary:        IAT Development Files
Group:          Development/Libraries/C and C++
Requires:       libiat = %{version}

%description -n libiat-devel
Development files for the ISO 9660 Analyzer Tool.

%prep
%setup -qn %{name}-%{git_commit}

%build
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%post -n libiat -p /sbin/ldconfig

%postun -n libiat -p /sbin/ldconfig

%files
%doc AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/%{name}
%doc %{_mandir}/man1/*

%files -n libiat
%{_libdir}/*.so.*

%files -n libiat-devel
%{_includedir}/libiat
%{_libdir}/*.so

%changelog
* Wed Aug 01 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.7+git%{git_date}
- Rebuilt for Fedora
* Fri Jun  8 2012 lazy.kent@opensuse.org
- Add iat-0.1.7-automake112.patch: fix build with automake-1.12.
- Fix typos in Summary/Description.
* Sat Dec  3 2011 lazy.kent@opensuse.org
- Build requires libtool.
* Tue Nov  8 2011 lazy.kent@opensuse.org
- Patch to fix man page.
- Added COPYING to docs.
- Corrected License tag.
- spec clean up.
* Fri Aug 13 2010 lazy.kent.suse@gmail.com
- update to latest git revision - 2f149fb
* Fri May 21 2010 lazy.kent.suse@gmail.com
- initial package created - 0.1.7
