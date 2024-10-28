Name:           pavuk
#BuildRequires:  dante-devel
#BuildRequires:  libdb-devel
BuildRequires:  gtk2-devel
BuildRequires:  openssl-devel
BuildRequires:  desktop-file-utils
Version:        0.9.35
Release:        7.1
URL:            https://pavuk.sourceforge.net/
Summary:        Powerful WWW or FTP Site Mirror Tool
License:        GPL-2.0+
Group:          Productivity/Networking/Web/Utilities
Source0:        %{name}-%{version}.tar.bz2
Source1:        %{name}.desktop
Patch1:         pavuk-ld-add-needed.patch
Patch2:         pavuk-nossl2.patch
Patch3:         pavuk-bugs.patch

%description
Pavuk is used to download or mirror Web sites or files. It transfers
document from HTTP, FTP, Gopher, and optionally from HTTPS (HTTP over
SSL) servers. An optional GTK GUI allows easy configuration. Many
options allow fine-tuning for the usage scenario. This is a tool for
experts and much too complicated for beginners.

Authors:
--------
    Ondrejicka Stefan <ondrej@idata.sk>

%prep
%setup -q
%patch 1
%patch 2 -p1
%patch 3 -p1

%build
CXXFLAGS="$RPM_OPT_FLAGS -DNDEBUG -Wall" \
%configure --enable-debug
make %{?jobs:-j%jobs}

%install
make DESTDIR=$RPM_BUILD_ROOT GNOME_PREFIX=/var/tmp install
rm -rf $RPM_BUILD_ROOT/var/tmp # gnome unwanted
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}
install -m 644 pavukrc.sample $RPM_BUILD_ROOT%{_sysconfdir}/pavukrc
rm -f $RPM_BUILD_ROOT/usr/info/dir.bak.gz
%find_lang %name
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
cp $RPM_BUILD_ROOT%{_datadir}/icons/pavuk_32x32.xpm \
   $RPM_BUILD_ROOT%{_datadir}/pixmaps/pavuk.xpm
rm -f $RPM_BUILD_ROOT%{_datadir}/icons/pavuk*
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

%files -f %name.lang
%config %{_sysconfdir}/pavukrc
%doc AUTHORS BUGS COPYING CREDITS ChangeLog MAILINGLIST NEWS README TODO wget-pavuk.HOWTO
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*.desktop

%changelog
* Mon Apr 13 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.35
- Rebuilt for Fedora
* Sun Apr 27 2014 crrodriguez@opensuse.org
- pavuk-nossl2.patch: fix build without SSLv2
- pavuk-bugs.patch previous patch was not enough to make it
  compile successfully, fixes open() arguments and a typo.
* Wed Dec 21 2011 coolo@suse.com
- remove call to suse_update_config (very old work around)
* Mon Sep 12 2011 massing@simula.no
- Added ld-add-patch
* Sat Jan  2 2010 vuntz@opensuse.org
- Change gtk1-compat-devel BuildRequires to gtk2-devel: it has been
  ported to GTK+ 2.x a while ago.
- Add missing BuildRequires for some features: dante-devel,
  db-devel, libopenssl-devel.
* Thu Jul 19 2007 mkudlvasr@suse.cz
- update to 0.9.35
  highlights from changelog
  - security fixes
  - minor bug fixes
* Tue Jan  9 2007 prusnak@suse.cz
- fixed pavuk.desktop file [#231755]
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Mon Jan 16 2006 mjancar@suse.cz
- update to 0.9.34
* Mon Sep 26 2005 sbrabec@suse.cz
- Force gtk2 using gtk1-compat-devel.
* Wed Aug  3 2005 mjancar@suse.cz
- update to 0.9.32
- drop obsolete patches:
  * pavuk-0.9pl30b-buffer-overflow.diff
* Tue Jul 13 2004 mjancar@suse.cz
- update to 0.9pl30b
- kill obsolete patches
- fix buffer overflow (#42141, #42764)
* Mon Jun 21 2004 mjancar@suse.cz
- fix buffer overflow (#42141)
- enable the spelling error fix
* Sat Jan 10 2004 adrian@suse.de
- build as user
* Mon Aug 25 2003 mjancar@suse.cz
- fix spelling error in pavukrc (#27733)
* Fri Aug 15 2003 adrian@suse.de
- add desktop file
* Fri Jul 11 2003 meissner@suse.de
- run suse_update_config.
* Mon Jun 16 2003 coolo@suse.de
- use BuildRoot
* Mon Mar 18 2002 uli@suse.de
- build with --enable-debug to allow fine-tuning (bug #15105)
* Mon Mar  4 2002 uli@suse.de
- commented out entries in pavukrc that require customization
  (bug #13977)
* Wed Aug 15 2001 uli@suse.de
- update -> 0.9pl28
* Tue Jul 24 2001 uli@suse.de
- update -> 0.9pl27
* Wed May  9 2001 mfabian@suse.de
- bzip2 sources
* Wed Apr 18 2001 uli@suse.de
- more 64 bit fixes
* Thu Mar 29 2001 uli@suse.de
- fixed for gcc >2.95
- 64 bit fixes
* Mon Nov  6 2000 ro@suse.de
- fixed neededforbuild
* Wed Jun  7 2000 ro@suse.de
- doc relocation
* Sun Mar  5 2000 olh@suse.de
- New version 0.9pl23, move manpages
* Fri Jan 14 2000 uli@suse.de
- New version 0.9pl23
* Tue Oct 26 1999 uli@suse.de
- New version 0.9pl21
* Fri Sep 17 1999 kettner@suse.de
- Reinserted old # Commandline: line.
* Mon Sep 13 1999 bs@suse.de
- ran old prepare_spec on spec file to switch to new prepare_spec.
* Tue Jul 13 1999 bs@suse.de
- use gtk and glib instead of gtkn and glibn
* Thu Jul  8 1999 uli@suse.de
- Spec file created from pavuk-0.9pl17.tgz by autospec
