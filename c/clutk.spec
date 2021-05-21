Name:           clutk
Version:        0.3.60
Release:        1
License:        GPLv3
Group:          Development/Libraries
Summary:        A general-purpose toolkit for Clutter
URL:            https://launchpad.net/clutk
Source:         http://launchpadlibrarian.net/38183759/%{name}-%{version}.tar.gz
BuildRequires:	clutter-devel, clutter-gtk-devel, glew-devel, librepository, vala-devel

%description
A general-purpose toolkit for Clutter used by UNR's netbook-launcher.

%package devel
Summary:        Development files for %{name}
Requires:	%{name}

%description devel
Development files for %{name}.

%prep
%setup -q
sed -i 's/clutter-gtk-0\.10/clutter-gtk-1.0/' configure clutk.pc.in

%build
%configure --disable-introspection --prefix=/usr
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

%clean
rm -rf %{buildroot}

%files
%{_libdir}/lib%{name}-*.so*
%{_datadir}/%{name}

%files devel
%doc AUTHORS TODO COPYING
%exclude %{_datadir}/gtk-doc/html/%{name}
%{_libdir}/lib%{name}-*.la
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*
%{_datadir}/vala/vapi/%{name}-*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuilt for Fedora
* Tue May 31 2011 Wei-Lun Chao <bluebat@member.fsf.org>
- Update to 0.3.60

* Fri Jul 31 2009 Wei-Lun Chao <bluebat@member.fsf.org>
- Initial Package
