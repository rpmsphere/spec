%define	oname	PhotoFilmStrip

Summary:	A program to make slide-show from pictures
Name:		photofilmstrip
Version:	3.7.3
Release:	1
License:	GPLv2+
Group:		Video
URL:		http://www.photofilmstrip.org/1-1-Home.html
Source0:	http://sourceforge.net/projects/photostoryx/files/photofilmstrip/%{version}/photofilmstrip-%{version}.tar.gz
BuildRequires:  python3-devel
BuildRequires:  python3-wxpython4
BuildRequires:  gettext
Requires:	python3-pillow
Requires:	mencoder
BuildArch:	noarch

%description
PhotoFilmStrip is a software to make movies out of your pictures in just 3
steps. First select your photos, customize the motion path and render the
video. There are several output possibilities for VCD, SVCD, DVD up to
FULL-HD. The effect of the slide-show is known as "Ken Burns". Comments of the
pictures are generated into a subtitle file. Furthermore an audio file can be
specified to setup the background music for the slide show. It has also the
opportunity to render slide shows in Full-HD (1920x1080) resolution.

%prep
%setup -q
chmod +r -R *

%build
#export DISPLAY=:0
python3 setup.py build

%install
#export DISPLAY=:0
python3 setup.py install --root=%{buildroot}

%files
%{_datadir}/doc/%{name}
%{_bindir}/%{name}
%{_bindir}/%{name}-cli
%{_datadir}/applications/%{name}.desktop
%{_datadir}/locale/*/LC_MESSAGES/%{oname}.mo
%{python3_sitelib}/%{name}*
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/pixmaps/%{name}.xpm

%changelog
* Sun May 22 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 3.7.3
- Rebuilt for Fedora
* Sun Feb 03 2013 Giovanni Mariani <mc2374@mclink.it> 1.5.0-69.1
- New release 1.5.0
- Killed rpmlint errors caused by the tarball file permissions
* Sun Dec 30 2012 Giovanni Mariani <mc2374@mclink.it> 1.4.0-69.1
- Rebuilt for Rosa 2012.1 by the MIB
- Added S2 to kill a ton of useless rpmlint warnings
* Fri Jan 07 2011 Giovanni Mariani <mc2374@mclink.it> 1.4.0-69.1mib2010.2
- New version 1.4.0
- Revised the spec file
- Massaged the Summary and Description text and removed the german versions of them
- Made the BuildRoot tag Wiki compliant
- Added a number to Source and Patch tags (as per Wiki specs)
- Provided a .desktop file as Source1 to replace the one provided in the sources
- Removed P0 (it does not apply)
- Removed uses of the deprecated "$RPM_BUILD_ROOT" macro
- Removed "%%post" and "%%postun" sections
- Killed a bunch of rpmlint warnings
* Mon Jun 21 2010 Beppe Florin <symbianflo@fastwebnet.it>
+ imported from pclos for mib
- MIB (Mandriva Italia Backport) - http://mib.pianetalinux.org
* Tue May 25 2010 slick50 <lxgator@gmail.com> 1.3.5-2pclos2010
- rebuild
* Sat May 15 2010 leiche <meisssw01 at aol.com> 1.3.5-1pclos2010
- Import to pclinuxos
