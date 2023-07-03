Name:           tvmaxe
Summary:        Watch TV channels on Linux
Version:        0.09
Release:        5.1
Source0:        tv-maxe-%{version}.tar.gz
Source1:        tv-maxe.desktop
Source2:        tv-maxe
Source3:	tv-maxe.svg
Source4:	channel-editor.tar.gz
BuildRequires:  desktop-file-utils
BuildRequires:	python2-devel
URL:            https://code.google.com/p/tv-maxe
Group:          Applications/Multimedia
# Main project is GPL-3.0, vlc.py is GPL-2.0+, workerpool is MIT(compabile with GPL-3.0), so license is
License:        GPL-3.0
Requires:       pygtk2
Requires:       sopcast
Requires:       vlc 
Requires:       mplayer
BuildArch:      noarch

%description
TV-MAXE is an application which provides the ability to watch TV stations and
listen radio via different streams, such is SopCast. Currently it has a large
number of channels, both romanian and international.

%prep 
%setup -q -n tv-maxe-%{version}

%build

%install
# menu
mkdir -pv %{buildroot}%{_datadir}/applications
cp %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop

# binaries
mkdir -pv %{buildroot}%{_bindir}
cp %{SOURCE2} %{buildroot}%{_bindir}/%{name}
chmod 755 %{buildroot}%{_bindir}/%{name}

# icons
mkdir -pv %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
cp %{SOURCE3} %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

# add channel editor for advanced user 
cp -r %{SOURCE4} ./
tar -xzf channel-editor.tar.gz
rm -rf channel-editor.tar.gz
chmod +x channel-editor/channeleditor.py

# libraries
mkdir -pv %{buildroot}%{_datadir}/%{name}
cp -r * %{buildroot}%{_datadir}/%{name}/
# remove non-needed
rm -rf %{buildroot}%{_datadir}/%{name}/CHANGELOG
rm -rf %{buildroot}%{_datadir}/%{name}/%{name}.png
# link channel editor
ln -sf %{_datadir}/%{name}/channel-editor/channeleditor.py %{buildroot}%{_bindir}/%{name}-channeleditor

# fix locale
mkdir -pv %{buildroot}%{_datadir}/locale
mkdir -pv %{buildroot}%{_datadir}/help
mv %{buildroot}%{_datadir}/%{name}/lng/* %{buildroot}%{_datadir}/locale/
rm -rf %{buildroot}%{_datadir}/%{name}/lng
find %{buildroot}%{_datadir}/locale/ -type f -name "tvmaxe.po" -delete -print
find %{buildroot}%{_datadir}/locale/ -type f -name "tvmaxe.mo" -exec bash -c 'i={}; mv $i ${i/tvmaxe/tv-maxe}' \; -print

# fix W:non-executable-script
pushd %{buildroot}%{_datadir}/%{name}/
find ./ -type f -name "*.py" | xargs sed -i '/^#!\/usr\/bin\/env python$/,+1 d'
find ./ -type f -name "*.py" | xargs sed -i '/^#!\/usr\/bin\/python$/,+1 d'
find ./ -type f -name "*.py" | xargs sed -i '/^#!\ \/usr\/bin\/python$/,+1 d'
# add shebang to channeleditor
sed -i "1i#!\/usr\/bin\/env python" %{buildroot}%{_datadir}/%{name}/channel-editor/channeleditor.py
rm -rf %{buildroot}%{_datadir}/help

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_datadir}/tvmaxe/channel-editor/channeleditor.py

%files
%doc CHANGELOG
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/%{name}
%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo

%changelog
* Sun Jun 23 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.09
- Rebuilt for Fedora
* Wed Mar 28 2012 i@marguerite.su
- Fix bnc#754459, license problem, thanks to babelworx.
* Sun Mar 25 2012 i@marguerite.su
- Update version 0.06.5
  * Channel lists are now cached
  * Switched subscriptions to project's SVN
  * HTTP remote control
  * Separation of protocol engines and multimedia backends
  * Removed recording options
  * GStreamer backend support
  * Faster startup
- Fixed locale directory. use system default dir.
- Added Chinese channels.
- Modified desktopfile. install icons to system default dir.
- Added channel editor for advanced users.
- Cleaned specfile and fixed python related warnings.
* Thu Oct 27 2011 i@marguerite.su>
- First openSUSE release
- Build on OBS
- Update version 0.06.4
  * TV-MAXE now uses local channel lists
  * Added a script to update channel lists
  * Added Russian , Spanish, Danish and Chinese ( both Simplified and Tranditional) translations
* Mon Aug  8 2011 venerix@gmail.com
- New release
- Fixed channel lists, again
- Fixed spec with proper application naming
- MRB-Mandriva Users.Ro
* Fri Aug  5 2011 venerix@gmail.com
- Rebuild for 2011.0
- MRB-Mandriva Users.Ro
* Sun Jul 24 2011 venerix@gmail.com
- Fixed romanian translations
- Fixed channel lists
- MRB-Mandriva Users.Ro
* Sun Jun 26 2011 venerix@gmail.com
- New release
- MRB-Mandriva Users.Ro
- Bugfixes
- TV-MAXE now detects available backends
* Fri May 27 2011 venerix@gmail.com
- New release
- MRB-Mandriva Users.Ro
- Update version 0.05
  * Status Icon
  * TV Shows section was cutted off
  * Subscribe to different TV Channels Lists
  * MPlayer backend with muted volume fixed
  * Channel info window
  * Broken channel reporting
  * Icon caching
  * Better icon downloading
  * TV guide fixes
  * Radio player
  * Internationalization support
* Thu Mar  3 2011 symbianflo@fastwebnet.it
- New release
- MRB-Mandriva Users.Ro
* Fri Dec  3 2010 venerix@blug.ro
- First release tvmaxe-0.01-69.1mrb2010.1
- Build for 2010.1 noarch
- MRB-Mandriva Users.Ro
