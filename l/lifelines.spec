Name:           lifelines
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  docbook-utils
BuildRequires:  dos2unix
BuildRequires:  libjpeg-devel
BuildRequires:  libpng
BuildRequires:  libxslt-devel
BuildRequires:  ncurses-devel
BuildRequires:  perl-XML-DOM
BuildRequires:  perl-XML-Parser
BuildRequires:  perl-XML-SAX
BuildRequires:  perl-libwww-perl
BuildRequires:  texlive-latex
BuildRequires:  texlive-jadetex
BuildRequires:  texlive-xmltex
BuildRequires:  tidy
BuildRequires:  w3m
URL:            https://lifelines.sourceforge.net/
Version:        3.0.62
Release:        136.1
Summary:        A terminal based Genealogy Program
License:        MIT
Group:          Productivity/Scientific/Other
Source:         https://download.sourceforge.net/lifelines/lifelines-3.0.62.tar.bz2
Source1:        sh.rellink
Patch:          lifelines-3.0.62.dif
Patch1:         lifelines-3.0.59-funcptr.dif
Patch2:         lifelines-3.0.60-array.dif
%global         _sysconfdir /etc
%global         ncursesw_config %(set -- %{_bindir}/ncursesw*-config; echo ${1})

%description
Lifelines is terminal-based program that allows the tracking of
genealogical information. The lifelines reports are the power of the
system but requires knowledge in the ll format.

Authors:
--------
    Tom Wetmore <ttw@shore.net>
    Matt Emmerton <matt@gsicomp.on.ca>
    Rob Fugina <robf@geekthing.com>
    Paul B. McBride <pbmcbride@rcn.com>
    Marc Nozell <marc@nozell.com>
    Perry Rapp <prapp@erols.com>
    Petter Reinholdtsen <pere@hungry.com>

%prep 
%setup -q
%patch  -p 0
#patch1 -p 0
%patch2 -p 0

%build
CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing -Wno-format-security -pipe $(%{ncursesw_config} --cflags)"
CPPFLAGS="-D_GNU_SOURCE -D_XOPEN_CURSES"
CC=gcc
export CC CFLAGS CPPFLAGS
autoreconf -fi
./configure --prefix=%{_prefix} -exec-prefix=%{_prefix}	\
	    --libexecdir=%{_libdir}		\
	    --sysconfdir=%{_sysconfdir}		\
	    --libdir=%{_libdir}			\
	    --mandir=%{_mandir}			\
	    --infodir=%{_infodir}		\
	    --disable-rpath			\
	    --with-gnu-ld			\
	    --with-docs				\
	    --without-included-gettex		\
	    --with-libintl-prefix=%{_prefix}	\
	    --with-included-gettext=%{_prefix}
make
#chmod 644 docs/*.1
#rm -f docs/*.pdf
make -C docs/

%install
. %{S:1}
make DESTDIR=%{buildroot}			\
     docdir=%{_defaultdocdir}/lifelines/doc	\
     pkgdatadir=%{_defaultdocdir}/lifelines/doc	\
     install
make -C docs/ DESTDIR=%{buildroot}		\
     docdir=%{_defaultdocdir}/lifelines/doc	\
     pkgdatadir=%{_defaultdocdir}/lifelines/doc	\
     install    
mkdir -p %{buildroot}%{_mandir}/man1
install -m 644 docs/*.1 %{buildroot}%{_mandir}/man1/
mkdir -p %{buildroot}%{_datadir}/lifelines/reports/st
install -m 644 reports/*.l[li]    %{buildroot}%{_datadir}/lifelines/reports/
install -m 644 reports/st/*.l[li] %{buildroot}%{_datadir}/lifelines/reports/st/
mkdir -p %{buildroot}%{_datadir}/lifelines/tt
install -m 644 tt/*.tt  %{buildroot}%{_datadir}/lifelines/tt/
mkdir -p %{buildroot}%{_defaultdocdir}/lifelines/reports
install -m 644 reports/CREDIT %{buildroot}%{_defaultdocdir}/lifelines/reports/
install -m 644 reports/index.html reports/boc.gif reports/ll.png %{buildroot}%{_defaultdocdir}/lifelines/reports/
install -m 644 README ChangeLog NEWS AUTHORS LICENSE %{buildroot}%{_defaultdocdir}/lifelines/
rm -f  %{buildroot}%{_defaultdocdir}/lifelines/doc/*.l[li]
path=$(relpath %{buildroot}%{_datadir}/lifelines/reports %{buildroot}%{_defaultdocdir}/lifelines/doc)
for l in %{buildroot}%{_datadir}/lifelines/reports/*.l[li] ; do
    ln -sf ${path}/${l##*/} %{buildroot}%{_defaultdocdir}/lifelines/doc/
done
rm -f  %{buildroot}%{_defaultdocdir}/lifelines/doc/{README,NEWS,LICENSE,CREDIT,AUTHORS}
rm -f  %{buildroot}%{_defaultdocdir}/lifelines/doc/{INSTALL,README.MAINTAINERS.win32}
if test -e %{buildroot}%{_defaultdocdir}/lifelines/doc/.linesrc ; then
    mv %{buildroot}%{_defaultdocdir}/lifelines/doc/.linesrc \
       %{buildroot}%{_defaultdocdir}/lifelines/doc/dot.linesrc
fi
if test -e %{buildroot}%{_defaultdocdir}/lifelines/doc/lines.cfg ; then
    mv %{buildroot}%{_defaultdocdir}/lifelines/doc/lines.cfg \
       %{buildroot}%{_defaultdocdir}/lifelines/doc/lines.cfg.tmp
    dos2unix -n %{buildroot}%{_defaultdocdir}/lifelines/doc/lines.cfg.tmp \
                %{buildroot}%{_defaultdocdir}/lifelines/doc/lines.cfg
    rm -f %{buildroot}%{_defaultdocdir}/lifelines/doc/lines.cfg.tmp
fi
%find_lang %name

%files -f %{name}.lang
%doc %{_defaultdocdir}/lifelines
%{_prefix}/bin/*
%{_datadir}/lifelines
%doc %{_mandir}/man1/*.gz

%changelog
* Thu Feb 28 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 3.0.62
- Rebuilt for Fedora
* Tue Jul 24 2012 werner@suse.de
- Add missing font
* Tue Jul 10 2012 werner@suse.de
- Make it build with latest TeXLive 2012 with new package layout
* Wed Dec 21 2011 coolo@suse.com
- remove call to suse_update_config (very old work around)
* Fri Dec  2 2011 coolo@suse.com
- add automake as buildrequire to avoid implicit dependency
* Wed Jul  8 2009 coolo@novell.com
- fix build with automake 1.11
* Mon May  5 2008 werner@suse.de
- Reqiures also xmltex
* Thu Apr 10 2008 werner@suse.de
- Changes for new ncurses header location
* Tue Mar 25 2008 werner@suse.de
- Work around missing LaTeX format for JadeTeX
* Fri Dec 14 2007 werner@suse.de
- Update to lifelines 3.0.62
  * Fix encoding conversion for GEDCOM, pedigree, and GEDCOM modes
  * Improved German translation
  * Improvements to configure finding curses
  * More strings made ready for internationalization
  * Minor doc tweaks, and packaging tweaks for Debian
* Wed Aug  1 2007 werner@suse.de
- Update to lifelines 3.0.60: Fixes a lot of documentation
- Avoid broken brp-symlink check
- Avoid some RPMlint warnings
* Thu Jun 21 2007 werner@suse.de
- Update to lifelines 3.0.59: Is able to handle UTF-8
* Sun Apr 22 2007 ro@suse.de
- use texlive for building
* Fri Mar 30 2007 rguenther@suse.de
- Add bison and ncurses-devel BuildRequires.
* Sat Oct 21 2006 schwab@suse.de
- Properly use autoreconf.
* Thu Jun 22 2006 ro@suse.de
- remove selfprovides
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Mon Jan 23 2006 werner@suse.de
- Fix array subscript number (bug #144800)
* Fri Sep 30 2005 werner@suse.de
- Update to lifelines 3.0.46.1 to get it work even with ncurses 5.4
* Thu Sep 29 2005 werner@suse.de
- Re-enable traditional address handling (-fno-strict-aliasing)
* Wed Jun 22 2005 ke@suse.de
- Add docbook-dsssl-stylesheets to neededforbuild and enable building
  docs.
* Tue Jun 14 2005 werner@suse.de
- New package: lifelines, a genealogy program
