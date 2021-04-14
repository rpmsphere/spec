Name: videogen
Version: 0.33
Release: 2.1
Summary: Modelines Generator
License: GPL
Group: System/Configuration/Other
URL: http://www.dynaweb.hu/opensource/videogen
Source: %name-%version.tar.gz

%description
Generates Modelines for the user specified hardware optimized
to the highest possible screen update frequency at a given
resolution.  Can be utilized via both interactive interface
and command line.  Using videogen together with XF86Setup and
xvidtune you can get out all performance your display card
and monitor provides. Now with kernel framebuffer support.

%prep
%setup -q

%build
%make_build CC="gcc %optflags"

%install
install -pD %name %buildroot%_bindir/%name
install -pD %name.1x %buildroot%_mandir/man1/%name.1x

%files
%_bindir/*
%_mandir/man1/*
%doc README CHANGES BUGS THANKS videogen.conf.sample

%changelog
* Tue Apr 19 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.33
- Rebuilt for Fedora
* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2:0.33-alt1.qa1
- NMU: rebuilt for debuginfo.
* Fri Sep 10 2010 Michael Shigorin <mike@altlinux.org> 2:0.33-alt1
- 0.33
* Mon Dec 02 2002 Michael Shigorin <mike@altlinux.ru> 2:0.32-alt1
- 0.32 (NVidia support)
- patch1 not applicable
- spec cleanup
* Sat Nov 02 2002 Dmitry V. Levin <ldv@altlinux.org> 1:0.16-ipl4
- Rebuilt in new environment.
* Mon Apr 15 2002 Rider <rider@altlinux.ru> 1:0.16-ipl3
- rebuild
* Thu Feb 08 2001 Dmitry V. Levin <ldv@fandra.org> 0.16-ipl2
- Fixed group tag.
* Mon Oct 30 2000 Dmitry V. Levin <ldv@fandra.org> 0.16-ipl1
- RE adaptions.
* Thu Oct 28 1999 Dmitry V. Levin <ldv@fandra.org>
- Fandra adaptions.
* Tue Sep 14 1999 Dmitry V. Levin <ldv@fandra.org>
- Initial revision.
