Name: msim
Version:      0.4.0
Release:        18.1
Summary:  Library for discrete event simulation
Group:    System Environment/Libraries
License:        GPLv2
URL:       http://msim.sourceforge.net
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  gcc-c++ >= 4.5
BuildRequires:  libtool

%description
A library for discrete event simulation, providing events, actors and an event scheduler.

%package devel
Summary: Development interface for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description -n %{name}-devel
Headers for msim discrete event simulation library.

%prep
%setup -q

%build
# NOTE: this is not GNU/automake configure
./configure --libdir=%{_libdir}
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT LIBDIR=%{_libdir} install

%files
%defattr(-,root,root,-)
%doc README LICENSE
%{_libdir}/lib%{name}.so*

%files devel
%defattr(-,root,root,-)
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*
%{_libdir}/pkgconfig/%{name}.pc

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig

%post -n %{name}-devel
(cd %{_libdir};
  ln -s -f lib%{name}.so.%{version}\
      lib%{name}.so ;
)
/sbin/ldconfig

%postun
/sbin/ldconfig

%postun -n %{name}-devel
(cd %{_libdir};
  rm -f %{name}.so ;
)
/sbin/ldconfig


%changelog
* Mon Apr 16 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.0
- Rebuild for Fedora

* Wed Jun 15 2011 Bernd Stramm <bernd.stramm@gmail.com| - 0.4.0-1
- start packaging
