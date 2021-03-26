Name:           mucommander
Version:        0.8.5
#Version:        0.9.0
Release:        13.1
License:        GPLv3, LGPLv3, APSL 2.0, ICU, BSD and CC-BY
Summary:        File manager with Norton Commander interface written in Java
URL:            http://www.mucommander.com
Group:          Productivity/File utilities
# svn export https://svn.mucommander.com/mucommander/tags/release_0_8_5/ mucommander-0.8.5
# tar cvjf mucommander-0.8.5.tar.bz2 mucommander-0.8.5
Source0:        %{name}-%{version}.tar.bz2
Source1:        %{name}.desktop
BuildRequires:  ant >= 1.6.5
BuildRequires:  java-devel-openjdk lua
BuildArch:      noarch

%description
muCommander is a lightweight, cross-platform file manager featuring a Norton Commander style interface
and running on any operating system with Java support (Mac OS X, Windows, Linux, *BSD, Solaris...).

* Virtual filesystem with local volumes, FTP, SFTP, SMB, NFS, HTTP and Bonjour support
* Quickly copy, move, rename files, create directories, email files...
* Browse, create and uncompress ZIP, RAR, TAR, GZip, BZip2, ISO/NRG, AR/Deb and LST archives
* ZIP files can be modified on-the-fly, without having to recompress the whole archive
* Universal bookmarks and credentials manager
* Multiple windows support
* Full keyboard access
* Highly configurable
* Available in 22 languages : American & British English, French, German, Spanish, Czech,
Simplified & Traditional Chinese, Polish, Hungarian, Russian, Slovenian, Romanian, Italian,
Korean, Brazilian Portuguese, Dutch, Slovak, Japanese, Swedish, Danish and Ukrainian.
* Free Software (GPL)

%prep
%setup -q

%build
#ant obfuscate
ant
echo '#!/bin/bash
java -jar %{_javadir}/%{name}.jar' > %{name}.sh

%install
install -D -m 0644 tmp/compile/mucommander_unobf.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
install -D -m 0755 %{name}.sh $RPM_BUILD_ROOT%{_bindir}/mucommander
for i in 16 32 48 128 256; do
  install -D -m 0644 res/images/mucommander/icon${i}_24.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${i}x${i}/apps/mucommander.png
done
install -D -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc license.txt readme.txt
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/16x16
%dir %{_datadir}/icons/hicolor/16x16/apps
%dir %{_datadir}/icons/hicolor/32x32
%dir %{_datadir}/icons/hicolor/32x32/apps
%dir %{_datadir}/icons/hicolor/48x48
%dir %{_datadir}/icons/hicolor/48x48/apps
%dir %{_datadir}/icons/hicolor/128x128
%dir %{_datadir}/icons/hicolor/128x128/apps
%dir %{_datadir}/icons/hicolor/256x256
%dir %{_datadir}/icons/hicolor/256x256/apps
%{_bindir}/mucommander
%{_javadir}/%{name}.jar
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/mucommander.png

%changelog
* Sun Mar 04 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8.5
- Rebuild for Fedora
* Wed Sep 14 2011 kirill.kirillov@gmail.com
- fixed license tag
* Thu Apr  1 2010 prusnak@suse.cz
- updated to 0.8.5
* Wed Jun 17 2009 radomir.cernoch@gmail.com
- initial package for openSUSE
