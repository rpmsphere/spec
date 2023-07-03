Summary: Create DOS/MS-compatible boot records
Name: ms-sys
Version: 2.8.0
Release: 1
License: GPL
Group: Applications/System
URL: https://ms-sys.sourceforge.net/
Source: https://dl.sf.net/ms-sys/ms-sys-%{version}.tar.gz
BuildRequires: bash
BuildRequires: gettext

%description
This program is used to create DOS/MS-compatible boot records. It is
able to do the same as Microsoft "fdisk /mbr" to a hard disk. It is
also able to do the same as DOS "sys" to a floppy or FAT32 partition
except that it does not copy any system files, only the boot record is
written.

%prep
%setup -q

%build
%{__make}  \
    CC="${CC:-%{__cc}}" \
    EXTRA_CFLAGS="%{optflags} -fasm" \
    EXTRA_LDFLAGS="%{optflags}" \
    PREFIX="%{_prefix}" \
    SHELL="/bin/bash"

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR="$RPM_BUILD_ROOT" PREFIX="%{_prefix}" MANDIR="%{_mandir}"
%find_lang %{name}

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%doc CHANGELOG CONTRIBUTORS COPYING FAQ README TODO
%{_mandir}/man1/ms-sys.1*
%{_mandir}/*/man1/ms-sys.1*
%{_bindir}/ms-sys

%changelog
* Sun Oct 09 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 2.8.0
- Rebuilt for Fedora
* Wed Jan 26 2011 Dag Wieers <dag@wieers.com> - 2.2.1-1
- Updated to release 2.2.1.
* Fri May 14 2010 Dag Wieers <dag@wieers.com> - 2.2.0-1
- Updated to release 2.2.0.
* Sun Mar 21 2010 Dag Wieers <dag@wieers.com> - 2.1.5-1
- Updated to release 2.1.5.
* Thu Oct 22 2009 Dag Wieers <dag@wieers.com> - 2.1.4-1
- Updated to release 2.1.4.
* Mon Dec 31 2007 Dag Wieers <dag@wieers.com> - 2.1.3-1
- Updated to release 2.1.3.
* Sat Nov 26 2005 Dag Wieers <dag@wieers.com> - 2.1.2-1
- Updated to release 2.1.2.
* Thu Aug 04 2005 Dag Wieers <dag@wieers.com> - 2.1.1-1
- Updated to release 2.1.1.
* Sun Jun 06 2004 Dag Wieers <dag@wieers.com> - 2.0.0-1
- Updated to release 2.0.0.
* Mon Mar 22 2004 Dag Wieers <dag@wieers.com> - 1.0.2-1
- Initial package. (using DAR)
