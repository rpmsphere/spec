%global debug_package %{nil}
%define _name imgSeek

Name:           imgseek
BuildRequires:  libpng-devel python2-devel
BuildRequires:  ImageMagick libdrm-devel libjpeg-devel python2-devel python2-pillow
BuildRequires:  qt4-devel PyQt4-devel
#BuildRequires:  qt3-devel PyQt
Requires:       PyQt
License:        GPL v2 or later
Group:          Productivity/Graphics/Viewers
Requires:       ImageMagick, python2-pillow
Version:        0.8.6
Release:        143.21
Summary:        Photo Collection Manager and Viewer with Content-Based Query
URL:            http://www.imgseek.net/
Source:         %{_name}-%{version}.tar.bz2
Patch:          %{_name}.diff
Patch1:         %{_name}-uninitialized.patch
Patch2:         %{_name}-gcc43.patch
Patch3:         imgSeek-0.8.6-with-keyword.patch

%description
imgSeek is a photo collection manager and viewer with content-based
search and many other features. The query is expressed either as a
rough sketch painted by the user or as another image you supply (or an
image in your collection).

Authors:
--------
    Ricardo Niederberger Cabral <nieder@mail.ru>
    Steffen Neumann <sneumann@TechFak.Uni-Bielefeld.DE>

%prep
%setup -q -n %{_name}-%{version}
%patch
%patch1
%patch2
%patch3
# we want python2 distutils
rm -rf distutils
sed -i 's/"lib"/"%{_lib}"/' setup.py

%build
export CFLAGS="$RPM_OPT_FLAGS" 
python2 setup.py build

%install
python2 setup.py install --prefix=%{_prefix} --root=$RPM_BUILD_ROOT
install -Dm 0644 imgSeek.png $RPM_BUILD_ROOT/usr/share/pixmaps/imgSeek.png
install -Dm 0644 imgSeek.desktop $RPM_BUILD_ROOT/usr/share/applications/imgSeek.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc ChangeLog README THANKS AUTHORS COPYING TODO
%{_bindir}/%{_name}*
%{python_sitearch}/%{_name}*
%{_datadir}/%{_name}
%{_datadir}/applications/%{_name}.desktop
%{_datadir}/pixmaps/%{_name}.png

%changelog
* Wed Nov 23 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8.6
- Rebuilt for Fedora
* Fri Sep 12 2008 matejcik@suse.cz
- renamed "self.with" member, because "with" is now a keyword
* Thu Oct 11 2007 matejcik@suse.cz
- update to 0.8.6
  - apparently a bugfix-only release, no changelog was included
- added missing includes for gcc4.3
* Wed Jan  3 2007 jmatejek@suse.cz
- fixed "uninitialized variable" warning (#231223)
* Tue Feb 28 2006 jmatejek@suse.cz
- updated to reflect python changes due to #149809
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Sun Nov 27 2005 coolo@suse.de
- respect kdebindings3 split
* Sun Oct  2 2005 stbinner@suse.de
- fixed .desktop patch
* Tue May 10 2005 mcihar@suse.cz
- update to 0.8.5
- still doesn't build due to PyQT
* Mon Feb 21 2005 joe@suse.de
- revert back to using PyQt to be more flexible with packaging the
  bindings
* Thu Dec 23 2004 mcihar@suse.cz
- update to 0.8.4
* Thu Nov 25 2004 adrian@suse.de
- install desktop file
* Tue Sep 21 2004 adrian@suse.de
- use kdebindings3-python instead of PyQt
* Fri May 28 2004 mcihar@suse.cz
- update to 0.8.3
* Thu Jan 29 2004 mcihar@suse.cz
- include more docs
* Sat Jan 10 2004 adrian@suse.de
- build as user
* Mon Sep 29 2003 mcihar@suse.cz
- updated to 0.8.2:
    A bug related to settings and image preview on Python 2.3 was fixed.
    The broken thumbnail generation for non-database images on HTML
    albums was fixed. The code for adding images to the database
    recursively was improved.
* Mon Sep  8 2003 mcihar@suse.cz
- updated to 0.8.1:
  - startup speed improvement (code is byte compiled)
  - many bugfixes
* Mon Aug 11 2003 mcihar@suse.cz
- updated to 0.7.2:
  - HTML album improvements
  - more speed improvements when adding images to database using QT
  - added option (on by default) to create group name automatically
    when adding images. New group name will be current system time.
    Later this could evolve to something better, like the top level
    dir of images to be added, appended with something to make it
    unique.
  - improved IPTC metadata import. Repeated fields should be properly
    imported now
  - show image filesize and dimensions on the bottom label @ preview
    pane
  - misc. bugfixes everywhere
  - full persistency for all kinds of similarity grouping
    (color,date,filename would get lost on 0.7.1)
  - speedup when moving/copying images across groups
  - improved startup time
* Tue Jun 17 2003 mcihar@suse.cz
- no more needded to explicitly list directory
* Mon Jun 16 2003 mcihar@suse.cz
- use record-rpm
* Mon Jun  2 2003 mcihar@suse.cz
- use python distutils instead of the one distributed with imgSeek
- fixed lib64 build
* Mon Jun  2 2003 mcihar@suse.cz
- new package
