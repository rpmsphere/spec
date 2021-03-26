Summary: Atomix clone where you create figures out of marbles
Name: lmarbles
Version: 1.0.8
Release: 1
License: GPLv2+
Group: Amusements/Games
URL: http://lgames.sourceforge.net/
Source: http://dl.sf.net/lgames/lmarbles-%{version}.tar.gz
BuildRequires: SDL-devel, SDL_mixer-devel, desktop-file-utils, ImageMagick
Obsoletes: marbles <= 1.0.5

%description
LMarbles is an Atomix clone with a slight change in concept. Instead of
assembling molecules you create figures out of marbles. Nevertheless, the
basic game play is the same: If a marble starts to move it will not stop
until it hits a wall or another marble. To make it more interesting there
are obstacles like one-way streets, crumbling walls and portals.
As Marbles is meant as a puzzle game you play against a move limit and not
a time limit. This way you have as much time as you need to think.

%prep
%setup -q

%build
%configure --localstatedir=%{_var}/lib/games
%{__make} %{?_smp_mflags}
# Having it as png seems more consistent
convert lmarbles48.gif lmarbles.png

%install
%{__make} install DESTDIR=%{buildroot}
%{__install} -D lmarbles.png %{buildroot}%{_datadir}/pixmaps/lmarbles.png

%{__cat} > %{name}.desktop << EOF
[Desktop Entry]
Name=LMarbles
Comment=Atomix clone where you create figures out of marbles
Exec=lmarbles
Icon=lmarbles.png
Terminal=false
Type=Application
Categories=Game;LogicGame;
Encoding=UTF-8
EOF

%{__mkdir_p} %{buildroot}%{_datadir}/applications
desktop-file-install --vendor "" \
    --dir %{buildroot}%{_datadir}/applications \
    %{name}.desktop

%post
update-desktop-database %{_datadir}/applications &>/dev/null || :

%postun
update-desktop-database %{_datadir}/applications &>/dev/null || :

%files
%doc AUTHORS COPYING ChangeLog README TODO
%attr(2551,root,games) %{_bindir}/lmarbles
%{_datadir}/applications/lmarbles.desktop
%{_datadir}/lmarbles/
%{_datadir}/pixmaps/lmarbles.png
%{_mandir}/man6/lmarbles.6*
%config(noreplace) %attr(664,games,games) %{_var}/lib/games/lmarbles.prfs
%exclude %{_datadir}/icons/lmarbles48.gif

%changelog
* Wed Nov 27 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.8
- Rebuild for Fedora

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.7-27
- Escape macros in %%changelog

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Oct 05 2015 Jaromir Capik <jcapik@redhat.com> - 1.0.7-21
- Adding the missing distag (#1237177)
- Cleaning the spec

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 13 2009 Matthias Saou <http://freshrpms.net/> 1.0.7-10
- Add LogicGame category to the desktop file (#485359).

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org>
- Autorebuild for GCC 4.3

* Wed Aug 22 2007 Matthias Saou <http://freshrpms.net/> 1.0.7-8
- Rebuild for new BuildID feature.

* Sun Aug  5 2007 Matthias Saou <http://freshrpms.net/> 1.0.7-7
- Update License field.
- Remove dist tag, since the package will seldom change.

* Mon Aug 28 2006 Matthias Saou <http://freshrpms.net/> 1.0.7-6
- FC5 rebuild.
- Add %%{?dist} tag.
- Remove explicit SDL* libraries requirements.

* Mon Mar  6 2006 Matthias Saou <http://freshrpms.net/> 1.0.7-5
- FC5 rebuild.

* Thu Feb  9 2006 Matthias Saou <http://freshrpms.net/> 1.0.7-4
- Rebuild for new gcc/glibc.

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 1.0.7-3
- rebuild on all arches

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Wed Jan 26 2005 Matthias Saou <http://freshrpms.net/> 1.0.7-1
- Update to 1.0.7.

* Wed May 19 2004 Matthias Saou <http://freshrpms.net/> 1.0.6-3
- Rebuild for Fedora Core 2.
- Added menu icon.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 1.0.6-2
- Rebuild for Fedora Core 1.
- Added missing SDL_mixer depencency.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.0.6 and renamed to lmarbles.
- Rebuilt for Red Hat Linux 9.

* Fri Oct  4 2002 Matthias Saou <http://freshrpms.net/>
- Update to 1.0.5.
- Rebuilt for Red Hat Linux 8.0.
- New menu entry.

* Tue Jul  2 2002 Matthias Saou <http://freshrpms.net/>
- Update to 1.0.4.

* Tue Jun 25 2002 Matthias Saou <http://freshrpms.net/>
- Update to 1.0.3.

* Thu May  2 2002 Matthias Saou <http://freshrpms.net/>
- Update to 1.0.2.
- Rebuilt against Red Hat Linux 7.3.
- Added the %%{?_smp_mflags} expansion.

* Fri Feb  8 2002 Matthias Saou <http://freshrpms.net/>
- Update to 1.0.1

* Thu Apr 24 2001 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat 7.1.

* Thu Mar  8 2001 Matthias Saou <http://freshrpms.net/>
- Update to 010307.

* Tue Jan  2 2001 Matthias Saou <http://freshrpms.net/>
- Initial RPM release for RedHat 7.0

