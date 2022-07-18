%global __os_install_post %{nil}

Name:		vbisam
Version:	2.0
Release:	12.1
Summary:	ISAM file handler
Group:		Development/Languages/Other
License:	GPLv2+ and LGPLv2+
URL:		http://sourceforge.net/projects/vbisam
Source:		http://dl.sourceforge.net/project/vbisam/vbisam2/%{name}-%{version}.tar.gz
BuildRequires:	libtool

%description
* Compatible with the leading commercial ISAM
* 32/64 bit filesystem capable (Break that 2GB barrier!)
* Multi-user aware (row-level locking)
* Transaction processing (begin/commit/rollback)
* Easily extensible

%package devel
Summary:	Development files for vbisam
Requires:	%{name} = %{version}-%{release}

%description devel
Development files for vbisam.

%prep
%setup -q
sed -i '/extern int/s/vbisam_off_t/off_t/' vbisam.h
sed -i '206s/short MISALIGNED/int MISALIGNED/' libvbisam/isinternal.h
sed -i '685s/LONG_MAX : LONG_MIN/INT_MAX : INT_MIN/' libvbisam/vbkeysio.c

%build
%configure --with-compatcisam
make

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS ChangeLog README COPYING COPYING.LIB NEWS
%{_bindir}/*
%{_libdir}/libvbisam.so.*

%files devel
%{_includedir}/*.h
%{_libdir}/libvbisam.a
%exclude %{_libdir}/libvbisam.la
%{_libdir}/libvbisam.so

%changelog
* Thu Dec 18 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0
- Rebuilt for Fedora
* Sun Aug 29 2010 - Sebastian Ritter - 1.1-0.2010-08-29
- OpenSuSE 11.3 with debian compatible package format and standard groups
