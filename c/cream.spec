Name:           cream
Summary:        User-friendly face for Vim
Version:        0.43
Release:        6.1
Source:         %{name}-%{version}.tar.gz
URL:            https://cream.sourceforge.net/
License:        GPL
Group:          Editors
BuildRequires:  desktop-file-utils
Requires:       vim-X11
BuildArch:      noarch

%description
Cream is a modeless GUIification of Vim.  Cream includes all the features of
Vim plus many custom utilities. A short list of features includes syntax
highlighting, spell check, multi-file find/replace, bookmarking, function
prototype popups, macros, auto-wrapping, reformatting, justification,
time/date stamps, file explorer, completion, sorting, calendar, tag
navigation, block commenting, Microsoft, Unix and Apple format text editing,
virtually unlimited file sizes, 38 varieties of 8-bit, 2-byte, and Unicode
support, single/multiple document modes, unlimited undo/redo, show invisible
characters, word count, and more.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %buildroot/%_datadir/vim/cream/{addons,bitmaps,docs,docs-html,filetypes,help,spelldicts}
cp creamrc %buildroot/%_datadir/vim/cream/
cp *.vim %buildroot/%_datadir/vim/cream/
cp addons/*.vim %buildroot/%_datadir/vim/cream/addons/
cp bitmaps/*.bmp %buildroot/%_datadir/vim/cream/bitmaps/
cp bitmaps/*.xpm %buildroot/%_datadir/vim/cream/bitmaps/
cp docs/*.txt %buildroot/%_datadir/vim/cream/docs/
cp docs-html/*.html %buildroot/%_datadir/vim/cream/docs-html/
##cp docs-html/*.css %buildroot/%_datadir/vim/cream/docs-html/
cp docs-html/*.png %buildroot/%_datadir/vim/cream/docs-html/
cp filetypes/*.vim %buildroot/%_datadir/vim/cream/filetypes/
cp help/*.txt %buildroot/%_datadir/vim/cream/help/
#cp spelldicts/cream-spell-dict-eng-s*.vim %buildroot/%_datadir/vim/cream/spelldicts/
#cp spelldicts/cream-spell-dict.vim %buildroot/%_datadir/vim/cream/spelldicts/

mkdir -p %buildroot/%_bindir
sed -i 's|\\$VIMRUNTIME|/usr/share/vim|' cream
cp cream %buildroot/%_bindir

mkdir -p %buildroot/%_datadir/applications
cp cream.desktop %buildroot/%_datadir/applications/

#mkdir -p %buildroot/
#cp cream.svg %buildroot/%_iconsdir/

#menu

desktop-file-install --vendor="" \
  --remove-key="XClassHintResName" \
  --remove-category="Application" \
  --add-category="TextEditor" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

install -Dm644 %{name}.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

%files
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/vim/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Thu Jul 14 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.43
- Rebuilt for Fedora

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.42-2mdv2011.0
+ Revision: 610171
- rebuild

* Wed Dec 30 2009 Jérôme Brenier <incubusss@mandriva.org> 0.42-1mdv2010.1
+ Revision: 483858
- new bugfix version 0.42

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 0.41-2mdv2010.0
+ Revision: 437145
- rebuild

* Wed Feb 18 2009 Jérôme Soyer <saispo@mandriva.org> 0.41-1mdv2009.1
+ Revision: 342436
- New upstream release

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - drop old menu
    - kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Jun 11 2007 Jérôme Soyer <saispo@mandriva.org> 0.39-1mdv2008.0
+ Revision: 38005
- Fix Build
- New release


* Sat Dec 30 2006 Jérôme Soyer <saispo@mandriva.org> 0.38-1mdv2007.0
+ Revision: 102731
- Fix buildrequires
- New release 0.38
- Import cream

* Thu Sep 14 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.36-2mdv2007.0
- XDG

* Tue Jun 13 2006 Charles A Edwards <eslrahc@mandriva.org> 0.36-1mdv2007.0
- 0.36
- mkrel
- .css docs no longer done

* Fri Apr 07 2006 Austin Acton <austin@mandriva.org> 0.35-1mdk
- New release 0.35

* Sat Feb 18 2006 Austin Acton <austin@mandriva.org> 0.34-1mdk
- New release 0.34

* Fri Nov 04 2005 Austin Acton <austin@mandriva.org> 0.33.1-1mdk
- New release 0.33.1

* Fri Oct 07 2005 Austin Acton <austin@mandriva.org> 0.33-1mdk
- New release 0.33

* Mon Feb 07 2005 Austin Acton <austin@mandrake.org> 0.32-1mdk
- initial package
