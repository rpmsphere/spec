Name: fbgetty
Version: 0.1.698
Release: 8.1
Summary: Framebuffer getty program
License: GPLv2+
Group: System/Base
URL: https://projects.meuh.org/fbgetty
Source0: https://projects.meuh.org/fbgetty/downloads/fbgetty-%version.tar.bz2
Patch0: fbgetty-0.1.69-login_prompt.patch
Patch1: fbgetty-info.patch
Patch2: fbgetty-0.1.698-stddef.patch

%description
FBgetty is similar to mingetty with framebuffer support.

%package contrib
Summary: Some additional files used with %name
Group: System/Base
Requires: %name = %version-%release

%description contrib
Some additional files used with %name.

%prep
%setup -q
#patch0 -p1
%patch 1 -p1
%patch 2 -p1
sed -i '137,140s|@itemx|@item\n@itemx|' docs/fbgetty.texi

%build
libtoolize -i
%configure
make -i -k

# Fix documentation
mv -f examples/README examples/README_examples

%install
make -i -k install DESTDIR=%{buildroot}
rm %{buildroot}%{_infodir}/dir

%files
%_sbindir/*
%_infodir/*
%_mandir/man8/*
%doc README docs/fbgetty-and-color.txt

%files contrib
%doc contrib/README contrib/rawtoissue.sh examples/issue.* examples/inittab.*
%doc examples/README_examples examples/test/issue.* examples/test/test.sh

%changelog
* Tue Oct 15 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.698
- Rebuilt for Fedora
* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.1.698-alt4.qa1
- NMU: rebuilt for debuginfo.
* Thu Oct 15 2009 Victor Forsyuk <force@altlinux.org> 0.1.698-alt4
- Remove deprecated (by filetriggers) info files handling in installation scripts.
* Tue Oct 24 2006 Victor Forsyuk <force@altlinux.org> 0.1.698-alt3
- Fix build (need to include stddef.h).
* Wed Mar 30 2005 Victor Forsyuk <force@altlinux.ru> 0.1.698-alt2
- Add URL.
- Really install info files (i.e. call install-info).
* Mon Oct 07 2002 Konstantin Volckov <goldhead@altlinux.ru> 0.1.698-alt1
- 0.1.698
- Move fbgetty from /usr/sbin to /sbin
* Tue Mar 05 2002 Konstantin Volckov <goldhead@altlinux.ru> 0.1.69-alt4
- Fixed packaging bug
* Fri Oct 26 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.1.69-alt3
- Fixed login prompt
* Tue Sep 25 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.1.69-alt2
- Fixed filelist bug. Thanks to Alexey Voinov.
* Mon Sep 17 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.1.69-alt1
- First build for Sisyphus
