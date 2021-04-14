Name: libgpewidget
License: GPL
Group: System Environment/Libraries
Summary: Widgets for the GPE environment
Version: 0.115
Release: 6.1
Source: http://gpe.linuxtogo.org/download/source/%{name}-%{version}.tar.bz2
URL: http://gpe.linuxtogo.org/
BuildRequires: libpng-devel
BuildRequires: gtk2-devel, perl-XML-Parser
Requires: gtk2

%description
The GPE Palmtop Environment (GPE) is a collection of integrated software
components optimized for (but not limited to) handheld and other input
constrained and resource limited devices.

%package	devel
Summary:	Development files for %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	pkgconfig

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
sed -i 's/-lgpewidget/-lgpewidget -lX11/' Makefile*
sed -i 's|glib/gkeyfile\.h|glib.h|' gpehelp.c

%build
%configure
%__make CFLAGS+=-Wno-format-security

%install
%__rm -rf $RPM_BUILD_ROOT
%__make DESTDIR=$RPM_BUILD_ROOT install

%clean
%__rm -rf $RPM_BUILD_ROOT

%files
%doc ChangeLog COPYING.LIB
%{_bindir}/infoprint
%{_libdir}/%{name}.so.1
%{_libdir}/%{name}.so.1.0.0
%{_datadir}/%{name}
%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo

%files devel
%{_includedir}/gpe
%{_libdir}/%{name}.a
%{_libdir}/%{name}.la
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Wed Apr 27 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.115
- Rebuilt for Fedora
