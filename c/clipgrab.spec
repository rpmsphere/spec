Name:           clipgrab
Version:        3.2.0.6
Release:        7.1
Summary:        Video downloader
License:        GNU General Public License version 3 (GPL v3)
Group:          Productivity/Multimedia/Video/Editors and Convertors 
URL:            http://clipgrab.de
Source0:        http://clipgrab.de/download/%{name}-%{version}.tar.bz2
Source1:        %{name}.desktop
Source2:        http://vanbittern.com/files/clipgrab-icons.zip
Requires:       ffmpeg
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  gcc-c++
BuildRequires:  qt4-devel
BuildRequires:  qt4-webkit-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  unzip
BuildRequires:  desktop-file-utils

%description
A program which downloads and converts online videos from YouTube, Vimeo,
DailyMotion, MyVideo and many other platforms.

%prep
%setup -q
%__mkdir "_icons"
pushd _icons
%__unzip "%{SOURCE2}"
popd #_icons

%build
#cleanup
%__rm -f moc_*

qmake-qt4 %{name}.pro QMAKE_CXXFLAGS="%{optflags}"
%__make clean
# fix build
  for _i in {gpl,qt,ffmpeg}; do
    ln -s logo.png logo-$_i.png
  done
%__make %{?_smp_flags}

%install
%__install -D -m 644 %{SOURCE1} $RPM_BUILD_ROOT/%{_datadir}/applications/%{name}.desktop
%__install -D -m 755 %{name} $RPM_BUILD_ROOT/%{_bindir}/%{name}

pushd _icons
%__rm -f 512.png
for f in *.png; do
    s="${f%.png}"
    %__install -D -m0644 "$f" "$RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${s}x${s}/apps/%{name}.png"
done
popd #_icons

%clean
%__rm -rf $RPM_BUILD_ROOT

%files
%defattr(0644,root,root,0755)
%doc COPYING
%attr(0755,-,-) %{_bindir}/clipgrab
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
* Sun Sep 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 3.2.0.6
- Rebuild for Fedora
* Sun May 20 2012 robertherb@arcor.de
- new upstream version <3.2.0.6>
* Mon Apr 30 2012 seife+obs@b1-systems.com
- new upstream version <3.2.0.5>
* Sun Nov 20 2011 reddwarf@opensuse.org
- new upstrean version <3.1.3.0>
- fix >12.1 build
* Sat Aug  6 2011 detlef@links2linux.de
- new upstream version <3.1.0.2>
* Sat Jul 23 2011 detlef@links2linux.de
- fix typo in clipgrap.desktop
* Wed Jul 14 2010 detlef@links2linux.de
- new upstream version <3.0.7.1>
* Sat Jul 10 2010 detlef@links2linux.de
- new upstream version <3.0.7>
* Mon Apr 19 2010 detlef@links2linux.de
- new upstream version <3.0.6.6>
* Thu Apr  8 2010 detlef@links2linux.de
- new upstream version <3.0.6.5>
* Fri Apr  2 2010 detlef@links2linux.de
- new upstream version <3.0.5.3>
* Mon Dec 28 2009 detlef@links2linux.de
- new upstream version <3.0.5>
* Mon Dec 21 2009 detlef@links2linux.de
- new upstream version <3.0.4.1>
* Mon Nov 30 2009 detlef@links2linux.de
- new upstream version <3.0.4>
* Thu Oct 29 2009 detlef@links2linux.de
- initial build clipgrab3
* Fri Mar 28 2008 detlef@links2linux.de
- initial build <2.0-beta2>
