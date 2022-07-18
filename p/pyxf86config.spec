%global __os_install_post %{nil}
%undefine _debugsource_packages

Summary: Python wrappers for libxf86config
Name: pyxf86config
Version: 0.3.37
Release: 13.1
URL: http://fedoraproject.org/wiki/pyxf86config
Source0: http://ajax.fedorapeople.org/%{name}/%{name}-%{version}.tar.bz2
Patch0: 0001-libxf86config.a-gained-dependency-on-xstrtokenize-pu.patch
Patch1: 0002-Provide-xf86CheckBoolOption.patch
Patch2: 0003-Initialize-configuration-file-parser-before-use.patch
Patch3: remove-buffers.patch
Patch4: option-header.patch
License: GPLv2
Group: System Environment/Libraries
BuildRequires: glib2-devel
BuildRequires: libX11-devel
BuildRequires: python2-devel python-unversioned-command
BuildRequires: xorg-x11-server-devel

# we don't want to provide private python extension libs
%{?filter_setup:
%filter_provides_in %{python2_sitearch}/.*\.so$ 
%filter_setup
}

%description
Python wrappers for the X server config file library libxf86config.
It is used to read and write X server configuration files.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

sed -i 's|-lxf86config||' Makefile.*
sed -i '1i #include <xorg-server.h>' xf86config_ext.c
sed -i -e '/textclockfreq/d' -e '/bios_base/d' pyxf86conf.c

%build
export CFLAGS="-Wno-format-security -fPIC"
pyver=$(python2 -c 'import sys ; print sys.version[:3]')
%configure  --x-libraries=%{_libdir} --with-python-version=$pyver
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

%files
%doc README NEWS AUTHORS COPYING
%{python2_sitearch}/ixf86configmodule.so
%{python2_sitearch}/xf86config.py*

%changelog
* Sun Mar 10 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.37
- Rebuilt for Fedora
* Tue Nov 29 2011 Dave Airlie <airlied@redhat.com> 0.3.37-12
- drop config buffers code since upstream X dropped it
* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.37-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild
* Sun Nov 07 2010 Lubomir Rintel <lkundrak@v3.sk> - 0.3.37-10
- Unbreak it for new XOrg configuration parser
* Sat Oct 02 2010 Parag Nemade <paragn AT fedoraproject.org> - 0.3.37-9
- Merge-review cleanup (#226349)
* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.3.37-8
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild
* Fri Aug 07 2009 Dave Airlie <airlied@redhat.com> 0.3.37-7
- fix X server and put this back
* Fri Aug 07 2009 Dave Airlie <airlied@redhat.com> 0.3.37-6
- fix ErrorF/VErrorF symbol visibility - hacky but should do for now
* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.37-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild
* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.37-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild
* Sat Feb 21 2009 Adam Jackson <ajax@redhat.com> 0.3.37-3
- Merge review cleanups (#226349)
* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.3.37-2
- Rebuild for Python 2.6
* Thu Mar 13 2008 Jeremy Katz <katzj@redhat.com> - 0.3.37-1
- And fix to not cause tracebacks with current X (#437236)
* Tue Mar 11 2008 Jeremy Katz <katzj@redhat.com> - 0.3.36-1
- Fix build with current X
* Tue Mar 11 2008 Jeremy Katz <katzj@redhat.com> - 0.3.35-1
- Don't include keyboard in the template
* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.3.34-2
- Autorebuild for GCC 4.3
* Wed Sep 26 2007 Adam Jackson <ajax@redhat.com> 0.3.34-1
- pyxf86config 0.3.34
- License is GPLv2
- Bump libxf86config-devel buildreq to pick up symbol visibility tweak
* Tue Aug 21 2007 Adam Jackson <ajax@redhat.com> - 0.3.33-2
- Rebuild for build id
* Mon Mar 12 2007 Adam Jackson <ajax@redhat.com> 0.3.33-1
- Add some more modes to the default set (#165325)
* Sat Jan  6 2007 Jeremy Katz <katzj@redhat.com> - 0.3.32-1
- Fix inconsistent PyObject/PyMem usage (#219918, #220993)
* Thu Dec  7 2006 Jeremy Katz <katzj@redhat.com> - 0.3.31-4
- rebuild against python 2.5
* Tue Dec 5 2006 Adam Jackson <ajax@redhat.com> 0.3.31-3
- Update libxf86config-devel BR to a sufficiently new version to not print the
  "Comment all HorizSync and VertSync values to use DDC" message, and
  rebuild.  (#216288)
* Sun Oct 01 2006 Jesse Keating <jkeating@redhat.com> - 0.3.31-2
- rebuilt for unwind info generation, broken in gcc-4.1.1-21
* Thu Sep 21 2006 Adam Jackson <ajackson@redhat.com> 0.3.31-1.fc6
- Add a .size() method to genlists.
- Use bzip2 archive
* Fri Aug 25 2006 Adam Jackson <ajackson@redhat.com> 0.3.30-1.fc6
- Remove a stray reference to XFree86.
* Wed Aug 23 2006 Adam Jackson <ajackson@redhat.com> 0.3.29-1.fc6
- Default depth of 24.
* Mon Aug 21 2006 Adam Jackson <ajackson@redhat.com> 0.3.28-1.fc6
- Decode degenerate ranges correctly. (#132679)
* Wed Jul 26 2006 Mike A. Harris <mharris@redhat.com> 0.3.27-2.fc6
- Remove dependency on xorg-x11-server-sdk, and replace it with correct dep
  on "libxf86config-devel >= 1.1.1-7", and rebuild in order to pick up
  necessary fixes in the static library.
- Use Fedora Extras style BuildRoot tag.
- Use {?dist} tag in Release
* Tue Jul 25 2006 Chris Lumens <clumens@redhat.com> 0.3.27-1
- Remove gigantic keyboard comment.
- Don't write out an empty modules section.
* Wed Jul 19 2006 Chris Lumens <clumens@redhat.com> 0.3.26-1
- Don't traceback when given empty section identifiers.
* Tue Jul 18 2006 Chris Lumens <clumens@redhat.com> 0.3.25-1
- Remove unneeded X config sections from template generation.
* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.3.24-3.1
- rebuild
* Tue Jun 13 2006 Jeremy Katz <katzj@redhat.com> - 0.3.24-3
- ppc64 X lives
* Fri May 26 2006 Adam Jackson <ajackson@redhat.com> 0.3.24-2
- BuildRequires: xorg-x11-server-sdk (#191894)
* Wed Feb 22 2006 Chris Lumens <clumens@redhat.com> 0.3.24-1
- Add 1600x1024 and 800x512 to the list of supported resolutions (#115679)
* Tue Jan 17 2006 Christopher Aillon <caillon@redhat.com> 0.3.23-1
- Use the standard X headers instead of keeping a copy in-tree
* Wed Dec 21 2005 Jesse Keating <jkeating@redhat.com>
- changed BuildReq to new modular devel package
- Changed search path for X libraries
* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt
* Sun Nov 13 2005 Jeremy Katz <katzj@redhat.com> - 0.3.20-1
- the X server compiles in the path for rgb.txt, so don't explicitly list 
  (fixes for the path move with modular X)
- get rid of no longer needed %%preun
- modular X buildrequires changes
* Fri Jul 15 2005 Paul Nasrat <pnasrat@redhat.com> - 0.3.19-6
- ExcludeArch ppc64 again
* Fri Jul 15 2005 Paul Nasrat <pnasrat@redhat.com> - 0.3.19-5
- Drop ppc64 ExcludeArch
- pyc and pyo includes
* Tue Mar 29 2005 Warren Togami <wtogami@redhat.com> - 0.3.19-4
- #138263 broken preun #142419 auto pyver
* Mon Nov  8 2004 Jeremy Katz <katzj@redhat.com> - 0.3.19-2
- rebuild for python 2.4
- make the python requires be on the python-abi
* Wed Aug 11 2004 Jeremy Katz <katzj@redhat.com> - 0.3.19-1
- Change keyboard driver to kbd
* Thu Apr 15 2004 Mike A. Harris <mharris@redhat.com> - 0.3.18-1
- Do not write out XkbRules line to config file, as it is unnecessary hard
  coding the rules file, which has a built in default which should always
  work. (#120858)
* Thu Apr 15 2004 Jeremy Katz <katzj@redhat.com> - 0.3.17-1
- xorg for XkbRules
* Wed Apr 14 2004 Alex Larsson <alexl@redhat.com> 0.3.16
- Rebuild for the new libxf86config
- remove references to XFree86
* Thu Feb 19 2004 Brent Fox <bfox@redhat.com> 0.3.15-1
- remove the setupMice() function createTemplate() 
- because the 2.6 kernel puts both PS/2 and USB mice on the same device
* Mon Feb  9 2004 Alexander Larsson <alexl@redhat.com> 0.3.14-1
- fix range array bug
* Thu Nov  6 2003 Jeremy Katz <katzj@redhat.com> 0.3.13-2
- rebuild for python 2.3
- don't build on ppc64 either since X is missing bits there as well
* Tue Jul 29 2003 Elliot Lee <sopwith@redhat.com> 0.3.13-1
- Rebuild
* Wed Jun  4 2003 Brent Fox <bfox@redhat.com> 0.3.12-1
- add a 'scrnum' attribute to the adjacency section
* Tue Jun  3 2003 Brent Fox <bfox@redhat.com> 0.3.11-1
- add a function to xf86config.py called getAllScreens()
* Tue Jun  3 2003 Brent Fox <bfox@redhat.com> 0.3.10-1
- add a BuildRequires for python2-devel
- add an options attribute to the server layout section (for Xinerama)
* Tue Apr 29 2003 Alexander Larsson <alexl@redhat.com> 0.3.6-1
- Added laptop resolutions
* Mon Jan 27 2003 Alexander Larsson <alexl@redhat.com> 0.3.5-1
- Rebuild
* Wed Jan 15 2003 Michael Fulbright <msf@redhat.com> 0.3.4-1
- remove code in xf86config.py:createTemplate() that inserted a Display
  section.  We want user to supply this and it shouldnt be in template.
* Sat Jan 11 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- add ExcludeArch: s390 s390x
* Thu Dec 12 2002 Mike A. Harris <mharris@redhat.com> 0.3.3-1
- Remove Excludearch alpha
* Tue Nov 12 2002 Michael Fulbright <msf@redhat.com> 0.3.2-1
- Added some convenience functions.
* Mon Jul  8 2002 Alexander Larsson <alexl@redhat.com>
- Bump to 0.3.1
* Mon Jun 17 2002 Alexander Larsson <alexl@redhat.com>
- Bump to 0.3.0
* Fri May 24 2002 Alex Larsson <alexl@redhat.com> 0.2.0-3
- Excludearch alpha for now
* Fri May 24 2002 Alex Larsson <alexl@redhat.com> 0.2.0-2
- Add some doc files
* Fri May 24 2002 Alex Larsson <alexl@redhat.com> 0.2.0-1
- Update version number for new release
* Thu Apr 11 2002 Alex Larsson <alexl@redhat.com> 0.1.0-1
- Initial release
* Wed Apr 10 2002 Alex Larsson <alexl@redhat.com>
- Initial specfile
