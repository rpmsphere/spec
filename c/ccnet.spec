Name:           ccnet
Version:        1.3.4
Release:        6.1
Summary:        Networking library framework
License:        GPLv3
URL:            https://github.com/haiwen/ccnet
Source0:        ccnet-master.zip
BuildRequires:  glib2-devel
BuildRequires:  python2-devel >= 2.6
BuildRequires:  sqlite-devel
BuildRequires:  openssl-devel
BuildRequires:  libevent-devel
BuildRequires:  libuuid-devel
BuildRequires:  searpc-devel
BuildRequires:  vala-devel

%description
Ccnet is a framework for writing networked applications in C.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n ccnet-master
sed -i -e /\(DESTDIR\)/d libccnet.pc.in

%build
./autogen.sh
%configure --disable-static --disable-compile-demo
make

%install
make install DESTDIR=%{buildroot}
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
#%doc AUTHORS COPYING README.markdown
%{_libdir}/*.so.*
%{_bindir}/%{name}*
%{python_sitearch}/%{name}

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/lib%{name}.pc

%changelog
* Sun Jun 23 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.3.4
- Rebuilt for Fedora
* Tue Jun 18 2013 Stefan Lohmaier <stefan.lohmaier@stefanlohmaier.de> - 1.3.4-1
- updated for seafile 1.7.0
* Thu May 30 2013 Stefan Lohmaier <stefan.lohmaier@stefanlohmaier.de> - 1.1.0-1
- added description from github
- moved to 1.1.0 from seafile 1.6.1
* Mon Jan 28 2013 Robin Lee <cheeselee@fedoraproject.org> - 1.0.1-1
- Initial package
