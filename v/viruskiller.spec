Summary: Frantic shooting game where viruses invade your computer
Name: viruskiller
Version: 1.0
Release: 1
License: GPLv2+
Group: Amusements/Games
URL: https://www.parallelrealities.co.uk/virusKiller.php
# No absolute URL since the home page tunnels it through a PHP script
Source: viruskiller-%{version}-1.tar.gz
Patch0: viruskiller-1.0-makefile.patch
BuildRequires: SDL-devel, SDL_mixer-devel, SDL_image-devel, SDL_ttf-devel
BuildRequires: zlib-devel, desktop-file-utils

%description
Your computer has been invaded! Dozens of little viruses are pouring in via
security holes in Microsoft Internet Explorer, Microsoft Outlook, Microsoft
MSN Messenger and Microsoft Recycle Bin!! Using your trusty mouse you must
shoot the buggers before they can destroy your files! Some will steal them
from their home directories and take them back to their security hole. Others
will just eat them right there on the spot! See how long you and your computer
can survive the onslaught!

%prep
%setup -q
%patch 0 -p1 -b .makefile
# Replace the displayed location of the help (in-game) to the proper one
%{__perl} -pi -e 's|/usr/share/doc/viruskiller/manual.html|%{_docdir}/%{name}-%{version}/manual.html|g' data/titleWidgets
# No files need to be executable, yet quite a few are, so fix that
find . -type f -exec %{__chmod} -x {} \;
sed -i 's|gzclose(pak);|fclose(pak);|' src/pak.cpp

%build
%{__make} %{?_smp_mflags} PREFIX="%{_prefix}" OPTFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

# Remove shipped menu entry, no Comment, wrong Exec... :-(
%{__rm} -f %{buildroot}%{_datadir}/applications/viruskiller.desktop

# Install menu entry
%{__cat} > %{name}.desktop << EOF
[Desktop Entry]
Name=Virus Killer
Name[zh_TW]=病毒入侵
Comment=Frantic shooting game where viruses invade your computer
Icon=viruskiller.png
Exec=viruskiller
Terminal=false
Type=Application
Categories=Game;ArcadeGame;
Encoding=UTF-8
EOF

%{__mkdir_p} %{buildroot}%{_datadir}/applications
desktop-file-install \
    --vendor "" \
    --dir %{buildroot}%{_datadir}/applications \
    %{name}.desktop

%files
%doc doc/*
%{_bindir}/viruskiller
%{_datadir}/viruskiller/
%{_datadir}/pixmaps/viruskiller.png
%{_datadir}/applications/%{name}.desktop

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0
- Rebuilt for Fedora
* Tue Nov 25 2008 Wind <yc.yan@ossii.com.tw> - 1.0-8
- Rebuild for OSSII.
* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0-7
- Autorebuild for GCC 4.3
* Thu Aug 23 2007 Matthias Saou <https://freshrpms.net/> 1.0-6
- Rebuild for new BuildID feature.
* Sun Aug  5 2007 Matthias Saou <https://freshrpms.net/> 1.0-5
- Update License field.
- Remove dist tag, since the package will seldom change.
- Remove desktop file prefix.
* Thu Jun 14 2007 Matthias Saou <https://freshrpms.net/> 1.0-4
- Move binary and data to "proper" locations by updating patch (#243031).
- Remove executable bit from all files from the archive, it shouldn't be set.
* Fri Feb  2 2007 Matthias Saou <https://freshrpms.net/> 1.0-3
- Make in-game help display the proper location for the manual.html (#220404).
* Mon Aug 28 2006 Matthias Saou <https://freshrpms.net/> 1.0-2
- FC6 rebuild.
- Add -lz to LIBS in the makefile patch (no longer in SDL libs?).
* Mon Mar  6 2006 Matthias Saou <https://freshrpms.net/> 1.0-1
- Update to 1.0-1.
- Update makefile patch.
- Remove no longer needed zziplib patch.
- No longer build require zziplib-devel, but zlib-devel instead.
* Thu Feb  9 2006 Matthias Saou <https://freshrpms.net/> 0.9-6
- Rebuild for new gcc/glibc.
- Remove old desktop file conditionals.
* Tue May 31 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.9-5
- rebuild once more as 0.9-4 src.rpm failed to build in build system
* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 0.9-4
- rebuild on all arches
* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt
* Sun Feb 27 2005 Matthias Saou <https://freshrpms.net/> 0.9-2
- Fix release tag.
* Tue Jun  8 2004 Matthias Saou <https://freshrpms.net/> 0.9-1
- Initial RPM release.
