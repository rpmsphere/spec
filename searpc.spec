Name:           searpc
Version:        1.1.0
Release:        6.1
Summary:        RPC library for Seafile
License:        GPLv3
URL:            https://github.com/haiwen/libsearpc
Source0:        libsearpc-master.zip
BuildRequires:  glib2-devel
BuildRequires:  python-devel

%description
Searpc is a simple C language RPC framework based on GObject system.
Searpc handles the serialization/deserialization part of RPC,
the transport part is left to users.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n libsearpc-master
sed -i -e /\(DESTDIR\)/d libsearpc.pc.in

%build
./autogen.sh
%configure --disable-static --disable-compile-demo
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc AUTHORS COPYING README.markdown
%{_libdir}/*.so.*
%{_bindir}/searpc-codegen.py
%{python_sitearch}/pysearpc/

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/lib%{name}.pc

%changelog
* Sun Jun 23 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.0
- Rebuild for Fedora
* Tue Jun 18 2013 Stefan Lohmaier <stefan.lohmaier@stefanlohmaier.de> - 1.1.0-2
- updated for seafile 1.7.0
* Thu May 30 2013 Stefan Lohmaier <stefan.lohmaier@stefanlohmaier.de> - 1.1.0-1
- added description from github
- moved to 1.1.0 from seafile 1.6.1
* Mon Jan 28 2013 Robin Lee <cheeselee@fedoraproject.org> - 1.0.1-1
- Initial package
