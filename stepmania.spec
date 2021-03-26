%define cvsdate 20080103

Name:	        stepmania
Version:	4.0
Release:	1
URL:		http://www.stepmania.com/
License:	GNU Lesser General Public License (LGPL)
Summary:        Music/rhythm game
Group:          Amusements/Games/Arcade
Source0:        StepMania-CVS-%{cvsdate}-src.tar.bz2
Source1:        stepmania
Source2:        stepmania.desktop
Source3:        StepMania.xpm
Patch0:         %{name}-gcc43.patch
Patch1:         %{name}-datadir.patch
BuildRequires:	cmake, librsvg2-devel, libjpeg-devel, libogg-devel, libvorbis-devel, zlib-devel, gtk2-devel
BuildRequires:  mesa-libGL-devel, SDL-devel, alsa-lib-devel, cairo-devel, pango-devel, libpng-devel, gettext

%description
StepMania is a music/rhythm game. The player presses different buttons
in time to the music and to note patterns that scroll across the screen.
Features 3D graphics, visualizations, support for gamepads/dance pads,
a step recording mode, and more!

%prep
%setup -q -n StepMania-CVS-%{cvsdate}-src
%patch0
%patch1

%build
%configure --without-mp3
sed -i 's|-Werror=format-security||' Makefile */Makefile
make %{?jobs:-j%jobs}

%install
install -D -m 0755 src/stepmania $RPM_BUILD_ROOT%{_datadir}/stepmania/stepmania
install -D -m 0644 Packages/StepMania.smzip $RPM_BUILD_ROOT%{_datadir}/stepmania/Packages/StepMania.smzip
install -D -m 0644 src/GtkModule.so $RPM_BUILD_ROOT%{_datadir}/stepmania/GtkModule.so
install -D -m 0777 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/stepmania
install -D -m 0644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/applications/stepmania.desktop
install -D -m 0644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/pixmaps/StepMania.xpm
mkdir -p $RPM_BUILD_ROOT%{_datadir}/stepmania/{Songs,AdditionalSongs,Courses,AdditionalCourses,Edits}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/stepmania
%doc Docs/Licenses.txt
%dir %{_datadir}/stepmania
%{_datadir}/stepmania/*
%{_datadir}/pixmaps/StepMania.xpm
%{_datadir}/applications/stepmania.desktop

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 4.0
- Rebuild for Fedora
* Wed Dec 22 2010 Chrin Lin <chris.lin@ossii.com.tw> 4.0-0 OX
- OX LINUX Version
