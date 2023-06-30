%global __os_install_post %{nil}

Name:           libpwmd
Version:        8.4.2
Release:        2
Summary:        A library to patch applications to send commands to PWMD
Group:          Applications/System
License:        GPLv2+
URL:            https://bjk.sourceforge.net/pwmd/
Source0:        https://downloads.sourceforge.net/bjk/%{name}-v%{version}.tar.gz
BuildRequires:  libassuan-devel
BuildRequires:  libgpg-error-devel
BuildRequires:  cracklib-devel
#BuildRequires:  pth-devel
BuildRequires:  libssh2-devel
BuildRequires:  c-ares-devel
BuildRequires:  gettext
#Requires:       pwmd

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
%setup -q -n %{name}-v%{version}

%build
export LDFLAGS=-lgpg-error
./autogen.sh
%configure --disable-static \
           --enable-quality
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc COPYING NEWS README TODO
%{_mandir}/man*/*.*
%{_bindir}/pwmc
%{_libdir}/%{name}.so.*

%files devel
%{_includedir}/*.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}*.pc

%changelog
* Sun Nov 27 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 8.4.2
- Rebuilt for Fedora
* Fri Jul 17 2009 Fabian Affolter <fabian@bernewireless.net> - 6.0.2-1
- Added new -devel package
- Added libssh2-devel as a BR
- Updated to new upstream version 6.0.2
* Sun Apr 19 2009 Fabian Affolter <fabian@bernewireless.net> - 5.0.11-1
- Initial package for Fedora
