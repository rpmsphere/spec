Name:           userinfo
Version:        2.5
Release:        1
Summary:        Console Utility to Display Local User Information
Source:         http://prdownloads.sourceforge.net/userinfo/userinfo-%{version}.tar.gz
URL:            http://benkibbey.wordpress.com/userinfo/
Group:          System/Base
License:        GNU General Public License version 2 or later (GPLv2 or later)
BuildRequires:  make gcc glibc-devel
BuildRequires:  autoconf automake libtool

%description
Userinfo is a console utility to display a variety of information about a local
user.

It uses loadable modules to perform different tasks which separate the output
with a field deliminator. Some may find it useful in shell scripts to gather
information which might be tedious by other methods.

%prep
%setup -q

%build
%configure --disable-debug
%__make %{?_smp_flags}

pushd contrib
%__cc %{optflags} -shared -fPIC -o kill.so kill.c
popd

%install
%__rm -rf "$RPM_BUILD_ROOT"
make DESTDIR=$RPM_BUILD_ROOT install
%__rm "$RPM_BUILD_ROOT%{_libdir}/userinfo"/*.la
%__install -m 0755 contrib/kill.so "$RPM_BUILD_ROOT%{_libdir}/userinfo/"

%clean
%__rm -rf "$RPM_BUILD_ROOT"

%files
%doc ChangeLog KnownBugs NEWS README doc/README.modules doc/uirc
%doc contrib/lastusers.sh
%{_bindir}/ui
%dir %{_libdir}/userinfo
%{_libdir}/userinfo/login.so
%{_libdir}/userinfo/mail.so
%{_libdir}/userinfo/passwd.so
%{_libdir}/userinfo/kill.so
%doc %{_mandir}/man1/ui.1.*

%changelog
* Tue Oct 08 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 2.5
- Rebuild for Fedora
* Sun Jan 16 2011 pascal.bleser@opensuse.org
- moved to OBS
- update to 2.3:
  * utmp[x] portability fixes
  * safer strncat usage
  * showing dead logins of utmpx output was fixed
* Sun Mar 18 2007 guru@unixtech.be
- new upstream version
- CHANGES: follow symbolic links option was changed from -l to -L
- CHANGES: user idle time from the login module is displayed as seconds rather than minutes
* Sat Apr 22 2006 guru@unixtech.be
- rewrote spec file
* Sun Jul 31 2005 guru@unixtech.be
- version 2.1
