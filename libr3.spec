Name:           libr3
Version:        1.3.4
Release:        1
Summary:        A high-performance URL router library
License:        MIT
URL:            https://github.com/c9s/r3
Source0:        https://github.com/c9s/r3/archive/%{version}.tar.gz#/r3-%{version}.tar.gz
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pcre-devel
BuildRequires:  check-devel

%description
libr3 compiles your route paths into a prefix tree (trie). By using the
constructed prefix trie in the start-up time, you may dispatch your routes
with efficiency.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n r3-%{version}


%build
./autogen.sh
%configure --disable-static
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc COPYING LICENSE HACKING.md README.md CHANGES.md
%{_libdir}/*.so.*
#{_bindir}/benchmark

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Wed Aug 16 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 1.3.4
- Initial package
