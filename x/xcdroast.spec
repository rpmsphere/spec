Name:           xcdroast
Version:        1.19
Release:        1
License:        GPL-2.0
Summary:        CD-burning software
URL:            http://www.xcdroast.org/
Group:          Productivity/Multimedia/CD/Record
Source0:        https://sourceforge.net/projects/xcdroast/files/%{name}-%{version}.tar.gz/download#/%{name}-%{version}.tar.gz
Patch0:         GUI-sudo.patch
Patch1:         edit_cddb.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gtk2-devel >= 2.24
BuildRequires:  libtool
BuildRequires:  pkgconfig(alsa)
Requires:       wodim
Requires:       genisoimage
Requires:       icedax

%description
X-CD-Roast is a flexible frontend for optical disc authoring.
It combines command line tools like "cdrecord", "cdda2wav", ?readcd"
and "mkisofs" into a nice GTK based graphical user interface.

%prep
%setup -q
# PATCH-ENHANCE-OPENSUSE as there is no gksudo but gnomesu around
%patch0
%patch1

%build
autoreconf --force --install -I m4
CFLAGS="${CFLAGS:-%optflags} -DGKSUDO_BINARY=\\\"/usr/bin/gksudo\\\""
%configure
%make_build

%install
%make_install

mkdir -p %{buildroot}%{_sysconfdir}/permissions.d
cat > %{buildroot}%{_sysconfdir}/permissions.d/xcdroast << EOF
        %{_libexecdir}/%{name}/bin/xcdrwrap     root:cdrom      04755
EOF
cat > %{buildroot}%{_sysconfdir}/permissions.d/xcdroast.paranoid << EOF
        %{_libexecdir}/%{name}/bin/xcdrwrap     root:cdrom      02755
EOF

mkdir -p %{buildroot}%{_datadir}/applications
install -m 0644 extra/xcdroast.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
sed -i 's|/usr/lib|/usr/libexec|' %{buildroot}%{_datadir}/applications/%{name}.desktop
mv %{buildroot}/usr/lib %{buildroot}/usr/libexec

%clean
rm -rf %{buildroot}

%files
%config %{_sysconfdir}/permissions.d/%{name}*
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_libexecdir}/%{name}
%{_mandir}/man1/*
%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo

%changelog
* Thu Oct 17 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 1.19
- Rebuild for Fedora
* Tue Jan 15 2019 Dr. Werner Fink <werner@suse.de>
- Add upstream patch  edit_cddb.patch
  * Fixes some issues when editing CD-Text/CDDB entries in the Write
    CD/DVD menue. Thanks to Mathias Büttner for reporting this problem.
* Mon Nov 12 2018 Dr. Werner Fink <werner@suse.de>
- Update to xcdroast 1.19
  * Add ALSA sound support on Linux.
  * Lots of bugfixes in the audio player.
  * Show all output lines of the tools cdrecord/cdda2wav/mkisofs. In some
    cases the last lines were not displayed before.
  * Merged patch: makefile_destdir.patch (Thanks to 'beachcoder'.)
  * Merged patch: imgfile_case-sensitivity.patch (Thanks to Mathias Büttner.)
  * Merged patch: nocdtextfile.patch (Thanks to Mathias Büttner.)
  * Merged patch: xcdroast-1.18-charsets.diff (Thanks to Georgy Salnikov.)
  * Merged modification of the xcdroast-1.18-charsets.diff patch to simplify
    ISO9660 custom charsets handling.  (Thanks to Mathias Büttner.)
  * Include swedish translation update from Peter Krefting.
- Remove patch imgfile_case-sensitivity.patch and makefile_destdir.patch
  now upstream.
* Tue Jul  3 2018 werner@suse.de
- Add upstream patch imgfile_case-sensitivity.patch
  Match file extensions case insensitive (e.g. .ISO). Thanks to
  Mathias Büttner.
* Tue Feb 27 2018 werner@suse.de
- Smaller fixes as well
* Tue Feb 20 2018 werner@suse.de
- Add patch GUI-sudo.patch to be able to choose e.g. gksudo
  or other tools
* Fri Feb 16 2018 werner@suse.de
- Correct dependencies for cdrecord, mkisofs, and cdda2wav
* Fri Feb 16 2018 werner@suse.de
- Update to xcdroast 1.18
  * Bugfix in configure script
  * Update desktop icon
  * Fix crash when deleting exactly 50 or a multiple of 50 tracks.
  * Change code to use g_io_channels. (Prepare for GTK3)
  * More GTK3 migration.
  * Remove of Mac OS X code since there have been no working cdrtools for
    more than a decade and thus X-CD-Roast cannot be programmed for OS X.
  * Rewrite child processing.
  * More GTK3 migration.
  * Rewrite dialog window placement.
  * Modernize code to display the xcdroast logo (cairo instead of
    pixbuf). Also improve the logo quality.
  * Add About-dialog.
  by Mathias Büttner:
  * Disabled the write mode selector for DVD (and BD) media in "Create"
    and in "Duplicate" menu.
  * Disabled "Do not fixate" for multisession writes (not just a warning).
  * Added fixed settings for nofixate and multisession in "Duplicate" menu
    as they can't be changed there.
  * Updated write mode settings and write options for cdrecord.
  * Fixed displaying wrong Disc size if no Audio CD or Mixed Mode CD.
  * Added notification if CD-Text will not be written.
  * Placed a small logo on top of the sidespace buttons.
  * Amended some of the old tooltips.
  * All terms talking about a CD (Compact Disc) are changed simply to
    the word Disc or CD/DVD/BD where meaningful. (by Mathias Büttner)
  * Resized Dialog windows
  * Removed checks for older cdrecord features
  * Replaced all GtkText by GtkTextView (modernize design)
  * Convert all translation files to UTF-8
  * Replace GtkFileSelection by GtkFileChooser (modernize design)
  * Code cleanup/formatting by Mathias Büttner
  * rename non-root-mode to user-host-mode, as we now always allow
    non-root users to start X-CD-Roast. The user-host-mode just allows to
    configure which user on which host can use X-CD-Roast.
    (e.g. for computer science labs or server installations)
  * detect the suid-bit settings on the cdrtools or the X-CD-Roast wrapper
    and offer a dialog to fix this automatically
  * Changed JEDEC prefixes to decimal and binary prefixes according to
    IEC 60027-2 (January 1999) to avoid confusion. (by Mathias Büttner)
  * Paranoia mode: auto setup of lowest read ahead buffer for each drive
    when scanning for new devices (by Mathias Büttner)
  * wrong cdrtool versions are now reported in a dialog window
    (not just as a warning in the terminal)
  * set suid bit on xcdrwrap on 'make install'
  * Fix various gdk-assertion failures
  * Fix resize of Read/Write progress window
  * Added new checkbox "audio deemphasis" (by Mathias Büttner)
  * Updated gettext to 0.19.7
  * Updated to autoconf 2.69
  * Update to autmake 1.14.1
  * use cddb protocol 6 instead of 1, this fixes also charset problems
  * Compile by default without non-root-mode. Currently I rely on
    that the cdrtools have the suid bit already set.
  * charset conversion from ISO8859-1 to UTF-8 on Album or Track titles.
  * merged in all patches I received and published on my webpage
    since X-CD-Roast 0.98alpha16. - Many thanks to all contributors!
    (parse_version.patch, change_norwegian_locale.txt, io_compile.patch,
    cdda2wav_version.patch, fix_cddb_hidden_tracks.patch, io_progressbar
    _fix.patch, format-security.patch, suid-perms.patch)
  * removed --enable-gtk2 option, this is enabled by default now.
  * Renamed norwegian translation file from "no" to "nb".
  * Updated galician translation.
  * Lots of input and patches and motivation for an updated xcdroast version
    by Mathias Büttner from southwestern Germany:
  * updated CD/DVD writer/reader default settings in setup menu.
  * removed the outdated slider "sectorburst" and added instead
    "size of read ahead buffer" and "minimum overlap of sectors"
    for paranoia mode in the setup menu.
  * added new checkbox "suppress a hidden audio track"
  * fixed info output and track increment in GTK-window
    'Reading audio tracks' for cdda2wav in paranoia mode.
  * changed cdrtools version check to allow only v3.02a09 or higher
    because v3.00a01 - v3.02a07 contain a bug and v2.01 is very outdated
    and may even not compile nowadays.
  * fixed xcdroast's mkisofs version detection since v3.02a01.
  * changed german translation to new orthography.
- Remove paches now solved upstream
  * invalid_mkisofs_version.patch
  * cdda2wav_version.patch
  * io_compile.patch
  * xcdroast.patch
  * cannot_access_cdrecord.patch
  * fix_cddb_hidden_tracks.patch
  * parse_version.patch
  * invalid_cdda2wav_version.patch
* Sun Apr 26 2015 werner@suse.de
- Add some missing patches
* Wed Oct 16 2013 salsergey@gmail.com
- added patches from http://www.xcdroast.org/xcdr098/patches/
* Wed Nov 30 2011 salsergey@gmail.com
- initial version 0.98alpha16
