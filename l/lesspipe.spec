Name:           lesspipe
Version:        1.83
Release:        1
Summary:        Input Filter for the Pager "less"
License:        GPL-2.0+
Group:          System/Console
URL:            http://www-zeuthen.desy.de/~friebel/unix/lesspipe.html
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildArch:      noarch

%description
The script runs under a ksh compliant shell (ksh, bash, zsh) and allows
to view files with binary content, compressed files, archives and files
contained in archives. A large and growing number of formats are
supported both as plain and compressed files using compress, gzip,
bzip2 or zip. Lesspipe has colorizing support for the languages ada,
asm, awk, c, c++, groff, html, xml, java, javascript, lisp, m4, make,
pascal, patch, perl, povray, python, ruby, shellscript and sql.

%prep
%setup -q

%build
./configure --yes --prefix=%{_prefix}

%install
install -Dpm 0755 code2color %{buildroot}%{_bindir}/code2color
install -Dpm 0755 lesspipe.sh %{buildroot}%{_bindir}/lesspipe
install -Dpm 0755 sxw2txt %{buildroot}%{_bindir}/sxw2txt
install -Dpm 0644 lesspipe.1 %{buildroot}%{_mandir}/man1/lesspipe.1

%files
%doc COPYING ChangeLog README TODO german.txt contrib/less_wrapper
%{_bindir}/code2color
%{_bindir}/lesspipe
%{_bindir}/sxw2txt
%doc %{_mandir}/man1/lesspipe.1.*

%changelog
* Mon Oct 07 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 1.83
- Rebuilt for Fedora
* Sun Sep  9 2012 asterios.dramis@gmail.com
- Rearranged runtime dependencies based on the respective packages'
  availability in openSUSE, Packman and OBS.
* Wed Jul 18 2012 asterios.dramis@gmail.com
- Replaced djvu runtime requirement with the correct djvulibre.
- Removed ppthtml runtime requirement (it is provided by the already required
  xlhtml package).
* Wed Jul 18 2012 asterios.dramis@gmail.com
- Removed perl-Storable runtime requirement (it is provided by the already
  required perl package).
* Sun Jul 15 2012 asterios.dramis@gmail.com
- Rearranged runtime dependencies based on the respective packages'
  availability in openSUSE, Packman and OBS.
* Fri Jul 13 2012 asterios.dramis@gmail.com
- Update to 1.72:
  * Detect proper options for the file command at runtime.
  * Guess the character encoding and optionally do a char conversion.
  * Make colored ls output working for different OS flavours.
  * Do not interpret files with an extension .xml as html files.
  * eval `.../lesspipe.sh` will set LESS_ADVANCED_PREPROCESSOR if meaningful.
  * Sample less wrapper to open URLs with less (in contrib).
- Changed License to GPL-2.0+ (SPDX style).
* Wed Feb  9 2011 asterios.dramis@gmail.com
- update to 1.71
  - detect a good version of tar, try to avoid /usr/bin/tar on Solaris (Jim
Pryor)
  - do more preprocessing if LESS_ADVANCED_PREPROCESSOR is set
  - always try to interpret (g)roff formatted text (man pages)
  - better detection of lzip and xz compressed files (Vincent Lefèvre)
  - do not call identify for 'image text' tagged files (Vincent Lefèvre)
  - do not rely on contents of LANG variable for calling iconv (Vincent Lefèvre)
  - have a fallback to bash or zsh for the shell used at runtime (Vincent
Lefèvre)
  From version 1.70
  - fixing the call of mktemp on MacOS (reported by Peter Kostka and Martin
Otte)
  - detect helper programs at runtime (suggested by David Leverton, Petr Uzel)
  - add support for xz compression (Mathieu Bouillaguet)
  - more stringent tests for gzip compression
  - changes in rpm processing to better support MacOSX and BSD based systems
  - introduce --fixed in configure to statically control lesspipe generation
  - improved generation of Makefile
  - calling eval `.../lesspipe.sh` will set the ENV variable LESSOPEN properly
  - fixing jar processing if not using fastjar (was a bug in 1.60 only)
  - control amount of preprocessing by the ENV var LESS_ADVANCED_PREPROCESSOR
if the related configure question is answered with y (default n) (Petr Uzel)
  - updated documentation to reflect recent changes
- Spec file updates:
  - Changes based on rpmdevtools templates and spec-cleaner run.
  - Removed all Requires: entries and used #Recommends: or #Suggests: for package
requirements (also added more packages).
  - Removed "make" from the %%build section (not needed).
  - Removed the %%changelog entries from the spec file.
* Tue Apr 21 2009 puzel@suse.cz
- update to 1.60
  - major restructuring of code, support for even more file types
  - using a temp dir and mktemp for creating temporary files
  - concentrate file type recognition in a function
  - rewritten the recognition and processing of html files, added xhtml
recognition, add elinks and w3m as html parsers
  - better support for jar files (recognized by extension jar and xpi)
  - support for excel and powerpoint files (recognized by extension)
  - support for perl pod files
  - colored directory listings
  - list and view the control parts of *.deb packages
  - added support for lzip compression (Antonio Diaz Diaz)
  - added support for DjVu files (Florian Cramer)
  - improved zip support for Solaris, bug fixes in configure (Paul Townsend)
  - code cleanup and bug fixes in lesspipe based on the restructured code
  - enhanced test suite
  - update of the documentation (merged english.txt and README)
* Mon Sep  1 2008 mjung@suse.de
- corrected specfile and created changes (thank you darix)
* Wed Aug 27 2008 mjung@suse.de
- initial package
