Name:		osptoolkit
Summary:	Toolkit for ETSI OSP standard for secure VoIP peering
Version:	4.13.0
Release:	7.1
License:	BSD
Group:		Development/Libraries/C and C++
URL:		http://sf.net/projects/osp-toolkit
Source:		http://sourceforge.net/projects/osp-toolkit/files/OSPToolkit-%{version}.tar.gz
Patch1:		osp-automake.diff
BuildRequires:	autoconf, automake, libtool
BuildRequires:	compat-openssl10-devel

%description
The OSP Toolkit is a complete development kit for software developers
who want to implement the client side of the European
Telecommunication Standards Institute's (ETSI) Open Settlement
Protocol. The OSP Toolkit includes source code written in ANSI C,
test tools and extensive documentation on how to implement OSP. A
hosted OSP test server is freely available on the Internet for all
developers to test their OSP implementation.

%package devel
Summary:	Toolkit for ETSI OSP standard for secure VoIP peering
Group:		Development/Libraries/C and C++
Requires:	%name = %version

%description devel
The OSP Toolkit is a complete development kit for software developers
who want to implement the client side of the European
Telecommunication Standards Institute's (ETSI) Open Settlement
Protocol. The OSP Toolkit includes source code written in ANSI C,
test tools and extensive documentation on how to implement OSP. A
hosted OSP test server is freely available on the Internet for all
developers to test their OSP implementation.

%prep
%setup -qn TK-4_13_0-20161107
%patch -P 1 -p1
sed -i 's|OSPM_ISNAN(metrics.mean, tnisnan);|OSPM_ISNAN((float)metrics.mean, tnisnan);|' src/osptransapi.c

%build
autoreconf -fi
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=%buildroot

%files
%_libdir/libosptk-*.so

%files devel
%_libdir/libosptk.so
%exclude %_libdir/libosptk.la
%_includedir/osp

%changelog
* Thu Dec 15 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 4.13.0
- Rebuild for Fedora
