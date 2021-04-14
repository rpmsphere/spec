%undefine _debugsource_packages

Name: umplayer
Summary: Complete Frontend for MPlayer
Version: 0.98.2
Source0: http://mirror.ufs.ac.za/smplayer/UMPlayer/%{version}/%{name}-%{version}-by-the-smplayer-team.tar.bz2
Release: 5.1
License: GPLv2+
Group: Applications/Multimedia
URL: http://www.umplayer.com/
BuildRequires:  desktop-file-utils
BuildRequires:  qt-devel
BuildRequires:  gcc-c++
Requires:       mplayer

%description
Qt Mplayer front-end, with basic features like playing
videos, DVDs, and VCDs to more advanced features like support
for MPlayer filters and more. One of the most interesting features
of UMPlayer: it remembers the settings of all files you play.
So you start to watch a movie but you have to leave... don't
worry, when you open that movie again it will resume at the same
point you left it, and with the same settings: audio track,
subtitles, volume...

%prep
%setup -q -n %{name}-%{version}-by-the-smplayer-team

%build
%{__make} PREFIX=%{_prefix} QMAKE=%{_libdir}/qt4/bin/qmake LRELEASE=%{_libdir}/qt4/bin/lrelease %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}

%{__make} PREFIX=%{_prefix} DOC_PATH=%{_docdir}/%{name}-%{version} QMAKE=%{_libdir}/qt4/bin/qmake LRELEASE=%{_libdir}/qt4/bin/lrelease DESTDIR=%{buildroot} install

desktop-file-install --delete-original \
--add-category="AudioVideo" \
--add-category="Player" \
--add-category="Video" \
--dir %{buildroot}%{_datadir}/applications/ \
%{buildroot}%{_datadir}/applications/%{name}.desktop

desktop-file-install --delete-original \
--add-category="AudioVideo" \
--add-category="Player" \
--add-category="Video" \
--dir %{buildroot}%{_datadir}/applications/ \
%{buildroot}%{_datadir}/applications/%{name}_enqueue.desktop

%clean
%{__rm} -rf %{buildroot}

%post
touch --no-create %{_datadir}/icons/hicolor
gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
update-desktop-database &> /dev/null || :

%postun
touch --no-create %{_datadir}/icons/hicolor
gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
update-desktop-database &> /dev/null || :

%files
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/icons/*
%{_mandir}/man*/*
%{_datadir}/umplayer
%{_docdir}/%{name}-%{version}

%changelog
* Tue Feb 17 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0.98.2
- Rebuilt for Fedora
* Sat May 28 2011 Sawa <sawa@ikoinoba.net> - 0.95-1.svn163
- Initial package
