%global debug_package %{nil}
%define oname Videoporama

Name:		videoporama
Version:	0.8.2
Release:	76.4
Summary:	A Python application to make video of image slide-show
License:	GPLv2+
Group:		Video
URL:		http://www.videoporama.tuxfamily.org
Source0:	%{oname}_%{version}-1.tar.gz
BuildRequires:	desktop-file-utils
BuildRequires:	python3-qt5-devel
BuildRequires:	python3-pillow-devel
BuildRequires:	qt5-devel
BuildRequires:	qscintilla-qt5-devel
#BuildRequires:	xvid-devel
BuildArch:	noarch
Requires:	python3-pillow
Requires:	ffmpeg
Requires:	mjpegtools
Requires:	sox
Requires:	mplayer

%description
Videoporama is a Python application for the creation of videos sequences
(slide-shows) made of:
  * titles, fixed or livened up;
  * images or photos, fixed or livened up;
  * movie clips.

These sequences are assembled in a slide show by the means of transitions of
sequence to produce a complete video.
Videoporama supports the following options:
  * cutting of video clips;
  * addition of text notes for images, photos, sequences and animations;
  * creation of animations by zooming or applying Ken Burns Effect on part of
    images or photos;
  * making of transitions between sequences;
  * addition of a background sound (wav, mp3 or ogg);
  * generation of videos usable by most of the current videos equipments:
    supported video format ranging from QVGA (320x240) to Full HD (1920x1080);
  * support for aspect ratio of 4:3 or 16:9;
  * support for raw dv (dv), avi, mpg, flv (Video flash), mp4 and mkv video
    formats.

%prep
%setup -qn %{oname}_%{version}

# Remove all the useless exec bits from help, icons, iconstr, locale and luma directories
# and also from the main dir
chmod -x help/images/*.png
chmod -x help/*.html
chmod -x help/*.css
chmod -x icons/*.png
chmod -x iconstr/*.png
chmod -x locale/*.qm
chmod -x luma/*.png
chmod -x *.py

%build
python3 setup.py build

%install
python3 setup.py install --skip-build --root=%{buildroot}

# Remove useless installed hidden files
rm -rf %{buildroot}%{_bindir}/.svn
rm -rf %{buildroot}%{_datadir}%{name}/help/images/.directory
rm -rf %{buildroot}%{_datadir}%{name}/help/images/.svn

# Create dest directories for icon and desktop files
mkdir -p %{buildroot}%{_datadir}/pixmaps
mkdir -p %{buildroot}%{_mandir}/man1

# Move the icon file
install -m 0644 debian/%{name}.xpm %{buildroot}%{_datadir}/pixmaps/

# Use the provided desktop file
desktop-file-install	-m 0644 --dir %{buildroot}%{_datadir}/applications/ \
			--add-category=Qt \
			debian/%{name}.desktop

# Add the manpage
install -m 0644 debian/%{name}.1 %{buildroot}%{_mandir}/man1/

sed -i 's|^import Image|from PIL import Image|' %{buildroot}%{_datadir}/%{name}/*.py


%files
%doc licences.txt README
%{_bindir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.xpm
%{_mandir}/man1/%{name}.1.*
%{python_sitelib}/*

%changelog
* Wed Nov 13 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8.2
- Rebuild for Fedora
* Sun Dec 30 2012 Giovanni Mariani <mc2374@mclink.it> 0.8.2-69.1
- Rebuilt for Rosa 2012.1 by the MIB
- Adjusted file list
* Sun May 27 2012 Giovanni Mariani <mc2374@mclink.it> 0.8.2-69.3mib2010.2
- Rebuild for new Qt
* Mon May 16 2011 Giovanni Mariani <mc2374@mclink.it> 0.8.2-69.2mib2010.2
- Added a missing (and needed) Requires for python-imaging
* Tue May 10 2011 Giovanni Mariani <mc2374@mclink.it> 0.8.2-69.1mib2010.2
- New version 0.8.2 for the MIB
- Adjusted the License type (see licence.rtf file in the sources)
- Removed some useless %%defines
- Made use of a valid value for the Group tag
- Changed the Reqs to be 64bit compliant and add version info
  (according to README and INSTALL files in the source tarball)
- Made the BuildRoot tag compliant with Wiki specs
- Redone the Summary and Description text in english lang
- Made sure the Description text is length <= 76 chars
- Removed uses of the deprecated "$RPM_BUILD_ROOT" macro
- Killed some other rpmlint warnings
- Added also a desktop file, an icon file and a manpage taken from sources
* Sat Feb 26 2011 Calogero Scarnà <specialworld83@gmail.com> 0.8.1
- New package introduction for Mandriva International Backports
- MIB (Mandriva International Backport) - http://mib.pianetalinux.org/
