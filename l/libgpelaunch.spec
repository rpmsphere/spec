Name: libgpelaunch
License: GPL
Group: System Environment/Libraries
Summary: Launch for the GPE environment
Version: 0.14
Release: 4.1
Source: https://gpe.linuxtogo.org/download/source/%{name}-%{version}.tar.bz2
URL: https://gpe.linuxtogo.org/
BuildRequires: libpng-devel
BuildRequires: gtk2-devel, startup-notification-devel

%description
The GPE Palmtop Environment (GPE) is a collection of integrated software
components optimized for (but not limited to) handheld and other input
constrained and resource limited devices.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
%configure
%__make

%install
%__rm -rf $RPM_BUILD_ROOT
%__make DESTDIR=$RPM_BUILD_ROOT install

%files
%{_libdir}/%{name}.so.*
/usr/libexec/%{name}

%files devel
%{_includedir}/gpe/*.h
%{_libdir}/%{name}.a
#{_libdir}/%{name}.la
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Wed Apr 27 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.14
- Rebuilt for Fedora
