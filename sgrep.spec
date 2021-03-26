Name:           sgrep
Version:        1.94a
Release:        1944.7
Summary:        Searching for Structured Patterns
License:        GPL-2.0-or-later
Group:          Productivity/Text/Utilities
URL:            https://www.cs.helsinki.fi/~jjaakkol/sgrep.html
Source:         https://fossies.org/linux/misc/old/%{name}-%{version}.tar.gz
Patch0:         sgrep-sgreprc.diff

%description
Sgrep is like "grep" but it will also work for structured patterns. You can
use the program to extract fragments from SGML/XML or any other well formed
text files (including UTF-8 encoded files).

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install
install -Dpm 0644 sample.sgreprc \
  %{buildroot}/%{_sysconfdir}/sgreprc
rm %{buildroot}%{_datadir}/sample.sgreprc

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README sgrep.lsm
%doc sample.sgreprc
%config %{_sysconfdir}/sgreprc
%{_bindir}/sgrep
%{_mandir}/man1/sgrep.1*

%changelog
* Tue Sep 29 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 1.94a
- Rebuild for Fedora
* Thu Apr 16 2020 Martin Pluskal <mpluskal@suse.com>
- Update to version 1.94a:
  * Killed nasty hash_function() bug
    + Killed nasty postings entry bug when posting was > 0xfffffff
  * Bumped hash table size up
  * Newer automake & autoconf files
- Changes for version 1.93a:
  * Fixed a bug which caused sgrep to dump core when using SGML
    scanner at least on Solaris platform (negative index to memory
    mapped file)
  * Fixed a bug which caused sgrep to  ignore '-n' command line
    option always.
- Drop no longer needed sgrep-no-build-date.patch
- Use alternative source url as official one is broken
* Sat Feb 25 2012 coolo@suse.com
- sync spec file name with package name
* Tue Aug 31 2010 cristian.rodriguez@opensuse.org
- Do not provide build date in binaries
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Tue Nov 15 2005 ke@suse.de
- Add -fno-strict-aliasing.
* Fri Oct 24 2003 ke@suse.de
- Fix sample.sgreprc.
- Don't Require tk (sgtool.tcl) were dumped.
- Use norootforbuild.
- Use DESTDIR.
* Mon May 26 2003 ke@suse.de
- Cleanup $RPM_BUILD_ROOT for packaging purposes.
* Tue Sep 17 2002 ro@suse.de
- removed bogus self-provides
* Fri Nov 17 2000 ke@suse.de
- cleanup spec file; use macros, add group tag (#4246).
* Fri Mar  3 2000 uli@suse.de
- moved man page to %%{_mandir}
* Mon Sep 13 1999 bs@suse.de
- ran old prepare_spec on spec file to switch to new prepare_spec.
* Fri Jan 15 1999 ke@suse.de
- update: version 1.92a.
* Mon Nov 24 1997 ro@suse.de
- changes /usr/X11/bin to /usr/X11R6/bin
* Thu Aug 14 1997 Karl Eichwalder  <ke@suse.de>
  * initial package: version 0.99
