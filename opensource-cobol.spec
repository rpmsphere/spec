Name:           opensource-cobol
Version:        1.5.2J
Release:        1
Summary:        Open-source COBOL compiler
Group:          Development/Languages
License:        GPLv2+ and LGPLv2+
URL:            https://github.com/opensourcecobol/opensource-cobol
Source:         https://github.com/opensourcecobol/opensource-cobol/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  gmp-devel >= 4.1.4
BuildRequires:  readline-devel
BuildRequires:  libdb-devel
BuildRequires:  libtool-ltdl-devel
Requires:       gcc
Requires:       glibc-devel
Requires:       libcob = %{version}
Obsoletes:      libcob-devel < 1.0.90
Obsoletes:      open-cobol opencobol

%description
"opensource COBOL" is open-source COBOL compiler, an extension of
the Japan-specific features. "opensource COBOL" translates COBOL
program to C code and compiles it using GCC or CL.
It was forked from OpenCOBOL in 2012.

%package -n libcob
Summary:        OpensourceCOBOL runtime library
Group:          Development/Libraries
Requires(post): /sbin/ldconfig
Requires(postun):       /sbin/ldconfig

%description -n libcob
%{summary}.
Runtime libraries for OpensourceCOBOL

%prep
%setup -q

%build
export CFLAGS="$RPM_OPT_FLAGS -fPIC -Wno-format-security -O"
export CPPFLAGS="$CFLAGS"
%configure
make %{?_smp_mflags} 

%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT/%{_libdir} -type f -name "*.*a" -exec rm -f {} ';'
rm -rf $RPM_BUILD_ROOT/%{_infodir}/dir

%files
%doc AUTHORS COPYING ChangeLog
%doc NEWS README THANKS TODO
%{_bindir}/cobc
%{_bindir}/cob-config
%{_bindir}/cobcrun
%{_datadir}/%{name}-%{version}
%{_infodir}/*.info*
%{_includedir}/libcob*
%{_libdir}/libcob.so
%{_datadir}/locale/ja/LC_MESSAGES/*.mo

%files -n libcob
%doc COPYING.LIB
%{_libdir}/libcob.so.*

%clean
rm -rf $RPM_BUILD_ROOT

%post 
/sbin/install-info %{_infodir}/open-cobol.info %{_infodir}/dir 2>/dev/null || :

%postun 
if [ $1 = 0 ]; then
  /sbin/install-info --delete %{_infodir}/open-cobol.info %{_infodir}/dir 2>/dev/null || :
fi

%post -n libcob -p /sbin/ldconfig

%postun -n libcob -p /sbin/ldconfig

%changelog
* Tue Jul 23 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 1.5.2J
- Rebuild for Fedora
