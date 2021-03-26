%define datadate 20091001

Summary: Game data for the Nexuiz first person shooter
Name: nexuiz-data
Version: 2.5.2
Release: 1
License: GPLv2+
Group: Amusements/Games
URL: http://www.nexuiz.com/
# Source is custom, obtained with :
# wget  http://downloads.sourceforge.net/nexuiz/nexuiz-252.zip
# unzip nexuiz-252.zip
# mkdir nexuiz-data-2.5.2/
# mv Nexuiz/data/ Nexuiz/Docs/* \
#    Nexuiz/gpl.txt nexuiz-data-2.5.2/
# tar czvf nexuiz-data-2.5.2.tar.gz nexuiz-data-2.5.2/
Source0: nexuiz-data-%{version}.tar.gz
NoSource: 0
BuildArch: noarch

%description
Nexuiz is a fast-paced, chaotic, and intense multiplayer first person shooter, 
focused on providing basic, old style deathmatches.
Data (textures, maps, sounds and models) required to play nexuiz.

%prep
%setup -q
%{__sed} -i 's/\r//' Readme.htm *.txt FAQ*
%{__sed} -i 's/\r//' server/rcon2irc/*  server/rcon.pl  server/readme.txt \
    server/server.cfg  server/server_linux.sh  server/server_mac.sh  \
    server/server_pro_linux.sh  server/server_pro_mac.sh \
    server/server_pro_windows.bat  server/server_windows.bat
%{__chmod} 644 server/*
%{__chmod} 755 server/rcon2irc
%{__chmod} 644 server/rcon2irc/*

%build

%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_datadir}/nexuiz/data/
%{__install} -p data/data%{datadate}.pk3 \
        %{buildroot}%{_datadir}/nexuiz/data/

%{__install} -p data/common-spog.pk3 \
        %{buildroot}%{_datadir}/nexuiz/data/

%clean
%{__rm} -rf %{buildroot}

%files
%doc Readme.htm cvars.txt mapping.txt
%doc gamemodes.txt FAQ* gpl.txt
%doc mapping.txt say-escapes.txt scorelog.txt
%doc eventlog.txt mapdownload.txt server
%{_datadir}/nexuiz/

%changelog
* Fri Jul 15 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 2.5.2
- Rebuild for Fedora
* Mon May 19 2008 Jon Ciesla <limb@jcomserv.net> - 2.4.2-1
- New upstream release.
* Tue Apr 29 2008 Jon Ciesla <limb@jcomserv.net> - 2.4-1
- New upstream release.
* Tue Aug 21 2007 Jon Ciesla <limb@jcomserv.net> - 2.3-3
- License tag correction.
* Mon Jul 02 2007 Jon Ciesla <limb@jcomserv.net> - 2.3-2
- Added disttag.
* Tue Jun 19 2007 Jon Ciesla <limb@jcomserv.net> - 2.3-1
- Updated to 2.3
* Thu Mar 01 2007 Adrian Reber <adrian@lisas.de> - 2.2.3-1
- updated to 2.2.3
* Mon Dec 18 2006 Adrian Reber <adrian@lisas.de> - 2.2.1-1
- updated to 2.2.1 (#220034)
- fix for CVE-2006-6609, CVE-2006-6610
* Sun Sep 24 2006 Adrian Reber <adrian@lisas.de> - 2.1-1
- updated to 2.1
* Mon Jun 26 2006 Adrian Reber <adrian@lisas.de> - 2.0-2
- upstream changed the sources without increasing the
  version and they also seem to add and remove some of
  the files or just changing their location randomly
* Sun Jun 18 2006 Adrian Reber <adrian@lisas.de> - 2.0-1
- updated to 2.0
* Thu Mar 16 2006 Adrian Reber <adrian@lisas.de> - 1.5-1
- updated to 1.5
* Mon Sep 19 2005 Adrian Reber <adrian@lisas.de> - 1.2.1-1
- updated to 1.2.1
* Sat Sep 03 2005 Adrian Reber <adrian@lisas.de> - 1.2-2
- I should really test my changes before check-in
* Fri Sep 02 2005 Adrian Reber <adrian@lisas.de> - 1.2-1
- updated to 1.2
- included serverfix12.zip
* Fri Jul  8 2005 Matthias Saou <http://freshrpms.net/> 1.1-0
- Split off data from the main package, will make fixing the binaries much
  easier and allow sharing this noarch package between archs. It also avoids
  shipping the source full of the already provided binary builds.
- Don't gz/bzip2 the source as it saves 252kB of 152MB at best and wastes time
  (the data is already a huge compressed .pk3).
