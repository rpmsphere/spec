Name:           nted
Version:        1.10.18
Release:        24.4
Summary:        Musical score editor
Group:          Applications/Publishing
License:        GPLv2+ and GFDL
URL:            https://vsr.informatik.tu-chemnitz.de/staff/jan/nted/nted.xhtml
Source0:        https://vsr.informatik.tu-chemnitz.de/staff/jan/nted/sources/nted-%{version}.tar.gz
Source1:        nted.desktop
BuildRequires:  gtk2-devel alsa-lib-devel
BuildRequires:  gettext yelp xmlto desktop-file-utils
BuildRequires:  fontpackages-devel >= 1.18
BuildRequires:  fontpackages-filesystem
BuildRequires:  qca2 baloo

%description
NtEd is a GTK score editor. It intends to be really WYSIWYG: what you
see on the screen is exactly what you get on printer output. It
supports up to 4 voices per staff, drum notes, 5 lyrics lines,
N-Tuplets, context changes, repeats with alternatives, configurable
music instruments per staff, MIDI and Postscript export, MusicXML
import. Scores can be played through the ALSA sequencer.

%prep
%setup -q
sed -i '1i #include <cstring>' dynarray.h
sed -i 's|HALF_COLOR 0.0|HALF_COLOR 0|' idiotseditor/idiotseditor.cpp
sed -i '1372s|< 0|== NULL|' voice.cpp

%build
%configure --docdir='%{_docdir}/%{name}-doc-%{version}'
sed -i 's|-Werror=format-security|-fpermissive -Wno-narrowing|' Makefile */Makefile
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
mv %{buildroot}%{_docdir}/%{name}-doc-%{version} docs

# Upstream desktop file contains some blank keys and is not spec-compliant
rm %{buildroot}%{_datadir}/applications/nted.desktop
desktop-file-install --vendor="" \
  --dir=%{buildroot}%{_datadir}/applications \
  %{SOURCE1}
%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%doc COPYING COPYING.GFDL
%{_bindir}/nted
%{_datadir}/applications/nted.desktop
%{_datadir}/pixmaps/nted.png
%{_datadir}/%{name}
%{_mandir}/*/*
%doc COPYING.GFDL docs/* COPYING COPYING.FONT.TXT

%changelog
* Wed Nov 13 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.10.18
- Rebuilt for Fedora
* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.10.18-3
- Rebuild for new libpng
* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild
* Fri Jan 28 2011 Hans Ulrich Niedermann <hun@n-dimensional.de> - 1.10.18-1
- Update to 1.10.18 (#673122).
* Tue Jan 25 2011 Hans Ulrich Niedermann <hun@n-dimensional.de> - 1.10.17-1
- Update to 1.10.17 (#625397).
* Wed Jul 21 2010 Hans Ulrich Niedermann <hun@n-dimensional.de> - 1.10.13-1
- Update to 1.10.13 (#616739).
* Fri Jul 16 2010 Hans Ulrich Niedermann <hun@n-dimensional.de> - 1.10.12-2
- Added License tags for -doc, -fonts subpackages.
- Added COPYING and COPYING.FONT.TXT (GPL w/ font exception) to fonts subpkg.
- Removed COPYING (GPL) from -doc subpkg (contains only GFDL files).
* Fri Jul 16 2010 Hans Ulrich Niedermann <hun@n-dimensional.de> - 1.10.12-1
- Update to 1.10.12 (#578125).
* Thu Apr 29 2010 Hans Ulrich Niedermann <hun@n-dimensional.de> - 1.10.3-2
- Repeat build with the sourc tarball actually uploaded
* Wed Apr 28 2010 Hans Ulrich Niedermann <hun@n-dimensional.de> - 1.10.3-1
- Update to 1.10.3 (support tremolo notes)
* Mon Apr 26 2010 Hans Ulrich Niedermann <hun@n-dimensional.de> - 1.10.1-1
- Update to 1.10.1
* Mon Apr 26 2010 Hans Ulrich Niedermann <hun@n-dimensional.de> - 1.9.22-1
- Update to 1.9.22 (bug fixes, mostly Lilypond export)
* Tue Mar 30 2010 Hans Ulrich Niedermann <hun@n-dimensional.de> - 1.9.19-1
- Update to 1.9.19 (time signature fixes)
- Remove upstreamed nted-1.9.18-link-fix-for-fedora.patch
* Wed Feb 10 2010 Hans Ulrich Niedermann <hun@n-dimensional.de> - 1.9.18-2
- Explicitly check for and link against libX11 (will be in upstream 1.9.19)
- Remove obsolete "chmod -x" on dynarray.h
- Update nted.desktop translations from upstream's nted.desktop
* Wed Feb 10 2010 Hans Ulrich Niedermann <hun@n-dimensional.de> - 1.9.18-1
- Update to 1.9.18
* Thu Jan 21 2010 Hans Ulrich Niedermann <hun@n-dimensional.de> - 1.9.17-1
- Update to 1.9.17
* Thu Dec 24 2009 Hans Ulrich Niedermann <hun@n-dimensional.de> - 1.9.13-1
- Update to 1.9.13
* Fri Dec  4 2009 Hans Ulrich Niedermann <hun@n-dimensional.de> - 1.9.10-1
- Update to 1.9.10
* Sat Oct 31 2009 Hans Ulrich Niedermann <hun@n-dimensional.de> - 1.9.2-1
- Update to 1.9.2
* Mon Oct  5 2009 Hans Ulrich Niedermann <hun@n-dimensional.de> - 1.8.6-1
- 1.8.6 release
* Sat Sep 26 2009 Hans Ulrich Niedermann <hun@n-dimensional.de> - 1.8.1-1
- update to upstream's nted-1.8.1 release
* Wed Sep 23 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1.6.2-2
- Update desktop file according to F-12 FedoraStudio feature
* Mon Jul 27 2009 Hans Ulrich Niedermann <hun@n-dimensional.de> - 1.6.2-1
- update to bugfix release 1.6.2
* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild
* Tue Jul 21 2009 Hans Ulrich Niedermann <hun@n-dimensional.de> - 1.6.1-1
- Upstream release 1.6.0/1.6.1
* Wed Mar 25 2009 Hans Ulrich Niedermann <hun@n-dimensional.de> - 1.5.0-6
- Rebuilt for Fedora 11 to pick up font autodeps (#491970)
* Thu Mar  5 2009 Hans Ulrich Niedermann <hun@n-dimensional.de> - 1.5.0-5
- Remove workaround for broken po2xml which is now fixed
- Move noarch subpackage conditional part to single place in file
* Sat Feb 28 2009 Hans Ulrich Niedermann <hun@n-dimensional.de> - 1.5.0-4
- Add (disabled) workaround for broken po2xml (would remove translated docs)
* Thu Feb 26 2009 Hans Ulrich Niedermann <hun@n-dimensional.de> - 1.5.0-3
- noarch subpackage for doc
- use versioned requirements for subpackages
* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild
* Fri Feb 20 2009 Hans Ulrich Niedermann <hun@n-dimensional.de> - 1.5.0-1
- Update to upstream 1.5.0 release
- nothing user visible besides the upstream 1.5.0 release
- replace %%dir %%{_fontdir} by fontpackages-devel >= 1.18 build req
- replace %%define with %%global
- ship COPYING.GFDL file
- split off nted-ntedfont-fonts subpackage for the font people
* Mon Jan 11 2009 Hans Ulrich Niedermann <hun@n-dimensional.de> - 1.4.17-2
- remove unneeded fontconfig hooks from spec
* Sun Jan 11 2009 Hans Ulrich Niedermann <hun@n-dimensional.de> - 1.4.17-1.1
- remove wrongly encoded german description
- use new font packaging rules
- split ntedfont.pfa into nted-fonts subpackage
* Wed Dec 10 2008 Hans Ulrich Niedermann <hun@n-dimensional.de> - 1.4.17-1
- Update to upstream's 1.4.17 release.
* Tue Nov 30 2008 Hans Ulrich Niedermann <hun@n-dimensional.de> - 1.4.16-1
- Update to upstream's 1.4.16 release.
* Tue Nov 11 2008 Hans Ulrich Niedermann <hun@n-dimensional.de> - 1.4.15-1
- Update to upstream's 1.4.15 release.
* Fri Oct 17 2008 Hans Ulrich Niedermann <hun@n-dimensional.de> - 1.4.2-1
- Update to upstream's 1.4.2 release.
* Wed Oct 15 2008 Hans Ulrich Niedermann <hun@n-dimensional.de> - 1.3.3-1
- Update to upstream's 1.3.3 release.
* Fri Sep 19 2008 Hans Ulrich Niedermann <hun@n-dimensional.de> - 1.2.1-1
- Update to upstream's 1.2.1 release.
* Wed Sep 10 2008 Hans Ulrich Niedermann <hun@n-dimensional.de> - 1.0.8-2
- Work around upstream shipping an executable dynarray.h file.
* Tue Sep  9 2008 Hans Ulrich Niedermann <hun@n-dimensional.de> - 1.0.8-1
- Update to upstream's 1.0.8 release.
* Sun Sep  7 2008 Hans Ulrich Niedermann <hun@n-dimensional.de> - 1.0.7-2
- Consistently use %%{buildroot} instead of $RPM_BUILD_ROOT
- Ship upstream's now correct COPYING file.
- Ship all docs disregarding the languages.
* Sun Sep  7 2008 Hans Ulrich Niedermann <hun@n-dimensional.de> - 1.0.7-1
- Update to nted-1.0.7
- Remove all patches (all adopted by upstream now)
- Consistently use --docdir, %%docdir
* Sun Jun  8 2008 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.24.1-1
- Update to 0.24.1
* Sun Jun  8 2008 Hans Ulrich Niedermann <hun@n-dimensional.de> - 0.22.3-2.4
- Temporary test build
- Add GFDL to licenses
- Add lang(de) variants for Summary and Description
- Have nted look for html docs in correct place
* Tue Jun  3 2008 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.22.3-2
- Use compiler flags
- Fix compilation warnings
- Reorganize documentation files
* Fri Apr 25 2008 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.22.3-1
- Initial package
