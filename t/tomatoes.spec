Name:           tomatoes
Version:        1.55
Release:        1
Summary:        I Have No Tomatoes
License:        zlib/libpng
Group:          Amusements/Games
URL:            https://%{name}.sourceforge.net
Source0:        https://dl.sourceforge.net/sourceforge/%{name}/%{name}-linux-src-%{version}.tar.bz2
Source1:        https://dl.sourceforge.net/sourceforge/%{name}/%{name}-linux-1.5.tar.bz2
Patch0:         tomatoes-makefile.patch
Patch1:         tomatoes-configdir.patch
Patch2:         tomatoes-hiscoredir.patch
BuildRequires:  SDL_mixer-devel SDL_image-devel SDL-devel mesa-libGL-devel gcc-c++
BuildRequires:  desktop-file-utils

%description
I Have No Tomatoes is an extreme leisure time activity idea of which culminates
in the following question: How many tomatoes can you smash in ten short minutes?
If you have the time to spare, this game has the vegetables just waiting to be
eliminated!

%prep
%setup -q -a1
%{__mv} tomatoes-1.5/* .
%{__rm} -rf tomatoes-1.5
%patch 0
%patch 1
%patch 2
sed -i 's/\r$//' README

%build
CFLAGS="%{optflags}" %{__make} MPKDIR='%{_datadir}/%{name}/' \
  MUSICDIR='%{_datadir}/%{name}/music/' \
  CONFIGDIR='%{_sysconfdir}/%{name}/' %{?_smp_mflags}

%install
%{__install} -p -D -m 0755 '%{name}' '%{buildroot}%{_bindir}/%{name}'
%{__install} -d -m 0755 '%{buildroot}%{_datadir}/%{name}'
%{__install} -p -D -m 0644 tomatoes.mpk '%{buildroot}%{_datadir}/%{name}'
%{__install} -d -m 0755 '%{buildroot}%{_datadir}/%{name}/music'
%{__install} -p -D -m 0644 music/* '%{buildroot}%{_datadir}/%{name}/music'
%{__install} -p -D -m 0644 config.cfg '%{buildroot}%{_sysconfdir}/%{name}/config.cfg'
%{__install} -p -D -m 0644 icon.png '%{buildroot}%{_datadir}/pixmaps/%{name}.png'

%{__install} -d -m 0755 '%{buildroot}%{_datadir}/applications'
%{__cat} > '%{buildroot}%{_datadir}/applications/%{name}.desktop' <<EOF
[Desktop Entry]
Type=Application
Name=I Have No Tomatoes
Exec=%{name}
Icon=%{name}
Categories=Game;ActionGame;
EOF

%files
%doc README
%{_bindir}/%{name}
%config %{_sysconfdir}/%{name}
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.55
- Rebuilt for Fedora
* Wed Aug 01 2012 Kevin Chen <kevin.chen@ossii.com.tw>
- Rebuild for OSSII
* Sat Jul  2 2011 jengelh@medozas.de
- Use %%_smp_mflags for parallel building
- Strip %%clean section (not needed on BS)
* Tue May 12 2009 cmorve69@yahoo.es
- Initial package
