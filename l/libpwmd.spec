Name:           libpwmd
Version:        6.0.2
Release:        7.1
Summary:        A library to patch applications to send commands to PWMD
Group:          Applications/System
License:        GPLv2+
URL:            http://bjk.sourceforge.net/pwmd/
Source0:        http://downloads.sourceforge.net/bjk/%{name}-%{version}.tar.gz
BuildRequires:  libassuan-devel
BuildRequires:  libgpg-error-devel
BuildRequires:  cracklib-devel
#BuildRequires:  pth-devel
BuildRequires:  libssh2-devel
BuildRequires:  c-ares-devel
BuildRequires:  gettext

Requires:       pwmd

%description
This is a library making it easy to patch applications to send commands to
PWMD. Features include:

* Thread safe (POSIX and libpth2 (optional) supported)
* Asynchronous pinentry when threading isn't possible
* Secure remote connections over SSH using libssh2
* Secure memory functions which applications may also use

Read libpwmd.h or libpwmd(3) for all the details. There is an included
command line client 'pwmc' that reads protocol commands from stdin and sends
them to the pwmd server.

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
export LDFLAGS=-lgpg-error
%configure --disable-static \
           --enable-quality \
           --with-pth=no
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
%find_lang %{name}
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%doc ChangeLog COPYING NEWS README TODO
%{_mandir}/man*/*.*
%{_bindir}/pwmc
%{_libdir}/%{name}.so.*
#%{_libdir}/%{name}-pth.so.*

%files devel
%doc KnownBugs 
%{_includedir}/*.h
%{_libdir}/%{name}.so
#%{_libdir}/%{name}-*.so
%{_libdir}/pkgconfig/%{name}.pc
#%{_libdir}/pkgconfig/%{name}-pth.pc

%changelog
* Thu Feb 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 6.0.2
- Rebuilt for Fedora
* Fri Jul 17 2009 Fabian Affolter <fabian@bernewireless.net> - 6.0.2-1
- Added new -devel package
- Added libssh2-devel as a BR
- Updated to new upstream version 6.0.2
* Sun Apr 19 2009 Fabian Affolter <fabian@bernewireless.net> - 5.0.11-1
- Initial package for Fedora
