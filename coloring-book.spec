Name:          coloring-book
Version:       0.13
Release:       11.4
Summary:       A simple coloring (or colouring) book program
Group:         Graphical Desktop/Applications/Educational
URL:           http://kavlon.org/index.php/cb
Source0:       http://kavlon.org/projects/releases/cb-%{version}.tar.gz
Source1:       coloring-book.desktop
Source2:       coloring-book-icons.tar.bz2
# italian version of the default book by KaeZar
Source3:       coloring-book-it.tar.bz2
Patch0:        %{name}-0.13-lang_env.patch
Patch1:        %{name}-0.13-select_book_by_lang.patch
# italian localization by KaeZar
Patch2:        %{name}-0.13-lang_it.patch
Patch3:        %{name}-0.13-mouse_speedup.patch
License:       GPL
BuildRequires: atlas, pygame-devel
Requires:      pygame
BuildArch:     noarch

%description
A simple coloring (or colouring) book program written in Python w/ Pygame.

%prep
%setup -q -n cb -a3
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/%{name} \
           $RPM_BUILD_ROOT%{_datadir}/pixmaps

cp -r * $RPM_BUILD_ROOT%{_datadir}/%{name}
# fix files permissions
find $RPM_BUILD_ROOT%{_datadir}/%{name} \
   -type f -exec chmod 644 {} \;
chmod 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/CB.py

install -D -m644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
tar xjf %{SOURCE2} --strip-components=1 -C $RPM_BUILD_ROOT%{_datadir}/pixmaps

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_datadir}/%{name}/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/coloring-book
%exclude %{_datadir}/%{name}/books/default/blank.py
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/*.png

%changelog
* Fri Jun 17 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.13
- Rebuild for Fedora
* Fri May 22 2009 Davide Madrisan <davide.madrisan@gmail.com> 0.13-6mamba
- update specfile
* Sat Jun 17 2006 Davide Madrisan <davide.madrisan@qilinux.it> 0.13-5qilnx
- fixed patch1 to correctly handle unsupported locales
* Mon Apr 17 2006 Davide Madrisan <davide.madrisan@qilinux.it> 0.13-4qilnx
- p0: take care of the LANG environment variable
- p1: use 'books/default' only if 'books/$LANG' is not found
- p2: italian localization by KaeZar
- p3: increase the default mouse speedup
- desktop file: added french translation
- %%install block rewritten
- fixed files permissions
- package arch set to noarch
* Wed Nov 30 2005 Davide Madrisan <davide.madrisan@qilinux.it> 0.13-3qilnx
- requires python-pygame
- new icons
* Wed Aug 17 2005 Silvan Calarco <silvan.calarco@qilinux.it> 0.13-2qilnx
- files moved to site-python libdir
* Mon Aug 01 2005 Alessandro Ramazzina <alessandro.ramazzina@qilinux.it> 0.13-1qilnx
- package created by autospec
