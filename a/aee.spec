%undefine _auto_set_build_flags
Summary:	An easy to use text editor
Name:		aee
Version:	2.2.15b
Release:	8.1
License:	Artistic
Group:		Editors
URL:		https://mahon.cwx.net/
Source0:	%{name}-%{version}.tar.bz2
Patch0:		%{name}-2.2.15b-mdkconf.patch
Patch1:		%{name}-2.2.15b-fix-str-fmt.patch
BuildRequires:	libX11-devel

%description
An easy to use text editor. Intended to be usable with little or no
instruction. Provides both a terminal (curses based) interface and native
X-Windows interface (in which case the executable is called xae). Features
include pop-up menus, journalling (to recover from system crash or loss of
connection), cut-and-paste, multiple buffers (associated with files or not),
and much more.

%prep
%setup -q
%patch0 -p1 -b .peroyvind
%patch1 -p1 -b .strfmt
sed -i 's|-s|-Wl,--allow-multiple-definition|' create.mk.*

%build
make both OPTFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -m755 %{name} -D $RPM_BUILD_ROOT%{_bindir}/%{name}
install -m755 xae -D $RPM_BUILD_ROOT%{_bindir}/xae
install -m644 %{name}.1 -D $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1
install -m644 help.ae -D $RPM_BUILD_ROOT%{_datadir}/%{name}/help.ae
cd $RPM_BUILD_ROOT/usr/bin
ln -s aee $RPM_BUILD_ROOT%{_bindir}/rae
ln -s xae $RPM_BUILD_ROOT%{_bindir}/rxae

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc Artistic README.aee aee.1.ps aee.i18n.guide keypad
%{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/help.ae
%{_mandir}/man1/*

%changelog
* Fri Mar 23 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 2.2.15b
- Rebuilt for Fedora
* Wed Feb 02 2011 Funda Wang <fwang@mandriva.org> 2.2.15b-7mdv2011.0
+ Revision: 634993
- rebuild
- tighten BR
* Wed Jun 10 2009 JĂŠrĂ´me Brenier <incubusss@mandriva.org> 2.2.15b-6mdv2011.0
+ Revision: 384638
- fix str fmt (1 patch)
* Thu Jun 19 2008 Thierry Vignaud <tv@mandriva.org> 2.2.15b-5mdv2009.0
+ Revision: 226131
- rebuild
* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 2.2.15b-4mdv2008.1
+ Revision: 135817
- restore BuildRoot
  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - buildrequires X11-devel instead of XFree86-devel
    - import aee
* Tue Jun 27 2006 Lenny Cartier <lenny@mandriva.com> 2.2.15b-4mdv2007.0
- rebuild
* Wed May 11 2005 Lenny Cartier <lenny@mandriva.com> 2.2.15b-3mdk
- rebuild
* Mon Jan 05 2004 Per Řyvind Karlsen <peroyvind@linux-mandrake.com> 2.2.15b-2mdk
- don't do rm -rf $RPM_BUILD_ROOT in %%prep
- cosmetics
- compile with $RPM_OPT_FLAGS (P0)
- move help file into %%{_datadir}/%%{name} (P0)
* Thu Sep 04 2003 Olivier Thauvin <thauvin@aerov.jussieu.fr> 2.2.15b-1mdk
- 2.2.15b
* Wed Apr 30 2003 Olivier Thauvin <thauvin@aerov.jussieu.fr> 2.2.15a-2mdk
- distlint fix
- Buildrequires
* Sun Dec 29 2002 Olivier Thauvin <thauvin@aerov.jussieu.fr> 2.2.15a-1mdk
- 2.2.15a
- reintroduce in contrib
*Thu Nov 15 2001 Lenn Cartier <lenny@mandrakesoft.com> 2.2.12a-1mdk
- 2.2.12a
* Tue Jun 26 2001 Lenny Cartier <lenny@mandrakesoft.com> 2.2.9-1mdk
- updated to 2.2.9
- fix url
* Tue Feb 27 2001 Lenny Cartier <lenny@mandrakesoft.com> 2.2.7-1mdk
- updated to 2.2.7
* Thu Jan 04 2001 Lenny Cartier <lenny@mandrakesoft.com> 2.2.3-1mdk
- upgraded to 2.2.3
* Wed Jul 26 2000 Lenny Cartier <lenny@mandrakesoft.com> 2.2.1-1mdk
- upgraded to v2.2.1
- BM
- macros
* Thu Apr 20 2000 Lenny Cartier <lenny@mandrakesoft.com> 2.2.0-2mdk
- fix group
* Tue Jan 25 2000 Lenny Cartier <lenny@mandrakesoft.com>
- build for mandrake
* Mon Jan 11 1999 Ryan Weaver <ryanw@infohwy.com>
  [aee-2.2.0-1]
- First RPM.
- Patch to move help files, etc. from /usr/local/lib to /usr/lib/aee
