Summary: A Thai im for GTK2
Name: gtk-im-libthai
Version: 0.2.1
Release: 8.1
License: GPL
Group: System Environment/Libraries
Source: ftp://linux.thai.net/pub/ThaiLinux/software/libthai/%{name}-%{version}.tar.gz
URL: https://linux.thai.net/
BuildRequires: gtk2-devel
BuildRequires: autoconf, libtool
BuildRequires: libthai-devel

%description
gtk-im-libthai is a Thai im for GTK2.

%prep
%setup -q

%build
autoconf
%configure --prefix=/usr --enable-shared
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
gtk-query-immodules-2.0 > /etc/gtk-2.0/gtk.immodules

%postun
/sbin/ldconfig
gtk-query-immodules-2.0 > /etc/gtk-2.0/gtk.immodules

%files
%doc README AUTHORS COPYING ChangeLog
%{_libdir}/gtk-2.0/2.10.0/immodules/im-thai-libthai.*
%exclude %{_libdir}/gtk-3.0/3.0.0/immodules/im-thai-libthai.*

%changelog
* Mon Aug 13 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.1
- Rebuilt for Fedora
* Tue Jan 8 2004 Supphachoke Suntiwichaya <mrchoke@opentle.org> 0.1.1-2_02tle
- Patch KeyPad from CVS
* Wed Dec 24 2003 Supphachoke Suntiwichaya <mrchoke@opentle.org> 0.1.1-2_01tle
- Build from CVS 24/12/03, Fixed bug numlock and caplock
* Tue Nov 18 2003 Supphachoke Suntiwichaya <mrchoke@opentle.org> 0.1.1-1_01tle
- Frist Spec for LinuxTLE 5.0.95 or Fedora Core 1
