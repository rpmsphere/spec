%define giflib_ver %(rpm -q --qf %{version} giflib-devel)

Summary:	Compatible package using giflib
Name:		libungif-compat
Version:	%{giflib_ver}
Release:	1.1
License:	MIT
Group:		System Environment/Libraries
URL:		http://www.sourceforge.net/projects/giflib/
BuildRequires:	giflib-devel
Provides:       libungif = %{version}-%{release}
Obsoletes:      libungif <= %{version}-%{release}

%description
libungif supported uncompressed GIFs while the Unisys LZW patent was in effect.
It is the API and ABI compatible package using giflib.

%package devel
Summary:	Development tools for libungif library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	giflib-devel
Provides:       libungif-devel = %{version}-%{release}
Obsoletes:      libungif-devel <= %{version}-%{release}

%description devel
This package includes development files for libungif.

%prep

%build
MAJOR=`echo '%{version}' | sed -e 's/\([0-9]\+\)\..*/\1/'`
%{__cc} $RPM_OPT_FLAGS -Wl,-z,now -shared -Wl,-soname,libungif.so.$MAJOR -lgif -o libungif.so.%{version}

%install
install -Dm 755 libungif.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libungif.so.%{version}
ln -sf libungif.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libungif.so.4
ln -sf libungif.so.4 $RPM_BUILD_ROOT%{_libdir}/libungif.so

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files 
%{_libdir}/lib*.so.*

%files devel
%{_libdir}/lib*.so

%changelog
* Mon Jul 23 2018 Huaren Zhong <huaren.zhong@gmail.com> 5.1.4
- Rebuild for Fedora
