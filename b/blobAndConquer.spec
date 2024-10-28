Name:           blobAndConquer
Version:        1.11
Release:        1
Summary:        Blob Wars 2: Blob And Conquer
Group:          Amusements/Games
License:        GPLv2+ and Redistributable, no modification permitted
URL:            https://github.com/perpendicular-dimensions/blobandconquer
Source0:        blobandconquer-master.zip
Source1:        %{name}-1.0-music.tar.bz2
Patch0:         %{name}-1.0-defines.patch
Patch1:         %{name}-1.0-desktop.patch
BuildRequires:  SDL2_image-devel SDL2_mixer-devel SDL2_ttf-devel zlib-devel
BuildRequires:  desktop-file-utils
Requires:       hicolor-icon-theme opengl-games-utils

%description
With the apparent defeat of Galdov and the reclaiming of the Fire, Time, Space
and Reality Crystals the Blobs' battle was only just beginning. Bob had rescued
many Blobs and fought many battles, but now he had an ever bigger task ahead of
him. The Blobs' homeworld is still littered with the alien forces and Bob once
again makes it his task to lead the counter attack. But even without Galdov the
aliens are still extremely well organised...

They're Ready. Will You Be?


%prep
%setup -q -n blobandconquer-master -a 1
#patch0 -p1
%patch 1 -p1
# some cleanup
chmod -x gfx/rw2/*.raw data/gameDefs/defines.h `find src -type f`
sed -i 's/\r//g' data/gameDefs/defines.h `find src -type f`
sed -i 's/Exec=blobAndConquer/Exec=blobAndConquer-wrapper/' \
  icons/blobAndConquer.desktop
#sed -i -e 's/-o root -g games//g' -e 's/-Wformat-security/-Wno-format-security/g' -e 's/-lGL/-lGL -lX11/' makefile
sed -i 's|gzclose(pak)|fclose(pak)|' src/pak.cpp

%build
make CFLAGS="$RPM_OPT_FLAGS" DOCDIR=%{_docdir}/%{name}-%{version}/ \
  DATADIR=%{_datadir}/%{name}/ all buildpak


%install
%__rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT BINDIR=%{_bindir}/ \
  DOCDIR=%{_docdir}/%{name}-%{version}/ \
  DATADIR=%{_datadir}/%{name}/ \
  ICONDIR=%{_datadir}/icons/hicolor/
#ln -s opengl-game-wrapper.sh $RPM_BUILD_ROOT%{_bindir}/%{name}-wrapper
#cp -p README.fedora-music $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

desktop-file-install --vendor fedora --delete-original \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  --add-category ActionGame \
  --remove-key Version \
  $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop



%post
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
   %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%postun
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
   %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%files
%doc %{_docdir}/%{name}-%{version}
%{_bindir}/%{name}*
# the data/gameDefs/defines.h file is needed runtime and thus not a devel file!
%{_datadir}/%{name}
%{_datadir}/applications/fedora-%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/locale/pl/LC_MESSAGES/blobAndConquer.mo

%changelog
* Sun Mar 12 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 1.11
- Rebuilt for Fedora
* Thu Oct 23 2008 Wind <yc.yan@ossii.com.tw> 1.0-2
- Rebuild for OSSII.
* Tue Sep 30 2008 Hans de Goede <hdegoede@redhat.com> 1.0-1
- New upstream release 1.0
* Wed Sep 17 2008 Rafał Psota <rafalzaq@gmail.com> 0.98-2
- Remove nonfree sound files
* Wed Jul  9 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.98-1
- New upstream release 0.98
* Thu Jun 26 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.96-1
- New upstream release 0.96
* Mon Jun 16 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.95-1
- New upstream release 0.95
* Thu Jun 12 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.94-1
- New upstream release 0.94
- Drop all patches (all upstream now)
* Sat May 17 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.93-2
- Fix only the last line of in between levels cutscenes text showing (449295)
* Tue May 13 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.93-1
- New upstream release 0.93
* Mon Apr 28 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.92-1
- New upstream release 0.92
* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.91-6
- Autorebuild for GCC 4.3
* Mon Dec 31 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.91-5
- Fix restoring of resolution when exiting a fullscreen game
* Mon Sep 24 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.91-4
- Use opengl-games-utils wrapper to show error dialog when DRI is missing
* Tue Aug 21 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.91-3
- Rebuild for buildId
* Sun Aug 12 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.91-2
- Update License tag for new Licensing Guidelines compliance
- Fix invalid desktop file (fix building with latest desktop-file-utils)
* Sun Jun  3 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.91-1
- New upstream release 0.91-1
- Drop upstreamed patches
* Thu May 24 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.90-2
- Add missing desktop-file-utils BuildRequire
* Fri May 18 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.90-1
- Initial Fedora package
