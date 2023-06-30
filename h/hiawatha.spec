%global __os_install_post %{nil}


Summary:	An advanced and secure webserver for Unix
Name:		hiawatha
Version:	10.12
Release:	1
Source0:	https://www.hiawatha-webserver.org/files/%{name}-%{version}.tar.gz
Source1:	%{name}-sysvscript
License:	GPLv2+
Group:		System Environment/Daemons
URL:		https://www.hiawatha-webserver.org/
BuildRequires:	libxml2-devel
BuildRequires:  libxslt-devel
BuildRequires:  mbedtls-devel
#BuildRequires:	polarssl-devel
BuildRequires:	cmake
BuildRequires:	pkcs11-helper-devel

%description
Hiawatha is an advanced and secure webserver for Unix. It has been written
with 'being secure' as its main goal. This resulted in a webserver which
has for example DoS protection, connection control and traffic throttling.
It has of course also thoroughly been checked and tested for buffer overflows.

%prep
%setup -q
#sed -i -e '/add_subdirectory(polarssl)/d' -e 's| polarssl/include||' -e 's|${POLARSSL_LIBRARY}||' CMakeLists.txt
#sed -i '/^\tpolarssl/d' CMakeFiles.txt

%build
%cmake	-DENABLE_CHROOT:BOOL=ON \
	-DENABLE_MONITOR:BOOL=ON \
	-DUSE_PKCS11_HELPER_LIBRARY:BOOL=ON \
	-DUSE_SYSTEM_MBEDTLS=ON \
	-DCMAKE_SKIP_RPATH:BOOL=OFF \
	-DCMAKE_INSTALL_LOCALSTATEDIR:PATH=/var \
	-DCMAKE_INSTALL_PREFIX:PATH="/usr" \
	-DCMAKE_INSTALL_BINDIR:PATH=%{_bindir} \
	-DCMAKE_INSTALL_SBINDIR:PATH=%{_sbindir} \
	-DCMAKE_INSTALL_SYSCONFDIR:PATH=%{_sysconfdir} \
	-DCMAKE_INSTALL_MANDIR:PATH=%{_mandir}
%cmake_build

%install
%cmake_install
mkdir -p %{buildroot}/var/log/%{name}
install -D -m 644 */logrotate.d/%name %{buildroot}%{_sysconfdir}/logrotate.d/%name
perl -pi -e 's|/usr/var/log/hiawatha/|/var/log/hiawatha/|' %{buildroot}%{_sysconfdir}/%name/hiawatha.conf
install -D -m 755 %{SOURCE1} %{buildroot}%{_initrddir}/%{name}

%files
%dir /var/log/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/*
%{_sbindir}/%{name}
%{_sbindir}/lefh
%{_mandir}/*/*.*
%config(noreplace) %{_sysconfdir}/logrotate.d/%name
%{_localstatedir}/www/%{name}/
%{_initrddir}/%name
%{_bindir}/ssi-cgi
%{_sbindir}/cgi-wrapper
%{_sbindir}/wigwam
%{_libdir}/%{name}

%changelog
* Sun Apr 25 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 10.12
- Rebuilt for Fedora
* Tue Sep 18 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 8.5-1
+ Revision: 817067
- update to 8.5
- use system polarssl library
* Sun Jun 10 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 8.4-1
+ Revision: 804330
- update to 8.4
* Fri May 25 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 8.3-1
+ Revision: 800733
- update to 8.3
* Fri May 04 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 8.2-1
+ Revision: 796129
- update to 8.2
* Sun Feb 26 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 8.1-1
+ Revision: 780912
- update to 8.1
* Thu Feb 02 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 8.0-1
+ Revision: 770756
- update to 8.0
  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild
  + Pixel <pixel@mandriva.com>
    - adapt to %%_localstatedir now being /var instead of /var/lib (#22312)
* Wed Jan 02 2008 Olivier Blin <blino@mandriva.org> 4.3.2-1mdv2008.1
+ Revision: 140747
- restore BuildRoot
  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import hiawatha
* Thu Aug 31 2006 Couriousous <couriousous@mandriva.org> 4.3.2-1mdv2007.0
- 4.3.2
* Sat Apr 15 2006 Couriousous <couriousous@mandriva.org> 4.2-1mdk
- 4.2
- LSB startup script
* Fri Mar 17 2006 Couriousous <couriousous@mandriva.org> 3.6.1-2mdk
- Rebuild
* Sat Oct  1 2005 Couriousous <couriousous@mandriva.org> 3.6.1-1mdk
- 3.6.1
- Some spec fix
* Sun Apr 24 2005 Couriousous <couriousous@mandriva.org> 3.5-1mdk
- 3.5
* Sat Apr 2 2005 Couriousous <couriousous@mandrake.org> 3.4-1mdk
- 3.4
* Wed Dec 1 2004 Couriousous <couriousous@zarb.org> 3.3-1mdk
- 3.3
* Mon Oct 11 2004 Couriousous <couriousous@zarb.org> 3.1-1mdk
- First Mandrakelinux release
